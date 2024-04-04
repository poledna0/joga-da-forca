PalavraParaAdivinhar = input('Digite a palavra para ser adivinhada: ')
ChancesParaAcertar = int(input('Digite a quantidade de vezes que pode errar: '))

# para limpar o terminal
print('\033c', end='')

LetrasLista = []
Ganhou = False

while True:
    TamanhoPalavra = len(PalavraParaAdivinhar)
    Posicao = 0

    while Posicao < TamanhoPalavra:
        letra = PalavraParaAdivinhar[Posicao]

        if letra in LetrasLista:
            print(letra.lower(), end=' ')
        else:
            print('_', end=' ')
            
        Posicao += 1

    ChuteDeLetra = input('Escolha uma letra para tentar completar a palavra: ')
    print(f'Você tem mais {ChancesParaAcertar} chances')

    if ChuteDeLetra.lower() not in PalavraParaAdivinhar.lower():
        ChancesParaAcertar -= 1
    else:
        LetrasLista.append(ChuteDeLetra.lower())

    if set(PalavraParaAdivinhar.lower()) == set(LetrasLista):
        Ganhou = True
        break

    if ChancesParaAcertar == 0:
        break

if Ganhou:
    print(f'Parabéns, você ganhou o jogo! A palavra era "{PalavraParaAdivinhar}".')
else:
    print(f'Você perdeu o jogo! A palavra era "{PalavraParaAdivinhar}".')
