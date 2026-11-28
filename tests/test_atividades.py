import pytest

from ex04_identificador_palavra_longa import identificador_palavras_longas
from ex04_identificador_palavra_longa import main as main_ex04


class TestEx04IdentificardoPalavraLonga:
    @pytest.mark.parametrize(
        "texto,resposta",
        [
            ("", []),
            ("Leia o dicionário", ["dicionário"]),
            (
                "A programação estruturada facilitou o desenvolvimento de grandes sistemas computacionais",
                ["programação", "estruturada", "desenvolvimento", "computacionais"],
            ),
        ],
        ids=["Vazio", "Uma palavra", "Muitas palavras"],
    )
    def test_identificador_palavra_longa(self, texto, resposta):
        retorno = identificador_palavras_longas(texto)
        assert resposta == retorno

    @pytest.mark.parametrize("texto,resposta", [(None, TypeError), (123, TypeError)])
    def test_identificador_palavra_longa_erro(self, texto, resposta):
        with pytest.raises(resposta):
            identificador_palavras_longas(texto)

    @pytest.mark.parametrize(
        "entrada,resposta",
        [
            ("", "Nenhum texto inserido."),
            (
                "Texto com palavras pequenas.",
                "Nenhuma palavra longa foi encontrada no texto.",
            ),
            ("Leia o dicionário", "Palavras longas encontradas: Dicionário."),
            (
                "A programação estruturada facilitou o desenvolvimento de grandes sistemas computacionais",
                "Palavras longas encontradas: Programação, Estruturada, Desenvolvimento, Computacionais.",
            ),
        ],
        ids=["Vazio", "Sem palavra grande", "Uma palavra", "Muitas palavras"],
    )
    def test_main(self, monkeypatch, capsys, entrada, resposta):
        monkeypatch.setattr("builtins.input", lambda _: entrada)
        main_ex04()
        saida_capturada = capsys.readouterr().out.strip()
        assert resposta == saida_capturada


# ZOMBIES TDD - zero one many boundary interface exception simples scenario

# testar se função conta e retorna lista com palavras grandes(10+ letras)

# ok Z: NONE ""
# ok O: Uma única palavra de 10 letras
# ok M: Texto repleto de palavras grandes
# ok B: palavras com 9 letras
# I:
# E: int
