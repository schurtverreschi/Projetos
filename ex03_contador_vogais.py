def contador_de_vogais(texto):

    vogais = 0

    for v in texto.lower():
        if v in "aàáâãeèéêẽiìíîĩoòóôõuùúûũ":
            vogais += 1

    return vogais


def main():
    entrada = input("Digite um texto: ")
    qtd_vogais = contador_de_vogais(entrada)
    if qtd_vogais == 0:
        print("O texto não contém vogais.")
    elif qtd_vogais == 1:
        print("O texto contém 1 vogal.")
    else:
        print(f"O texto contém {qtd_vogais} vogais.")


if __name__ == "__main__":  # pragma: no cover
    main()


# Contagem de vogais em um texto

# Mariana é professora de língua portuguesa e quer um programa que conte quantas vogais há em um texto digitado pelos alunos. Isso ajudará a analisar a estrutura das palavras utilizadas.

# Crie um programa que peça um texto e exiba quantas vogais (a, e, i, o, u) ele contém.

# Exemplo de entrada:

# Digite um texto: A linguagem Python é muito versátil.

# Saída esperada:

# O texto contém 13 vogais.
