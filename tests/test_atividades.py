import pytest

from ex03_contador_vogais import contador_de_vogais
from ex03_contador_vogais import main as main_ex03


class Test_Ex03ContadorVogais:
    @pytest.mark.parametrize(
        "texto,resposta",
        [
            ("", 0),
            (" ", 0),
            ("q w r t y", 0),
            ("a", 1),
            ("A linguagem Python é muito versátil.", 13),
            ("CAIXA ALTA  e caixa baixa", 12),
            ("à pé maçã pô", 5),
        ],
    )
    def test_contador_de_vogais(self, texto, resposta):
        assert resposta == contador_de_vogais(texto)

    @pytest.mark.parametrize(
        "texto,resposta",
        [(None, AttributeError), (123, AttributeError), ([1, 2], AttributeError)],
    )
    def test_contador_de_vogais_erros(self, texto, resposta):
        with pytest.raises(resposta):
            contador_de_vogais(texto)

    @pytest.mark.parametrize(
        "entrada,resposta",
        [
            ("", "O texto não contém vogais."),
            (" ", "O texto não contém vogais."),
            ("q w r t y", "O texto não contém vogais."),
            ("a", "O texto contém 1 vogal."),
            ("A linguagem Python é muito versátil.", "O texto contém 13 vogais."),
            ("CAIXA ALTA  e caixa baixa", "O texto contém 12 vogais."),
            ("à pé maçã pô", "O texto contém 5 vogais."),
        ],
    )
    def test_main(self, monkeypatch, capsys, entrada, resposta):
        monkeypatch.setattr("builtins.input", lambda _: entrada)
        main_ex03()
        saida_capturada = capsys.readouterr().out.strip()
        assert resposta == saida_capturada
