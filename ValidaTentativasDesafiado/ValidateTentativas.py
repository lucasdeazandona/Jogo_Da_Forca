from ValidaPalavra import ValidacaoPalavras
from MontaForca import Monta_Forca

def Validate_Tentativas_Desafiado(PalavraDesafiador):
    PalavraDesafiador = PalavraDesafiador.upper()
    Letras_de_tentativa = ''
    L_P = ''
    Percorre_L_P_Desafiador = ''
    Percorre_L_P_Desafiado = ''
    Lista_Chutes = ', '
    FimJogo = ''

    Desafiado_Pontuacao = 0
    Pontuacao_Desafiador = 0
    N_Tentativas = 0
    Percorre_Palavra = 0
    Indice_Letra = 0

    Lista_Palavra_Desafiador = []
    Lista_Letra_Encontrada = []
    Ver_Lista_Chutes = []
    Desagrupa_Palavra_Desafiado = []

    Letra_Enc = False
    Proxima_Jo = False

    while Percorre_Palavra < len(PalavraDesafiador):
        Lista_Palavra_Desafiador.append(PalavraDesafiador[Percorre_Palavra])
        if PalavraDesafiador[Percorre_Palavra] == '-':
            Lista_Letra_Encontrada.append('S')
        else:
            Lista_Letra_Encontrada.append('N')
        Percorre_Palavra += 1

    while True:
        Letras_de_tentativa = ''
        Proxima_Jo = False
        N_Tentativas += 1

        if N_Tentativas > 1:
            if Letra_Enc:
                print('Acertou! Parabéns!')
            else:
                print('Poxa, você errou!')
                Pontuacao_Desafiador += 1

        if Verifica_Achou_Todas_Letras(Lista_Letra_Encontrada):
            Desafiado_Pontuacao = 6

        if Desafiado_Pontuacao == 6 or Pontuacao_Desafiador == 6:
            if Desafiado_Pontuacao == 6:
                print('Parabéns desafiado, você venceu o jogo!')
            else:
                print('Parabéns desafiador, você venceu o jogo!')
                print(f'A palavra escolhida pelo Desafiador foi: {PalavraDesafiador}' )

            while True:
                try:
                    FimJogo = input('Você deseja jogar novamente? ')
                    FimJogo = FimJogo.upper()

                    if FimJogo == 'N':
                        return True
                    elif FimJogo == 'S':
                        return False
                    else:
                        print('Apenas S ou N são aceitos como resposta!')
                except:
                    print('Erro:' + Exception)

        Monta_Forca.MontarForca(Pontuacao_Desafiador, Lista_Letra_Encontrada, Lista_Palavra_Desafiador, Ver_Lista_Chutes)

        Letra_Enc = False
        while not (Proxima_Jo):
            if N_Tentativas == 1:
                print('Atenção, na primeira rodada apenas letras podem ser escolhidas')
                L_P = 'L'
            else:
                print('Caso deseje chutar uma Palavra, só poderá realizar uma tentativa de acerto,\n'
                      'caso erre, perde o jogo, caso acerte, ganha o jogo.')
                L_P = str(input('Deseja informar uma letra ou uma palavra? Digite L para informar uma letra ou P para palavra\n'))

            L_P = L_P.upper()
            L_P = L_P.strip()

            if L_P == '':
                print('Informe ao menos uma letra!')
            elif not(L_P) in 'LP':
                print('Apenas as Letras L e P são permitidas!')
            else:
                if ((L_P == 'L') or (N_Tentativas == 1)):
                    print("Digite uma letra que você acha que está na palavra escolhida pelo desafiador!\n")
                    Letras_de_tentativa = input()
                    Letras_de_tentativa = Letras_de_tentativa.upper()
                    Letras_de_tentativa = Letras_de_tentativa.strip()

                    if Letras_de_tentativa == '':
                        print('Informe ao menos uma letra!')
                        Proxima_Jo = False
                    if len(Letras_de_tentativa) > 1:
                        print('Digite apenas uma letra!')
                        Proxima_Jo = False
                    elif ValidacaoPalavras.Validate_Palavra(Letras_de_tentativa, 'S', 'S'):
                        Percorre_L_P_Desafiador = ''

                        if Letras_de_tentativa in Ver_Lista_Chutes:
                            print('A letra já foi utilizada anteriormente!')
                            Proxima_Jo = False
                            break

                        Ver_Lista_Chutes.append(Letras_de_tentativa)

                        Indice_Letra = 0
                        for Percorre_L_P_Desafiador in Lista_Palavra_Desafiador:
                            if Letras_de_tentativa == Percorre_L_P_Desafiador:
                                Lista_Letra_Encontrada[Indice_Letra] = 'S'
                                Proxima_Jo = True
                                Letra_Enc = True
                            else:
                                Proxima_Jo = True

                            Indice_Letra +=1

                elif ((L_P == 'P') and (N_Tentativas > 0)):
                    Letras_de_tentativa = input(print("Digite uma palavra que você acha que é a palavra escolhida pelo desafiador!\n"))
                    Letras_de_tentativa = Letras_de_tentativa.upper()
                    Letras_de_tentativa = Letras_de_tentativa.strip()

                    if Letras_de_tentativa == '':
                        print('Informe ao menos duas letras!','S')
                        Proxima_Jo = False
                    if len(Letras_de_tentativa) == 1:
                        print('Informe mais que uma letra','S')
                        Proxima_Jo = False
                    elif ValidacaoPalavras.Validate_Palavra(Letras_de_tentativa, 'S', 'S'):
                        Percorre_L_P_Desafiador = ''
                        Percorre_L_P_Desafiado = ''
                        Indice_Letra = 0

                        Letras_de_tentativa = ValidacaoPalavras.Ajusta_Palavra_Composta(Letras_de_tentativa)
                        for Percorre_L_P_Desafiado in Letras_de_tentativa:
                            Desagrupa_Palavra_Desafiado.append(Percorre_L_P_Desafiado)

                        for Percorre_L_P_Desafiador in Lista_Palavra_Desafiador:
                            if Lista_Palavra_Desafiador[Indice_Letra] != Desagrupa_Palavra_Desafiado[Indice_Letra]:
                                Pontuacao_Desafiador = 5
                                Proxima_Jo = True
                                Letra_Enc = False
                                break
                            else:
                                Desafiado_Pontuacao = 5
                                Letra_Enc = True
                                Proxima_Jo = True
                                Lista_Letra_Encontrada[Indice_Letra] = 'S'
                            Indice_Letra += 1

def Verifica_Achou_Todas_Letras(Letras_Encontradas):
    Indice_Letra = 0
    vVeririficaLetras = ''

    for vVeririficaLetras in Letras_Encontradas:
        if vVeririficaLetras == 'S':
            Indice_Letra +=1
        else:
            Indice_Letra -=1

    if Indice_Letra == len(Letras_Encontradas):
        return True
    else:
        return False
