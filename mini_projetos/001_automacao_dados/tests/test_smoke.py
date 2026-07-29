from src.main import main

def test_main(capsys):
    main()
    captured = capsys.readouterr()
    assert "001_automacao_dados" in captured.out
