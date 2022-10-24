'''O banco Facimp concederá um crédito especial com juros de 2% aos seus clientes
de acordo com o saldo médio no último ano. Faça um programa que leia o saldo
médio de um cliente e calcule o valor do crédito de acordo com a tabela a seguir. O
programa   deve   imprimir   uma   mensagem   informando   o   saldo   médio   e   o   valor   de credito'''
# coding=UTF-8


print('''
O banco FACIMP vai lhe oferecer um credito de acordo com seu ultimo saldo medio.
sera cobrado apenas 2% de juros. 
''')

saldo=float(input('''vamos ver se temos saldo disponivel para voce.
DIGITE SUA ULTIMA RENDA: '''))

if saldo < 501:
    print("infelizmente nao temos ofertas disponiveis para voce.")

elif saldo >=501 and saldo <1001:
    credito=saldo*(30/100)
    print(f'''
    Parabens seu emprestimo foi aprovado, o valor disponivel
    para clientes com saldo medio de R$ {saldo}, eh de: R$ {credito}''')

elif saldo >=1001 and saldo <3001:
    credito=saldo*(40/100)
    print(f'''
    Parabens seu emprestimo foi aprovado, o valor disponivel
    para clientes com saldo medio de R$ {saldo}, eh de: R$ {credito}''')

elif saldo >=3001:
    credito=saldo*(50/100)
    print(f'''
    Parabens seu emprestimo foi aprovado, o valor disponivel
    para clientes com saldo medio de R$ {saldo}, eh de: R$ {credito}''')

elif saldo<=0:
    print("desculpe valores negativos nao sao aceitos. por favor tente novamente...")

