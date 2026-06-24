#!/usr/bin/env bash
set -euo pipefail

if [[ ! -d ".venv" ]]; then
  echo "❌ .venv não existe neste projeto."
  echo "Crie com: python3 -m venv .venv"
  exit 1
fi

# shellcheck disable=SC1091
source .venv/bin/activate

cmd="${1:-help}"
shift || true

freeze_runtime() {
  pip freeze | grep -viE '^(pytest|pluggy|packaging|iniconfig|exceptiongroup|tomli)(==|$)' > requirements.txt || true
  echo "✅ requirements.txt atualizado"
}

freeze_dev() {
  pip freeze | grep -iE '^(pytest|pluggy|packaging|iniconfig|exceptiongroup|tomli)(==|$)' > requirements-dev.txt || true
  echo "✅ requirements-dev.txt atualizado"
}

case "$cmd" in
  run)
    python -m src.main
    ;;
  test)
    pytest -q
    ;;
  freeze)
    freeze_runtime
    freeze_dev
    ;;
  install)
    [[ -f requirements.txt ]] && pip install -r requirements.txt
    [[ -f requirements-dev.txt ]] && pip install -r requirements-dev.txt
    ;;
  add)
    if [[ $# -eq 0 ]]; then
      echo "Uso: ./dev.sh add pacote [pacote2 ...]"
      exit 1
    fi
    pip install "$@"
    freeze_runtime
    ;;
  add-dev)
    if [[ $# -eq 0 ]]; then
      echo "Uso: ./dev.sh add-dev pacote [pacote2 ...]"
      exit 1
    fi
    pip install "$@"
    freeze_dev
    ;;
  recreate-venv)
    rm -rf .venv
    python3 -m venv .venv
    # shellcheck disable=SC1091
    source .venv/bin/activate
    python -m pip install -U pip wheel setuptools
    [[ -f requirements.txt ]] && pip install -r requirements.txt
    [[ -f requirements-dev.txt ]] && pip install -r requirements-dev.txt
    echo "✅ Ambiente recriado com sucesso"
    ;;
  info)
    echo "📁 Projeto: $(pwd)"
    echo "🐍 Python: $(which python)"
    echo "📦 Pip: $(which pip)"
    echo
    pip list
    ;;
  shell)
    echo "✅ Ambiente ativado. Para sair, use: exit"
    exec bash --noprofile --norc
    ;;
  help|*)
    echo "Uso: ./dev.sh [run|test|freeze|install|add|add-dev|recreate-venv|info|shell]"
    ;;
esac
