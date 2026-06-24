from src.main import main

def test_main(capsys):
    main()
    captured = capsys.readouterr()
    assert "aula02_automação_dados" in captured.out
