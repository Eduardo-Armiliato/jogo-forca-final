
def pergunta_nome_jogadores():
    while True:
        jogador1=input('informe o nome do jogador 1: ')
        jogador2=input('informe o nome do jogador 2: ')
        return jogador1, jogador2


def pergunta_jogador_desafiador():
    while True:
        jogador_desafiador=input('quem é o jogador que vai criar a palavra? jogador1 ou jogador2 ')
        
        if jogador_desafiador=='jogador1' or jogador_desafiador=='1':
            return 1 
            
        elif jogador_desafiador=='jogador2' or jogador_desafiador=='2':
            return 2
        else:
            print('aceitamos apenas os valores: jogador1 ou 1, jogador2 ou 2')


def cria_palavra(jogador1, jogador2, jogador_desafiador):
    if jogador_desafiador == 2:
        print(f'o {jogador2} cria a palavra e o {jogador1} responde')
    elif jogador_desafiador == 1:
        print(f'o {jogador1} cria a palavra e o {jogador2} responde')

def pergunta (jogador1, jogador2, jogador_desafiador):
    if jogador_desafiador == 1:
        palavra = input(f'{jogador1} digite a palavra em segredo: ')
        desafiado = jogador2
        return palavra
    else:
        palavra = input(f'{jogador2} digite a palavra em segredo: ')
        desafiado = jogador1
