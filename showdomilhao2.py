# Bibliotecas

import random
from operator import itemgetter

# Chamando os arquivos de texto para leitura e gravando numa lista

chama_perguntas = open("perguntas.txt", "r", encoding="UTF-8")
lista_perguntas = chama_perguntas.readlines()
chama_perguntas.close()

chama_respostas = open("respostas.txt", "r", encoding="UTF-8")
lista_respostas = chama_respostas.readlines()
chama_respostas.close()

respostas_corretas = open("respostas_corretas.txt", "r", encoding="UTF-8")
lista_corretas = respostas_corretas.readlines()
respostas_corretas.close()

# Tratando as valistas que contém as perguntas e as respostas, dado que na leitura do arquivo vem junto o caractere \n
# Aqui trata esse \n, o retirando da lista

for i in range(len(lista_perguntas)):
    lista_perguntas[i] = lista_perguntas[i].rstrip('\n')

for i in range(len(lista_respostas)):
    lista_respostas[i] = lista_respostas[i].rstrip('\n')

# Definindo as funções para geração de perguntas e para verificação de respostas

def aleatoria():
    result = random.sample(range(0,len(lista_perguntas)), 10)
    return result
    
def verif_resposta(x):
    global pontos
    if x == int(lista_corretas[pergunta[i]]):
        print("\033[1;32mResposta correta!\033[m")
        if pergunta[i] <= 8:
            pontos = 1
        elif pergunta[i] >= 9 and pergunta[i]<= 16:
            pontos = 3
        else:
            pontos = 5
        
    else:
        print("\033[1;31mResposta errada!\033[m")
        pontos = 0



# Chamando a função e a salvando numa variável, para toda vez que a variável for chamada, a função ser chamada novamente
# Sendo assim, gerando outros números aleatórios

pergunta = aleatoria()

# Código geral do jogo

while True:

    # Nome do jogador

    nome_jogador = str(input("Boas vindas ao Show do Milhão 2! Para começar, digite seu nome, espaços em brancos não são aceitos: "))
    print("")

    # Verificando nomes, qualquer nome é aceito contanto que não possua espaços em branco

    while nome_jogador.count(" ") > 0:
        print("\033[1;31mNome inválido, favor retirar os epaços em branco.\033[m")
        print("")
        nome_jogador = str(input("Insira um nome novamente:"))
        print("")

    # Introdução ao jogo
        
    print("-="*80)
    print('''O jogo contará com um sistema de dificuldade, a pontuação da pergunta será avaliada de acordo com o nível de dificuldade dela.
    Fácil = 1 ponto
    Média = 3 pontos
    Difícil = 5 pontos
A dificuldade da pergunta estará logo após sua descrição.
Pressione qualquer tecla para continuar, boa sorte!''')
    print("-="*80)
    input("") 

    # Variável de pontuação que será usada em breve, a princípio, todos os jogadores começam com 0 pontos

    pontuação = 0

    # Nesse for é tratado como as perguntas vão aparecer e sua relação com as alternativas tão quanto sua dificuldade

    for i in range(len(pergunta)):
        print("-="*80)
        print(lista_perguntas[pergunta[i]])
        if pergunta[i] == 0:
            print("Dificuldade: \033[4;34mFácil\033[m")
            for j in range(4):
                print(j+1,")",lista_respostas[j])
        else:
            if pergunta[i] >= 1 and pergunta[i] <= 8:
                print("Dificuldade: \033[4;34mFácil\033[m")
                print("")
            elif pergunta[i] >= 9 and pergunta[i] <= 16:
                print("Dificuldade: \033[4;33mMédia\033[m")
                print("")
            elif pergunta[i] >16:
                print("Dificuldade: \033[4;37mDifícil\033[m")
                print("")
            for j in range(4):
                x = pergunta[i]*4
                print(j+1,")",lista_respostas[x+j])

        # Um imput para o usuário selecionar sua resposta, tendo um valor de 1 a 4

        print("")
        alternativa = int(input("Escolha uma alternativa: "))
        print("")

        # Verificação pra deixar o usuário prosseguir apenas quando selecionar uma alternativa válida

        while (alternativa < 1 or alternativa > 4):
                print("\033[1;31mInsira uma alternativa válida\033[m")
                print("")
                alternativa = int(input("Escolha uma alternativa: "))
                print("")

        # Chama a função para verificar a resposta, passando a alternativa que foi escolhida pelo usuário

        verif_resposta(alternativa)

        # Após a função retornar o valor dos pontos atribuídos, ele é somado na variável pontuação

        pontuação += pontos

    print("-="*80)

    # Chamando o arquivo de texto para adicionar as informações dos jogadores e suas pontuações

    scoreboard = open("scoreboard.txt", "a", encoding="UTF-8")
    scoreboard.write(str(nome_jogador)+" "+str(pontuação)+"\n")
    scoreboard.close()

    # Chamando o arquivo de texto para ler esses valores que foram dados anteriormente

    scoreboard = open("scoreboard.txt", "r", encoding="UTF-8")
    scoreboard_valores = scoreboard.readlines()
    scoreboard.close()

    # Atribuindo uma lista que será usada na formação dos placares

    placar = []

    # Nesse for tratamos os valores da variável scoreboard_values, convertendo para string, e depois convertendo para lista novamente
    # Para assim podermos separar os valores de nome de usuário e pontuação
    # Exemplo:
    # Antes: ['nome de usuario pontuação']
    # Depois: ['nome de usuario', 'pontuação']

    for i in range(len(scoreboard_valores)):
        scoreboard_valores_converter = str(scoreboard_valores[i]).strip('[]')
        scoreboard_convertendo = scoreboard_valores_converter.split()
        placar.append(scoreboard_convertendo)

    # Converter os valores dos pontos de string para int, para realizar a organização decrescente

    for i in range(len(placar)):
        placar[i][1] = int(placar[i][1])

    # Agradecimentos finais, aqui o jogo já terminou, é apresentado sua pontuação e seu nome de usuário

    print("Obrigado por jogar", placar[-1][0]," sua pontuação foi de:", placar[-1][1],"!")
    print("-="*80)

    # Agora será exibido, se por assim desejar o usuário, o placar do top 10 jogadores caso já houver 10 jogadores, em ordem decrescente

    placar.sort(key=itemgetter(1), reverse=True)

    if len(placar) >= 10:
        confirmação = input("Deseja ver o top 10 dos jogadores? Digite 0 se não quiser, se quiser tecle qualquer outra coisa.")
        print("-="*80)
        if confirmação != "0":
            for i in range(10):
                print(i+1,"º) Nome do jogador: ", placar[i][0], "\nPontuação: ", placar[i][1],"\n")
            print("-="*80)
    
    # Antes do loop acontecer, é dado ao usuário a opção de fechar o jogo, ou jogar novamente

    continuar = input("Uma nova rodada irá começar, deseja continuar?\nDigite 0 se quiser sair do jogo, se não, tecle qualquer coisa.\n")
    print("-="*80)
    if continuar == "0": break

    # Com isso, gera uma nova sequencia de perguntas para serem atribuidas ao jogo

    pergunta = aleatoria()

    



        
            