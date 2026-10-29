
import pytest

from dividir import dividir


def test_dividir_dos_enteros():
    assert dividir(10, 2) == 5.0


def test_dividir_con_resultado_decimal():
    assert dividir(5, 2) == 2.5


def test_dividir_numeros_negativos():
    assert dividir(-10, 2) == -5.0


def test_dividir_entre_cero():
    with pytest.raises(ZeroDivisionError):
        dividir(10, 0)
