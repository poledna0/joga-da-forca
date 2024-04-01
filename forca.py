
PalavraParaAdivinhar = input('Digite a palavra para ser adivinhada: ')
ChancesParaAcertar = int(input('Digite a quantidade de vezes que pode errar: '))

# para limpar o teminal
print('\033c', end='') 

LetrasLista = []
Ganhou = False

while True:
    for Letras in PalavraParaAdivinhar:
        if Letras in LetrasLista:
            print(Letras.lower(), end=' ')
        else:
            print('_', end=' ')

    ChuteDeLetra = input('Escolha uma letra para tentar completar a palavra: ')
    LetrasLista.append(ChuteDeLetra.lower())
    print(f'Você tem mais {ChancesParaAcertar} chances')

    if ChuteDeLetra.lower() not in PalavraParaAdivinhar.lower():
        ChancesParaAcertar -= 1 

    if set(PalavraParaAdivinhar.lower()) == set(LetrasLista):  #perguntar para o prof
        Ganhou = True
        break

    if ChancesParaAcertar == 0:
        break

if Ganhou:
    print(f'Parabéns, você ganhou o jogo! A palavra era "{PalavraParaAdivinhar}".') 
else:
    print(f'Você perdeu o jogo! A palavra era "{PalavraParaAdivinhar}".')