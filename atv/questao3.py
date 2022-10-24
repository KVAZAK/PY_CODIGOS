"""
Faça um programa que leia "n" valores. O programa deve inicialmente solicitar aousuário que informe a 
quantidade desejada de valores a ser informada, 
depois leros "n" valores e ao final imprimir a média aritmética dos valores lidos.
"""
valores = int(input("Digita um número inteiro[0 pra terminar]: "))
soma = 0
quantidade = 1

while valores != 0:
    soma = soma + valores
    quantidade = soma / valores
    valores = int(input("Digita um número inteiro[0 pra terminar]: "))
    
    print(f"A soma foi:{quantidade:.2f}")