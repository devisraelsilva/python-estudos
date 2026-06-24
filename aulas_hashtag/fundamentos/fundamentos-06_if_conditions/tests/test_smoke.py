from src.main import main

def test_main(capsys):
    main()
    captured = capsys.readouterr()
    assert "fundamentos-06_if_conditions" in captured.out
