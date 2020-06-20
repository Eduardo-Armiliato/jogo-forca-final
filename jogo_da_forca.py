from arquivos.telas import entrada_de_dados, saida_de_dados, tentativa

termina_jogo = False

saida_de_dados.msg_boas_vindas()
saida_de_dados.regras()

while not termina_jogo:
    jogador1, jogador2 = entrada_de_dados.pergunta_nome_jogadores()
    jogador_desafiador = entrada_de_dados.pergunta_jogador_desafiador()

    entrada_de_dados.cria_palavra(jogador1, jogador2, jogador_desafiador)
    palavra = entrada_de_dados.pergunta(jogador1, jogador2, jogador_desafiador)
    tentativa.valida_chutes(palavra)
    termina_jogo = tentativa.tentar_denovo()

   