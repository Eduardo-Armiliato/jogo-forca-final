

    

def valida_chutes(palavra):
    senha = ''
    acertos = []
    chute = ''
    letras = []
    index_letras = 0 
    verifica_acertos = 0
    erros = 0
    percorre_palavra = ''
    encontrou_letras = False
    # continua_jogo = False
    dica = input('de uma dica: ')
    print(f'a dica é {dica} agora tente descobrir qual é a palavra, então digite uma letra: ')

    for percorre_palavra in palavra:
        letras.append(percorre_palavra)
        acertos.append('N')
    while True:
        chute = input('digite a letra: ')
        index_letras = 0
        encontrou_letras = False 
        for l in letras:
            if l == chute:
                acertos[index_letras] = 'S'
                encontrou_letras = True
            index_letras += 1        
        if not encontrou_letras:
            erros +=1

        index_letras = 0 

        senha = ''
        for i in acertos:
            if i == 'S':
                senha += letras[index_letras] + ' '
            else:
                senha += ' _ ' 

            index_letras += 1      

        verifica_acertos = 0
        for i in acertos:
            if i == 'S':
                verifica_acertos += 1
            else:
                verifica_acertos -= 1 

        jogo_forca(erros, senha, dica)

        if ((verifica_acertos == len(acertos)) or (erros == 6)):
            break

def tentar_denovo():        
    continua_jogo = input('Deseja continuar jogando? S/N')
    
    if continua_jogo == 'S' or continua_jogo == 's':
        return False
    elif continua_jogo == 'N' or continua_jogo == 'n':
        return  True
    else:
        print('não entendi oque quis diser, irei para o sistema.')
        return True  
                      

def jogo_forca(erros, senha, dica):
    if erros == 0:
        print(f'''
                    
        --------|-      {dica}  
        |          
        |
        |
        |
        |
        =============
        {senha}
        ''')
    elif erros == 1:
        print(f'''
                    
        --------|-      {dica}
        |       0   
        |
        |
        |
        |
        =============
        {senha}
        ''')
    elif erros == 2:
        print(f'''
                    
        --------|-      {dica}
        |       0    
        |       |
        |
        |
        |
        =============
        {senha}
        ''')
    elif erros == 3:
        print(f'''
                    
        --------|-      {dica}
        |       0    
        |       |\\
        |
        |
        |
        =============
        {senha}
        ''')
    elif erros == 4:
        print(f'''
                    
        --------|-      {dica}
        |       0   
        |      /|\\
        |
        |
        |
        =============
        {senha}
        ''')
    elif erros == 5:
        print(f'''
                    
        --------|-      {dica}
        |       0  
        |      /|\\
        |      /
        |
        |
        =============
        {senha}
        ''')
    else:
        print(f'''
                    
        --------|-      {dica}
        |       0   
        |      /|\\
        |      / \\
        |
        |
        =============
          VOCÊ PERDEU 
        ''')


