def Valida_Palavra_Desafiador(vDesafiado):
    verPalavra = ''
    vMsg = ''
    while True:
        print('Ao digitar uma palavra composta, irá ser subtituído o ESPAÇO por HÍFEN')
        verPalavra = input(f'Escolha a palavra que deseja que o jogador {vDesafiado} advinhe.\n')
        if len(verPalavra) <= 1:
            print(f'A palavra deve conter mais que "UMA" letra')
        else:
            verPalavra = Ajusta_Palavra_Composta(verPalavra)
            if Validate_Palavra(verPalavra, 'S'):
                break
    return verPalavra

def Validate_Palavra(Palavra = str, Mostra_Msg = 'N', Valida_Hifen = 'N'):
    condicao = '()*&¨%$#@!¹²³£¢¬:><.,^~][´`_=+/?|\ }{ùúàáãõóòìíçÙÚÀÁÃÕÓÒÌÍÇ123456789' if Valida_Hifen == 'N' else '()*&¨%$#@!¹²³£¢¬:><.,^~][´`_=+/?|\ }{ùúàáãõóòìíçÙÚÀÁÃÕÓÒÌÍÇ123456789-'

    if Palavra in condicao:
        if Mostra_Msg == 'S':
            if Valida_Hifen == 'N':
                print('Por favor informe apenas letras! Único caracter além das letras que é permitido é o HÍFEN', 'S')
            else:
                print('Por favor informe apenas letras!', 'S')
        return False
    else:
        return True

def Ajusta_Palavra_Composta(Palavra):
    verPalavra = ''
    verPalavra = Palavra
    return verPalavra.replace(' ', '-')