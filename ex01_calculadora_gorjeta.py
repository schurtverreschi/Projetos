def calcular_gorjeta(conta, porcentagem_gorjeta):
    gorjeta = conta * porcentagem_gorjeta / 100
    total_conta = conta + gorjeta
    return gorjeta, total_conta


def main():
    try:
        conta = float(input("Digite o valor da conta: ").replace(",", "."))
        porcentagem_gorjeta = float(
            input("Digite o percentual de gorjeta desejado: ").replace(",", ".")
        )

        total_conta, gorjeta = calcular_gorjeta(conta, porcentagem_gorjeta)

        print(f"Valor da gorjeta: R$ {gorjeta:.2f}")
        print(f"Valor total com gorjeta R$ {total_conta:.2f}")
    except ValueError:
        print("Erro: Digite somente números")


if __name__ == "__main__":  # pragma: no cover
    main()

# Calculando a gorjeta em um restaurante

# João trabalha como garçom em um restaurante e precisa calcular a gorjeta que os clientes deixam ao pagar a conta. O restaurante sugere uma gorjeta de 10%, mas alguns clientes podem escolher dar mais ou menos.

# Para agilizar o processo, João quer um programa que receba o valor total da conta e a porcentagem de gorjeta desejada e exiba o valor final que o cliente deverá pagar.

# Crie um programa que peça ao usuário o valor da conta e a porcentagem de gorjeta. O programa deve calcular e exibir o valor da gorjeta e o total a ser pago.

# Exemplo de entrada:

# Digite o valor da conta: 120.00
# Digite a porcentagem de gorjeta: 10

# Saída esperada:

# Valor da gorjeta: R$ 12.00
# Total a pagar: R$ 132.00
