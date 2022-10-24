'''Faça um programa que receba a altura e o sexo de uma pessoa, após isso calcule e imprima 
o seu peso ideal, utilizando as seguintes fórmulas:
•Para homens: (72,7 * A) - 58
•Para mulheres: (62,1 * A) - 44,7Em que: A = Altura'''

print('''vamos saber o peso ideal de uma pessoa.

voce deseja saber o peso ideal para homem ou mulher?
''')

sexo=int(input('''DIGITE O NUMERO DA OPCAO DESEJADA:
1- HOMEM
2- MULHER
'''))

if sexo == 1:
    print("voce deseja saber o peso de ideal para um homem.")
    altura=float(input("DIGITE A ALTURA DO HOMEM: "))
    peso= (72.7*altura) - 58
    print(f"o peso adequado para um homem de {altura} eh: {peso:.2f}kg")
    

elif sexo == 2:
    print("voce deseja saber o peso de ideal para uma mulher.")
    altura=float(input("DIGITE A ALTURA DA MULHER: "))
    peso= (62.1*altura) - 44.7
    print(f"o peso adequado para uma mulher de {altura} eh: {peso:.2f}kg")
    

else:
    print("POR FAVOR DIGITE APENAS 1 OU 2")

