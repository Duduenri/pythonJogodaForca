#  Criar, apresentar e explicar o código (de 5 a 10 min de apresentação) de um jogo, 
# como, por exemplo: “Batalha Naval”, “Campo Minado”, “Jogo da Forca” ou algum 
# outro de escolha do aluno. 
#  Não vale “Jogo da Velha”
#   Não vale copiar um código da Web e apresentar
#   O programa deve manipular as estruturas de dados utilizadas trabalhadas na disciplina, 
# como listas, matrizes ou dicionários para representar o jogo. As regras / pontuações, o 
# aluno pode definir.
#   No início do jogo, ler nome do usuário. No final, salvar a pontuação (com o nome) em 
# arquivo texto. Permitir a exibição do ranking dos jogadores


#menu vai ter: 1. Jogar - 2. Incluir Palavras 3. Excluir Palavras

#import os
import random
import time


nome = input("Nome do Jogador:  ")

hora_inicial = time.time()

def carregasPalavras():
    palavras = []
    with open("palavras.txt", 'r') as palavra: # 'r' é um metodo, (read). ele vai ser aberto apenas para leitura
          palavras = [linha.strip() for linha in palavra.readlines()] # strip() = função. remove espaços em brancos no INICIO OU FIM de cada palavra 
    return palavras                                                   # readlines() retorna em formato de string o que esta no arquivo

def incluirPalavras():
     with open('palavras.txt', 'a') as arquivodePalavras: # o 'a' faz a função do append(adicionar). quando um arquivo em 'a' ele adiciona no final sem alterar nada
        nova_palavra = input("Qual nova palavra deseja incluir?: ").strip()
        arquivodePalavras.write(nova_palavra + '\n') #método .write escreve string em um arquivo
     print("Palavra adicionada com sucesso!")
     

def escolhePalavra(palavras):
    return random.choice(palavras)


def excluirPalavra():
    palavras = carregasPalavras()
    palavraExcluida = input("Qual palavra deseja excluir?" )
    if palavraExcluida in palavras:
        palavras.remove(palavraExcluida)
        with open('palavras.txt', 'w') as arquivodePalavras: # o argumento 'w' de write, ele cria e sobreescre arquivos
            for palavra in palavras: #agora ele vai atualizar a lista, sem a palavra excluida
                arquivodePalavras.write(palavra + '\n')
        print("Palavra excluida com sucesso!")

def jogar():
    palavras = carregasPalavras()
    palavra_escolhida = escolhePalavra(palavras)
    ocultando_Palavra = ["_"] * len(palavra_escolhida) #length = tamanho da palavra
    tentativas = 7
    letras_tentadas = set() #set é uma coleção não ordenada de elementos
    pontos = 0


    while tentativas > 0:
        print(" ".join(ocultando_Palavra)) #ele concatena os elementos de uma strinda, vai ser ______ ao inves de '_', '_','_'
        letra = input("Qual letra deseja tentar? ").strip().lower() # strip() = função. remove espaços em brancos no INICIO OU FIM de cada palavra 

        if len(letra) != 1: #verifica se o tamanho da letra é diferente de uma caracterere só
            print("Por favor, digite apenas uma letra.")
            continue

        ## não deixar repetir letra, isso tem q vir primeiro para verificar se a letra não esta no letras tentadas
        if letra in letras_tentadas:
            pontos -= 3
            print("Você já tentou essa letra")
            continue

        letras_tentadas.add(letra) 

        if letra in palavra_escolhida:
            pontos += 10 #10 pontos se 
            for i in range(len(palavra_escolhida)): #pela a letra e percorre a palavra escolhida
                if palavra_escolhida[i] == letra: #verifica se letra digitada pe igual a letra correspondendo na palavra escolhida
                    ocultando_Palavra[i] = letra #A linha ocultando_Palavra[i] = letra serve para atualizar a lista ocultando_Palavra com a letra correta na posição i.

        else: 
            pontos -= 5
            print("Letra não encontrada")
            tentativas -= 1 #-= é subtração no local (subtração in-place) ele diminui a variavel e retorna com a resposta
            #tentativas = tentativas - 1 (seria a mesma coisa)
            print(f"Tentativas restantes: {tentativas}")

        if "_" not in ocultando_Palavra:
            print("Parabéns voce completou a tarefa")
            pontos += 100 #é outra forma de usar o operador de atribuição in-place
            #pontos = pontos + 1
            break

        if tentativas == 0:
            print(f"Game Over! A palavra era {palavra_escolhida} e sua pontuação foi {pontos}")



#palavra_escolhida = escolhePalavra(palavras)
#print(f"A palavra escolhida é: {palavra_escolhida}")
#excluirPalavra()


def menu():
    while True:
        print("\nMenu:")
        print("1. Jogar")
        print("2. Incluir Palavra")
        print("3. Excluir Palavra")
        print("4. Sair")
        selecao = input("Escolha sua opção: ").strip()

        if selecao == '1':
            jogar()         
        elif selecao == "2":
            incluirPalavras()
        elif selecao == "3":
            excluirPalavra()
        elif selecao == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida")

palavras = carregasPalavras()

menu()