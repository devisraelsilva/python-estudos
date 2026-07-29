#!/usr/bin/env bash
set -euo pipefail

PYTHON=".venv/bin/python"
PIP=".venv/bin/python -m pip"

if [[ ! -x "$PYTHON" ]]; then
  echo "❌ .venv não existe ou está incompleta neste projeto."
  echo "Use: ./dev.sh recreate-venv"
  exit 1
fi

cmd="${1:-help}"
shift || true

freeze_runtime() {
  $PIP freeze | grep -viE '^(pytest|ipykernel|pluggy|packaging|iniconfig|exceptiongroup|tomli|pygments|ipython|jupyter|jupyter-client|jupyter-core|traitlets|debugpy|comm|matplotlib-inline|nest-asyncio|parso|pexpect|prompt_toolkit|ptyprocess|pure_eval|stack_data|tornado|wcwidth|executing|asttokens|decorator|jedi)(==|$)' > requirements.txt || true
  echo "✅ requirements.txt atualizado"
}

case "$cmd" in
  run)
    "$PYTHON" -m src.main
    ;;

  test)
    "$PYTHON" -m pytest -q
    ;;

  install)
    [[ -f requirements.txt ]] && $PIP install -r requirements.txt
    [[ -f requirements-dev.txt ]] && $PIP install -r requirements-dev.txt
    ;;

  add)
    if [[ $# -eq 0 ]]; then
      echo "Uso: ./dev.sh add pacote [pacote2 ...]"
      exit 1
    fi
    $PIP install "$@"
    freeze_runtime
    ;;

  add-dev)
    if [[ $# -eq 0 ]]; then
      echo "Uso: ./dev.sh add-dev pacote [pacote2 ...]"
      exit 1
    fi
    $PIP install "$@"
    $PIP freeze > requirements-dev.txt
    echo "✅ requirements-dev.txt atualizado"
    ;;

  recreate-venv)
    rm -rf .venv
    python3 -m venv .venv
    .venv/bin/python -m pip install -U pip wheel setuptools
    [[ -f requirements.txt ]] && .venv/bin/python -m pip install -r requirements.txt
    [[ -f requirements-dev.txt ]] && .venv/bin/python -m pip install -r requirements-dev.txt
    echo "✅ Ambiente recriado com sucesso"
    ;;

  info)
    echo "📁 Projeto: $(pwd)"
    echo "🐍 Python: $("$PYTHON" -c 'import sys; print(sys.executable)')"
    echo "📦 Pip: $("$PYTHON" -m pip --version)"
    echo
    $PIP list
    ;;

  doctor)
    echo "🔍 Verificando ambiente..."
    echo
    "$PYTHON" -m pytest --version
    "$PYTHON" -m ipykernel --version
    ;;

  help|*)
    echo "Uso: ./dev.sh [run|test|install|add|add-dev|recreate-venv|info|doctor]"
    ;;
esac
