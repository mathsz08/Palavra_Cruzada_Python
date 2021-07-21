import pandas as pd
from random import randint

db = pd.read_table('dados.txt', index_col=0)


class palavra:

    def __init__(self, nome, definicao, dica, ant = None, pos = None, raiz = None):
        """
            Init classe Palavra responsavel por armazenar as caracterirsticas de cada palavra escolhida
        :param nome:
        :param definicao:
        :param dica:
        :param ant:
        :param pos:
        :param raiz:
        """
        self.conex = []
        self.ant = None
        self.pos = None
        self.raiz = None
        self.letras = []
        self.nome = nome
        self.definicao = definicao
        self.dica = dica
        for j in nome:
            aux = [j, False]
            self.letras.append(aux)

    def palavra(self, nome, definicao,dica , ant = None, pos = None, raiz = None):
        """
        Instanciador do objeto palavra, responsavel por receber algumas caractiristicas iniciais da Palavra
        :param nome:
        :param definicao:
        :param dica:
        :param ant:
        :param pos:
        :param raiz:
        :return:
        """

        self.ant = ant
        self.pos = pos
        self.raiz = raiz
        self.letras = []
        self.nome = nome
        self.definicao = definicao
        self.dica = dica
        for j in nome:
            aux = [j,self, False]
            self.letras.append(aux)

    def getNome(self):
        return self.nome

    def getTam(self):
        return len(self.letras)

    def getDefinicao(self):
        return self.definicao

    def getDica(self):
        return self.dica

    def getLetras(self):
        return self.letras

    def getLetra(self, pos):
        return self.letras[pos]

    #def defPos(self, i, pos):
     #   self.getLetra(i).append(pos)

    def getAnt(self):
        return self.ant

    def setAnt(self,value):
        self.ant = value

    def getPos(self):
        return self.pos

    def setPos(self, value):
        self.pos = value

    def getRaiz(self):
        return self.raiz

    def setRaiz(self, value):
        self.raiz = value

    def conectada(self):
        for i in self.getLetras():
            if i[1]:
                return True
        return False

    def conectar(self, index,val):
        self.conex.append(val)
        self.getLetra(index).append(val)
        self.getLetra(index)[2] = True


    def getPalavraInfo(self):
        aux = []
        print(f"-----------{self.getNome()}----------")
        if self.getPos() and self.getAnt() is not None:
            print(f"Conectada com : {self.getPos().getNome()} e {self.getAnt().getNome()}")
        elif self.getPos() is not None:
            print(f"Conectada com : {self.getPos().getNome()}")
        elif self.getAnt() is not None:
            print(f"Conectada com : {self.getAnt().getNome()}")
        else:
            pass

        for i in self.getLetras():
            if i[1]:
                aux.append(i)
        print("Letras conectadas : ", aux)