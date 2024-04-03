PalavraParaAdivinhar = input('Digite a palavra para ser adivinhada: ')
ChancesParaAcertar = int(input('Digite a quantidade de vezes que pode errar: '))

# para limpar o terminal
print('\033c', end='')

LetrasLista = []
Ganhou = False

while True:
    for Letra in PalavraParaAdivinhar:
        LetraEncontrada = False
        for LetraEscolhida in LetrasLista:
            if LetraEscolhida.lower() == Letra.lower():
                LetraEncontrada = True
                break

        if LetraEncontrada:
            print(Letra, end=' ')
        else:
            print('_', end=' ')

    ChuteDeLetra = input('Escolha uma letra para tentar completar a palavra: ').lower()
    print(f'Você tem mais {ChancesParaAcertar} chances')

    LetrasLista.append(ChuteDeLetra)

    Ganhou = True
    for letra in PalavraParaAdivinhar:
        LetraEncontrada = False
        for LetraEscolhida in LetrasLista:
            if LetraEscolhida.lower() == letra.lower():
                LetraEncontrada = True
                break
        if not LetraEncontrada:
            Ganhou = False
            break

    if Ganhou:
        break

    if ChancesParaAcertar == 0:
        break

    if ChuteDeLetra not in PalavraParaAdivinhar.lower():
        ChancesParaAcertar -= 1

if Ganhou:
    print(f'Parabéns, você ganhou o jogo! A palavra era "{PalavraParaAdivinhar}".')
else:
    print(f'Você perdeu o jogo! A palavra era "{PalavraParaAdivinhar}".')
