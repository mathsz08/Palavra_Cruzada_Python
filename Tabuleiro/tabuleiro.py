from Palavras import dicionario as dc
from random import randint
from time import sleep


class tabuleiro:
    def __init__(self,dicionario):
        """
            Init da classe responsavel por colocar as palavras em Tabuleiro, constituido por uma matriz [30][30]

        :param dicionario:Palavra
        """
        self.tabuleiro = list() # tabuleiro gabarito
        self.tabuleiroJog = list()# tabuleiro para o usuario
        self.dicionario = dicionario # lista de palavras interligadas para o tabuleiro
        self.palnum =1
        self.posPals = dict()

    def tabuleiro(self,dicionario):
        """
            Instanciador da Classe Tabuleiro, responsavel por criar uma matriz com as Palavras geradas
        :param dicionario:
        :return: None
        """
        self.tabuleiro = list() # tabuleiro gabarito
        self.tabuleiroJog = list() # tabuleiro para o usuario
        self.dicionario = dicionario # lista de palavras interligadas para o tabuleiro

    def getDicionario(self):
        """
            Retorna o Dicionario
        :return: Dicionario
        """
        return self.dicionario

    def getTab(self):
        """
            Retorna o tabuleiro gabarito
        :return: None
        """
        for i in self.tabuleiro:
            for j in i:
                if j != 0:
                    print(f"|{j[0]}|", end=" ")
                else:
                    print("   ", end=" ")
            print(" ")

    def getTabJog(self):
        """
            Retorna o tabuleiro do jogador
        :return: None
        """
        for i in self.tabuleiroJog:
            for j in i:
                if j != 0:
                    if type(j) is int:
                        print(f' {j} ',end=' ')
                    else:
                        print(f"|{j[0]}|", end=" ")
                else:
                    print("   ", end=" ")
            print(" ")


    def criarTab(self):
        """
        Cria o esqueleto dos tabuleiros, uma matriz[30][30]
        :return: None
        """
        for i in range(30): # percorre uma distancia de 30 unidades
            aux = [] # array auxiliar para o tabuleiro gabarito
            aux2 = [] # array auxiliar para o tabuleiro do Jogador
            for j in range(30): # percorre novamente uma distancia de 30 unidades
                aux.append(0) # preenche o array com 0's a cada unidade percorrida
                aux2.append((0))# preenche o array com 0's a cada unidade percorrida
            self.tabuleiro.append(aux) # conecta o array com 0's no tabuleiro gabarito
            self.tabuleiroJog.append(aux2) # conecta o array com 0's no tabuleiro do jogador


    def colocarPalavras(self,palavra):
        """
        Função responsavel por começar o preenchimento dos tabuleiros, através de outras duas funções recursivas
        :param palavra: Palabvra
        :return: None
        """
        self.colocarVertical(palavra,len(self.tabuleiro[5]) - 20) # Chama a função para colocar a primeira palavra na vertical

    def colocarHorizontal(self,palavra,pos,posant = None):
        """
            Coloca Palavras, na direção horizonta(linhas), do tabuleiro recebendo como parametro a propria
            palavra, a posição na qual ela começará e informações da palavra anterior caso necessarío
        :param palavra: Palavra
        :param pos: Int
        :param posant: Tuple(str(),int(),int())
        :return: None
        """

        cn = 0 # Inicia uma variavel para receber o index da letra conectada
        for index,l in enumerate(palavra.getLetras()): # Intera entre as letras da palavra passada por parametro
            if l[0].upper() == posant[0].upper(): # Caso a letra seja igual a letra conectada
                cn = index # guarda o index da letra igual
                break # encerra o loop
        for index, letra in enumerate(palavra.getLetras()): # para cada letra da palavra
            if index == 0:
                self.posPals.update({self.palnum:((posant[2],index+posant[1]),0)})
                self.tabuleiroJog[posant[2]][(index+posant[1])-cn-1] = self.palnum
            self.tabuleiro[posant[2]][(index+posant[1])-cn] = letra # posiciona a letra no tabuleiro gabarito
            if randint(0,10) % 2 == 0: # pequeno filtro para escolher quais letras não colocar
                self.tabuleiroJog[posant[2]][(index + posant[1]) - cn] = letra # posiciona a letra no tabuleiro do Jogador
            else:
                self.tabuleiroJog[posant[2]][(index + posant[1]) - cn] = ' '  # posiciona espaço vazio no tabuleiro do Jogador
            if letra[1]: #caso a letra esteja interligada em alguma palavra
                self.palnum += 1
                self.colocarVertical(letra[2],index,(letra[0],pos,(index+posant[1])-cn)) # chama a função para a palavra interligada

    def colocarVertical(self,palavra,pos,posant = None):
        """
         Colocar palavras, na direção vertical(colunas), do tabuleiro recebendo coo parametro a palavra a ser colocada,
         a posição na qual será colocada e informações da palavra interior caso necessario
        :param palavra:
        :param pos:
        :param posant:
        :return:
        """
        cn =0 # Inicia uma variavel para receber o index da letra conectada
        if posant is not None: # Se não for a primeira palavra conectada
            for index, l in enumerate(palavra.getLetras()): # Intera entre as letras da palavra passada por parametro
                if l[0].upper() == posant[0].upper():# Caso a letra seja igual a letra conectada
                    cn= index # guarda o index da letra igual
                    break# encerra o loop
            for index, letra in enumerate(palavra.getLetras()):# para cada letra da palavra
                if index == 0:
                    self.tabuleiroJog[(index + 4 + posant[1])-cn][posant[2]] = self.palnum
                    self.posPals.update({self.palnum:(((index + 5 + posant[1])-cn,posant[2]),1)})
                self.tabuleiro[(index + 5 + posant[1])-cn][posant[2]] = letra # posiciona a letra no tabuleiro gabarito
                if randint(0, 10) % 2 == 0:# pequeno filtro para escolher quais letras não colocar
                    self.tabuleiroJog[(index + 5 + posant[1]) - cn][posant[2]] = letra  # posiciona a letra no tabuleiro do Jogador
                else:
                    self.tabuleiroJog[(index + 5 + posant[1]) - cn][posant[2]] = ' '  # posiciona espaço vazio no tabuleiro do Jogador
                if letra[1]:#caso a letra esteja interligada em alguma palavra
                    self.palnum =+ 1
                    self.colocarHorizontal(letra[2],index,(letra[0],pos,(index + 5 + posant[1])-cn))# chama a função para a palavra interligada
        else: # se for a primeira palavra
            for index, letra in enumerate(palavra.getLetras()):# para cada letra da palavra
                if index == 0:
                    self.posPals.update({self.palnum: ((index+5,pos), 1)})
                    self.tabuleiroJog[index + 4][pos] = self.palnum
                self.tabuleiro[index+5][pos] = letra # posiciona a letra no tabuleiro gabarito
                if randint(0, 10)  % 2 == 0:# pequeno filtro para escolher quais letras não colocar
                    self.tabuleiroJog[index + 5][pos] = letra  # posiciona espaço vazio no tabuleiro do Jogador
                else:
                    self.tabuleiroJog[index + 5][pos] = ' '  # posiciona a letra no tabuleiro do Jogador
                if letra[1]:#caso a letra esteja interligada em alguma palavra
                    self.palnum += 1
                    self.colocarHorizontal(letra[2], index, (letra[0], pos,index+5))# chama a função para a palavra interligada

