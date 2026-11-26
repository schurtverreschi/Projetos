import pytest

from ex01_calculadora_gorjeta import calcular_gorjeta
from ex01_calculadora_gorjeta import main as main_ex01


class TestEx01Gorjeta:
    @pytest.mark.parametrize(
        "conta,porcentagem_gorjeta,gorjeta,total_esperado",
        [(120, 10, 12, 132), (150, 7.5, 11.25, 161.25)],
    )
    def test_calcular_gorjeta(
        self, conta, porcentagem_gorjeta, gorjeta, total_esperado
    ):
        assert (gorjeta, total_esperado) == calcular_gorjeta(conta, porcentagem_gorjeta)

    @pytest.mark.parametrize("conta,porcentagem_gorjeta", [("abc", 10), (150, "dez")])
    def test_calcular_gorjeta_type_error(self, conta, porcentagem_gorjeta):
        with pytest.raises(TypeError):
            calcular_gorjeta(conta, porcentagem_gorjeta)

    @pytest.mark.parametrize(
        "conta,porcentagem_gorjeta,total_esperado",
        [("120", "10", "132"), ("150", "7.5", "161.25"), ("75,80", "10", "83.38")],
    )
    def test_main_entrada_valida(
        self, monkeypatch, capsys, conta, porcentagem_gorjeta, total_esperado
    ):
        # Prepara a fila de respostas simuladas do usuário
        entradas = iter([conta, porcentagem_gorjeta])
        # Substitui o input() real pelo nosso simulador
        monkeypatch.setattr("builtins.input", lambda _: next(entradas))

        main_ex01()

        # Captura tudo o que foi impresso no terminal
        saida_capturada = capsys.readouterr().out

        assert total_esperado in saida_capturada

    @pytest.mark.parametrize(
        "conta,porcentagem_gorjeta", [("abc", "10"), ("150", "dez")]
    )
    def test_main_entrada_invalida(
        self, monkeypatch, capsys, conta, porcentagem_gorjeta
    ):
        # Simula o usuário digitando texto no primeiro input
        entradas = iter([conta, porcentagem_gorjeta])
        monkeypatch.setattr("builtins.input", lambda _: next(entradas))

        main_ex01()

        saida_capturada = capsys.readouterr().out

        # Valida se a sua mensagem amigável de erro foi exibida
        assert "Erro" in saida_capturada
