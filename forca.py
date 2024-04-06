PalavraParaSerAdivinhada = input('Digite a palavra: ')
NumeroDeTentativas = int(input('Digite o número máximo de tentativas: '))
FraseNaLista = []
Ganhou = False
print('\033c', end='')

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
    
    ChuteDaLetra = input('Digite um caractere: ')
    
    for Letra in PalavraParaSerAdivinhada:
        if Letra == ChuteDaLetra:
            FraseNaLista.append(ChuteDaLetra)

    if Letra != ChuteDaLetra:
            NumeroDeTentativas -= 1
    print(NumeroDeTentativas)
    print(FraseNaLista)

    if NumeroDeTentativas == 0:
        print(f' você perdeu a palavra era {PalavraParaSerAdivinhada}')
        break
    if FraseNaLista == PalavraParaSerAdivinhada:
         print('Voce advinhou a palavra parabens')
         
    PalavraCompleta = True

    for LetraPalavra in PalavraParaSerAdivinhada.lower():
        LetraPresente = False
        for LetraAdivinhada in FraseNaLista:
            if LetraPalavra == LetraAdivinhada:
                LetraPresente = True
                break
        if LetraPresente == False:  
            PalavraCompleta = False
            break

    if PalavraCompleta == True:  
        print('Parabéns, você adivinhou a palavra!')
        Ganhou = True
        break