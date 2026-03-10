from app import saludar


def test_saludar():
    assert saludar("Ana") == "Hola, Ana"
