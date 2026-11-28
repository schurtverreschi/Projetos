def identificador_palavras_longas(texto):
    try:
        lista_palavras = texto.split()
        lista_palavras_longas = [p for p in lista_palavras if len(p) >= 10]
        return lista_palavras_longas
    except AttributeError:
        raise TypeError


def main():
    entrada = input("Digite um texto: ")

    if entrada.strip() == "":
        print("Nenhum texto inserido.")
    else:
        lista = identificador_palavras_longas(entrada)
        saida = [p.capitalize() for p in lista]
        if saida:
            print(f"Palavras longas encontradas: {', '.join(saida)}.")
        else:
            print("Nenhuma palavra longa foi encontrada no texto.")


if __name__ == "__main__":
    main()


# Identificando palavras mais longas em um texto

# Sofia é revisora de textos e precisa identificar palavras muito longas em um parágrafo. Textos mais fáceis de ler costumam ter palavras curtas, então ela quer um programa que encontre palavras que tenham mais de 10 letras e as exiba em destaque.

# Crie um programa que receba um texto e exiba todas as palavras que possuem mais de 10 letras. Caso nenhuma palavra longa seja encontrada, o programa deve avisar o usuário.

# Exemplo de entrada:

# Digite um texto: A programação estruturada facilitou o desenvolvimento de grandes sistemas computacionais

# Saída esperada:

# Palavras longas encontradas: programação, estruturada, desenvolvimento, computacionais

# Se nenhum palavra longa for encontrada:

# Nenhuma palavra longa foi encontrada no texto.
