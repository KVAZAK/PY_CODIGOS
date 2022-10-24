


print("compare a adicao ao numero 20, caso seja maior adicione 8, caso nao, diminua 5")

x=int(input("digite o primeiro numero: "))
y=int(input("digite o segundo numero: "))

r= x+y

if r > 20 :
    r=r+8
    print(r)
else:
    r=r-5
    print(r)