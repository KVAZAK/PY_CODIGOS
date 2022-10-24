


print('''

lista de cargos e porcetagem de reajuste:

1- Auxiliar de escritorio 7%
2- Secretario (a)         9%
3- Cozinheiro (a)         5%
4- Entregador (a)        12%
''')

cargo=int(input("Digite o numero do cargo que voce quer saber o novo salario: "))

if cargo== 1:
    salario=float(input("Qual o valor do salario atual do auxiliar de escritorio? "))
    reajuste=salario + (salario * 7/100)
    print(f"O valor do salario com reajuste eh: {reajuste} ")

elif cargo== 2:
    salario=float(input("Qual o valor do salario atual ? "))
    reajuste=salario + (salario * 9/100)
    print(f"O valor do salario com reajuste eh: {reajuste} ")

elif cargo== 3:
    salario=float(input("Qual o valor do salario atual do cozinheiro(a) ? "))
    reajuste=salario + (salario * 5/100)
    print(f"O valor do salario com reajuste eh: {reajuste} ")

elif cargo== 4:
    salario=float(input("Qual o valor do salario atual entregador(a) ? "))
    reajuste=salario + (salario * 12/100)
    print(f"O valor do salario com reajuste eh: {reajuste} ")

else:
    print("POR FAVOR DIGITAR APENAS NUMEROS CORRESPONDENTES AOS CARGOS! ")


    