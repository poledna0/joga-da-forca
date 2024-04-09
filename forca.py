PalavraParaSerAdivinhada = input('Digite a palavra: ')
NumeroDeTentativas = int(input('Digite o número máximo de tentativas: '))
FraseNaLista = []
Ganhou = False
print('\033c', end='')
TenatavivasUsadas = 0 

while True:

    if PalavraParaSerAdivinhada in FraseNaLista:
                print("A string", PalavraParaSerAdivinhada, "está presente na lista.")
                break
    
    for Letras in PalavraParaSerAdivinhada:
        encontrado = False

        for letra in FraseNaLista:
            if Letras.lower() == letra:
                encontrado = True
                break

        if encontrado:
            print(Letras.lower(), end=' ')
            
        else:
            print('_', end=' ')

    print(f'\nVocê tem {NumeroDeTentativas} tentativas')
    ChuteDaLetra = input('Digite o número máximo de tentativas:  ')
    
    for Letra in PalavraParaSerAdivinhada:
        if Letra == ChuteDaLetra:
            FraseNaLista.append(ChuteDaLetra)

    # if Letra != ChuteDaLetra:
    NumeroDeTentativas -= 1
    TenatavivasUsadas += 1
            
            
    if NumeroDeTentativas == 0:
        print(f' Que pena. A palavra era {PalavraParaSerAdivinhada}')
        break
         
    PalavraCerta = True

    for LetraPalavra in PalavraParaSerAdivinhada.lower():
        LetraAchada = False
        for LetraAdivinhada in FraseNaLista:
            if LetraPalavra == LetraAdivinhada:
                LetraAchada = True
                break
        if LetraAchada == False:  
            PalavraCerta = False
            break

    if PalavraCerta == True:  
        print(f'Parabéns, você ganhou em {TenatavivasUsadas} tentativas')
        Ganhou = True
        break