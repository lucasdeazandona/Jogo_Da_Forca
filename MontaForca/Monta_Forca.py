def MontarForca(Erros = 0, Letras_Encontradas = [], Desafiado = [], chute = []):
    Encontradas = ''
    Percorre_L_P = ''
    Lista_Chutes = ', '
    Indice_Letra = 0

    for Percorre_L_P in Desafiado:
        if Letras_Encontradas[Indice_Letra] == 'S':
            Encontradas = Encontradas + ' ' + Percorre_L_P
        else:
            Encontradas = Encontradas + ' ' + '_'
        
        Indice_Letra += 1
    
    if Erros == 0:
        print(f'''
.........|     Letras informadas: {Lista_Chutes.join(chute) if len(chute) >= 1 else ''}
|      
|     
|     
|
|
|{Encontradas}''')
    elif Erros == 1:
        print(f'''
.........|     Letras informadas: {Lista_Chutes.join(chute) if len(chute) >= 1 else ''}
|        O      
|     
|     
|
|
|{Encontradas}''')
    elif Erros == 2:
        print(f'''
.........|     Letras informadas: {Lista_Chutes.join(chute) if len(chute) >= 1 else ''}
|       O     
|       |     
|     
|
|
|{Encontradas}''')
    elif Erros == 3:
        print(f'''
.........|     Letras informadas: {Lista_Chutes.join(chute) if len(chute) >= 1 else ''}
|        O     
|       /|     
|     
|
|
|{Encontradas}''')
    elif Erros == 4:
        print(f'''
.........|     Letras informadas: {Lista_Chutes.join(chute) if len(chute) >= 1 else ''}
|        O     
|       /|\\     
|     
|
|
|{Encontradas}''')
    elif Erros == 5:
        print(f'''
.........|     Letras informadas: {Lista_Chutes.join(chute) if len(chute) >= 1 else ''}
|        O     
|       /|\\     
|       /
|
|
|{Encontradas}''')
    elif Erros == 6:
        print(f'''
.........|     Letras informadas: {Lista_Chutes.join(chute) if len(chute) >= 1 else ''}
|        O     
|       /|\\     
|       / \\
|
|
|{Encontradas}''')
