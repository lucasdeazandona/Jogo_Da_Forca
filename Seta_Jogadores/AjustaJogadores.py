def GetJogadores():
    Desafiador = 0
    Desafiado = 0

    while True:
        try:
            Desafiador = int(input('Quem ira começar 1 ou 2?.\n'))
            
            if Desafiador == 1:
                Desafiado = 2
                break
            elif Desafiador == 2:
                Desafiado = 1
                break
            else:
                print('Apenas os jogadores 1 e 2 estão disponíveis!')
        except ValueError:
                print('Apenas números inteiros.')

                print('O Jogador {Desafiador} começa escolhendo a palavra e o jogador {Desafiado} vai tentar acertala!')

    return int(Desafiador), int(Desafiado)
