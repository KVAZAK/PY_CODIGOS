'''Escreva   um   programa   que   leia   um   peso   na   Terra   e   o   número   de   um   planeta   e
imprima   o   valor   correspondente   do   peso   neste   planeta.   A   relação   de   planetas   é
dada   a   seguir   juntamente   com   o   valor   das   gravidades   relativas   à   Terra.    
calcular o peso no planeta use a fórmula:'''

print('''
Digite um peso aqui do nosso planeta e veja o equilante nos plantes..

A formula para os calculos sera essa: PP=PT/10*G''')

pt=float(input("Digite o peso: "))

print(f'''Em qual planeta voce quer saber quanto vale {pt} 
''')
planeta=int(input('''
1- MERCURIO
2- VENUS 
3- MARTE 
4- JUPITER 
5- SATURNO 
6- URANO 
Digite o numero do planeta: '''))

if planeta == 1:
    pp=(pt/10)*0.37
    print(f"o peso equivalente em MERCURIO é: {pp:.3f}")

elif planeta == 2:
    pp=(pt/10)*0.88
    print(f"o peso equivalente em VENUS é: {pp:.3f}")

elif planeta == 3:
    pp=(pt/10)*0.38
    print(f"o peso equivalente em MARTE é: {pp:.3f}")

elif planeta == 4:
    pp=(pt/10)*2.64
    print(f"o peso equivalente em JUPITER é: {pp:.3f}")

elif planeta == 5:
    pp=(pt/10)*1.15
    print(f"o peso equivalente em SATURNO é: {pp:.3f}")

elif planeta == 6:
    pp=(pt/10)*1.17
    print(f"o peso equivalente em URANO é: {pp:.3f}")

else: 
    print("DIGITE APENAS NUMEROS CORRESPONDENTE A ALGUM PLANETA")
