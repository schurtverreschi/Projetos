import pytest

from ex02_validador_CPF import main as main_ex02
from ex02_validador_CPF import validar_cpf


class TestEx02CPF:
    @pytest.mark.parametrize(
        "numero,resposta",
        [
            ("123.456.789-10", "CPF valido."),
            ("12345678910", "CPF valido."),
            ("  12345678910 ", "CPF valido."),
            ("123456789 10", "CPF valido."),
        ],
    )
    def test_validar_cpf(self, numero, resposta):
        assert resposta == validar_cpf(numero)

    @pytest.mark.parametrize(
        "numero,resposta",
        [
            ("123.abc.789-10", "Erro: O CPF deve conter apenas números."),
            ("1234567891011", "Erro: O CPF deve ter exatamente 11 dígitos."),
        ],
    )
    def test_validar_cpf_errado(self, numero, resposta):
        assert resposta == validar_cpf(numero)

    @pytest.mark.parametrize(
        "entrada,resposta",
        [
            ("123.456.789-10", "CPF valido."),
            ("12345678910", "CPF valido."),
            ("  12345678910 ", "CPF valido."),
            ("123456789 10", "CPF valido."),
        ],
    )
    def test_main_entrada_valida(self, monkeypatch, capsys, entrada, resposta):
        monkeypatch.setattr("builtins.input", lambda _: entrada)
        main_ex02()
        saida_capturada = capsys.readouterr().out.strip()
        assert resposta == saida_capturada

    @pytest.mark.parametrize(
        "entrada,resposta",
        [
            ("123.abc.789-10", "Erro: O CPF deve conter apenas números."),
            ("1234567891011", "Erro: O CPF deve ter exatamente 11 dígitos."),
        ],
    )
    def test_main_entrada_invalida(self, monkeypatch, capsys, entrada, resposta):
        monkeypatch.setattr("builtins.input", lambda _: entrada)
        main_ex02()
        saida_capturada = capsys.readouterr().out.strip()
        assert resposta == saida_capturada
