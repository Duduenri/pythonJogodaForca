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


import os
import random
import time

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


palavras = carregasPalavras()

palavra_escolhida = escolhePalavra(palavras)
print(f"A palavra escolhida é: {palavra_escolhida}")
excluirPalavra()