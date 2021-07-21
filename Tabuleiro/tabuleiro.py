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
        self.posPals = dict(zip(range(dicionario.num_pals),self.dicionario.pals))
        self.palnum  = 1

    def tabuleiro(self,dicionario):
        """
            Instanciador da Classe Tabuleiro, responsavel por criar uma matriz com as Palavras geradas
        :param dicionario:
        :return: None
        """
        self.tabuleiro = list() # tabuleiro gabarito
        self.tabuleiroJog = list() # tabuleiro para o usuario
        self.dicionario = dicionario # lista de palavras interligadas para o tabuleiro
        self.palnum = 1

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
                    print(f"|{j[1]}|", end=" ")
                else:
                    print("   ", end=" ")
            print(" ")

    def getTabJog(self,select = None):
        """
            Retorna o tabuleiro do jogador
        :return: None
        """
        for l,i in enumerate(self.tabuleiroJog):
            for c, j in enumerate(i):
                if j != 0 or j == " ":
                    if select is None:
                        if type(j) is int:
                            print(f' {j} ',end=' ')
                        else:
                            print(f"|{j[1]}|", end=" ")
                    else:
                        if type(j) is int:
                            print(f' {j} ', end=' ')
                        else:
                            if select == j[0]:
                                print(f"\033[31m|{j[1]}|\033[m", end=" ")
                            else:
                                print(f"|{j[1]}|", end=" ")
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
            if l[1].upper() == posant[0].upper(): # Caso a letra seja igual a letra conectada
                cn = index # guarda o index da letra igual
                break # encerra o loop
        for index, letra in enumerate(palavra.getLetras()): # para cada letra da palavra
            if index == 0:
            #     self.posPals.update({self.palnum:(posant[2],index+posant[1])})
                for i in self.posPals.keys():
                    if self.posPals.get(i) == palavra:
                        self.tabuleiroJog[posant[2]][(index+posant[1])-cn-1] = i +1
            self.tabuleiro[posant[2]][(index+posant[1])-cn] = letra # posiciona a letra no tabuleiro gabarito
            if randint(0,10) % 2 == 0: # pequeno filtro para escolher quais letras não colocar
                self.tabuleiroJog[posant[2]][(index + posant[1]) - cn] = letra # posiciona a letra no tabuleiro do Jogador
            else:
                self.tabuleiroJog[posant[2]][(index + posant[1]) - cn] = (palavra,' ',letra[2])  # posiciona espaço vazio no tabuleiro do Jogador
            if letra[2]: #caso a letra esteja interligada em alguma palavra
                self.palnum += 1
                self.colocarVertical(letra[3],index,(letra[1],pos,(index+posant[1])-cn)) # chama a função para a palavra interligada

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
                if l[1].upper() == posant[0].upper():# Caso a letra seja igual a letra conectada
                    cn= index # guarda o index da letra igual
                    break# encerra o loop
            for index, letra in enumerate(palavra.getLetras()):# para cada letra da palavra
                if index == 0:
                    for i in self.posPals.keys():
                        if self.posPals.get(i) == palavra:
                            self.tabuleiroJog[(index + 4 + posant[1])-cn][posant[2]] = i +1
                #     self.posPals.update({self.palnum:((index + 5 + posant[1])-cn,posant[2])})
                self.tabuleiro[(index + 5 + posant[1])-cn][posant[2]] = letra # posiciona a letra no tabuleiro gabarito
                if randint(0, 10) % 2 == 0:# pequeno filtro para escolher quais letras não colocar
                    self.tabuleiroJog[(index + 5 + posant[1]) - cn][posant[2]] = letra  # posiciona a letra no tabuleiro do Jogador
                else:
                    self.tabuleiroJog[(index + 5 + posant[1]) - cn][posant[2]] = (palavra,' ',letra[2])  # posiciona espaço vazio no tabuleiro do Jogador
                if letra[2]:#caso a letra esteja interligada em alguma palavra
                    self.palnum =+ 1
                    self.colocarHorizontal(letra[3],index,(letra[1],pos,(index + 5 + posant[1])-cn))# chama a função para a palavra interligada
        else: # se for a primeira palavra
            for index, letra in enumerate(palavra.getLetras()):# para cada letra da palavra
                if index == 0:
                #     self.posPals.update({self.palnum: (index+5,pos)})
                    for i in self.posPals.keys():
                        if self.posPals.get(i) == palavra:
                            self.tabuleiroJog[index + 4][pos] = i +1
                self.tabuleiro[index+5][pos] = letra # posiciona a letra no tabuleiro gabarito
                if randint(0, 10) % 2 == 0 or letra == '-':# pequeno filtro para escolher quais letras não colocar
                    self.tabuleiroJog[index + 5][pos] = letra  # posiciona espaço vazio no tabuleiro do Jogador
                else:
                    self.tabuleiroJog[index + 5][pos] = (palavra,' ',letra[2]) # posiciona a letra no tabuleiro do Jogador
                if letra[2]:#caso a letra esteja interligada em alguma palavra
                    self.palnum += 1
                    self.colocarHorizontal(letra[3], index, (letra[1], pos,index+5))# chama a função para a palavra interligada

    def ganhou(self):
        for i in range(30):
            for j in range(30):
                if self.tabuleiroJog[i][j] != self.tabuleiro[i][j]:
                    return False
        return True


    def selectPalavra(self,num):
        try:
            if (num-1)%2 == 0:
                self.getTabJog(self.posPals[num-1])
                self.selectPosLetra(self.posPals[num-1])
            else:
                self.getTabJog(self.posPals[num-1])
                self.selectPosLetra(self.posPals[num - 1])
        except KeyError:
            print('Escreva um valor valido')

    def selectPosLetra(self,pal):
        ind = 0
        aux =[]
        for l, i in enumerate(self.tabuleiro):
            for c, j in enumerate(i):
                if j != 0:
                    if i[c][0] == 0 or i[c][0] == 0:
                        if self.tabuleiroJog[l][c] == self.tabuleiro[l][c]:
                            aux.append((self.tabuleiroJog[l][c],(l,c)))
                            print(f"|{j[1]}|", end=' ')
                        else:
                            aux.append((self.tabuleiroJog[l][c],(l,c)))
                            print(f"|{ind}|", end=" ")
                    elif j[0] == pal or (i[c][0] == pal and i[c][0] == pal):
                        ind += 1
                        if self.tabuleiroJog[l][c] == self.tabuleiro[l][c]:
                            aux.append((self.tabuleiroJog[l][c],(l,c)))
                            print(f"|{j[1]}|", end='-')
                        else:
                            aux.append((self.tabuleiroJog[l][c],(l,c)))
                            print(f"|{ind}|",end="-")
        print(" ")
        aux2 = self.letraInteraction(aux,input("Escolha a posição da letra: "))
        self.tabuleiroJog[aux2[1][0]][aux2[1][1]] = (pal,aux2[0])

    def letraInteraction(self,pal,ind):
        for j,i in enumerate(pal):
            if j == int(ind)-1:
                p= i[1]
                print(f"\033[34m|{i[0][1]}|\033[m", end=' ')
            else:
                print(f"|{i[0][1]}|", end=' ')
        print(" ")
        return input('digite a letra: '), p