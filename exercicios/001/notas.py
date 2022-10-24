print("DIGITE O VALOR QUE DESEJA SACAR. RESPEITE OS LIMITES DO BANCO")
print("valor minimo para sacar [20,00R$]")
print("valor maximo para sacar [500,00R$]")
print("")

numero= int(input("digite um valor para sacar(50-500): "))

cem = numero // 100
numero = numero % 100

cinquenta = numero // 50
numero = numero % 50

vinte = numero // 20
numero = numero % 10

cinco = numero // 5
numero = numero % 5

um = numero

print(f"Notas de 100,00R$ {cem}, notas de 50,00R$ {cinquenta}, notas de 10,00R$ {vinte}, notas de 5,00R$ {cinco}, notas de 1,00R$ {um}")
print("")
print("notas de 100", cem)
print("notas de 50", cinquenta)
print("notas de 20", vinte)
print("notas de 5", cinco)