'''faca um programa que de o valor da passagem de um viajante de acordo com seu desttino '''
# coding=UTF-8





destino=int(input('''SEJA BEM VINDO AO MENU DE DESTINOS DA F.H VIAGENS.

ESCOLHA O SEU DESTINO: 
1- REGIAO NORTE 
2- REGIAO NORDESTE 
3- REGIAO CENTRO-OESTE 
4- REGIAO SUL

DIGITE O NUMERO CORRESPONDENTE AO SEU DESTINO: '''))

if destino == 1: 
    ida_volta=int(input('''
    VOCE ESCOLHEU O NORTE COMO SEU DESTINO.

    VOCE DESEJA PASSAGENS DE IDA E VOLTA?
    1- SIM 
    2- NAO 
    DIGITE O NUMERO DA SUA OPCAO: '''))
    if ida_volta == 1 :
        print('''O VALOR DO SEU PACOTE DE VIAGEM PARA O NORTE FICOU: r$ 900,00 reais,
        DESFRUTE DO SEU PASSEI E OBRIGADO PELA PREFERENCIA!''')
    elif ida_volta == 2 : 
        print('''O VALOR DO SEU PACOTE DE VIAGEM PARA O NORTE FICOU DE r$ 500,00 reais,
        DESFRUTE DO SEU PASSEIO E OBRIGADO PELA PREFERENCIA!''')
    else: 
        print("POR FAVOR, RESPONDER COM 1 OU 2 ")
elif destino == 2: 
    ida_volta=int(input('''
    PARABENS, OTIMA ESCOLHA, O NORDESTE É INCRIVEL!

    VOCE DESEJA PASSAGENS DE IDA E VOLTA?
    1- SIM 
    2- NAO 
    DIGITE O NUMERO DA SUA OPCAO: '''))
    if ida_volta == 1 :
        print('''O VALOR DO SEU PACOTE DE VIAGEM PARA O NORDESTE FICOU: r$ 650,00 reais,
        DESFRUTE DO SEU PASSEI E OBRIGADO PELA PREFERENCIA!''')
    elif ida_volta == 2 : 
        print('''O VALOR DO SEU PACOTE DE VIAGEM PARA O NORDESTE FICOU DE r$ 350,00 reais,
        DESFRUTE DO SEU PASSEIO E OBRIGADO PELA PREFERENCIA!''')
    else: 
        print("POR FAVOR, RESPONDER COM 1 OU 2 ")
elif destino == 3: 
    ida_volta=int(input('''
    UAU, VOCE FEZ UMA BELA ESCOLHA EM QUERER CONHECER O CENTRO-OESTE.
    
    VOCE DESEJA PASSAGENS DE IDA E VOLTA?
    1- SIM 
    2- NAO 
    DIGITE O NUMERO DA SUA OPCAO: '''))
    if ida_volta == 1 :
        print('''O VALOR DO SEU PACOTE DE VIAGEM PARA O CENTRO-OESTE FICOU: r$ 600,00 reais,
        DESFRUTE DO SEU PASSEI E OBRIGADO PELA PREFERENCIA!''')
    elif ida_volta == 2 : 
        print('''O VALOR DO SEU PACOTE DE VIAGEM PARA O CENTRO-OESTE FICOU DE r$ 350,00 reais,
        DESFRUTE DO SEU PASSEIO E OBRIGADO PELA PREFERENCIA!''')
    else: 
        print("POR FAVOR, RESPONDER COM 1 OU 2 ")
elif destino == 4: 
    ida_volta=int(input('''
    PARABENS VOCE ESCOLHEU O SUL COMO DESTINO. 

    VOCE DESEJA PASSAGENS DE IDA E VOLTA?
    1- SIM 
    2- NAO 
    DIGITE O NUMERO DA SUA OPCAO: '''))
    if ida_volta == 1 :
        print('''O VALOR DO SEU PACOTE DE VIAGEM PARA O SUL FICOU: r$ 550,00 reais,
        DESFRUTE DO SEU PASSEI E OBRIGADO PELA PREFERENCIA!''')
    elif ida_volta == 2 : 
        print('''O VALOR DO SEU PACOTE DE VIAGEM PARA O SUL FICOU DE r$ 300,00 reais,
        DESFRUTE DO SEU PASSEIO E OBRIGADO PELA PREFERENCIA!''')
    else: 
        print("POR FAVOR, RESPONDER COM 1 OU 2 ")
else:
    print("NAO RECONHECEMOS SUA ESCOLHA,POR FAVOR TENTAR NOVAMENTE.")

