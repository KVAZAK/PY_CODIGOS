
quant = 0
pesototal = 0
pesomedio = 0
qtdvolumes = 0

caixa = input("Deseja casdastrar uma caixa? [1]-sim [2]-nao")

while caixa != 2:
    qtdvolumes+= qtdvolumes
    pesocaixa = int(input("Infome peso da caixa: "))
    pesototal += pesocaixa
    caixa = input("Deseja casdastrar uma caixa? [1]-sim [2]-nao")

    pesomedio = pesototal / qtdvolumes

    print(f"""
Quantidade de volumes:{qtdvolumes}
Peso total dos volumes:{pesototal}
Peso medio dos volumes:{pesomedio}
 """)
