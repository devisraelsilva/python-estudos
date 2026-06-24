from src.main import main

def test_main(capsys):
    main()
    captured = capsys.readouterr()
    assert "fundamentos-04_misturando_tipos_variaveis" in captured.out
