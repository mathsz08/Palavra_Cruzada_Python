from Palavras import palavra as pl
from Palavras import dicionario as dc
from Tabuleiro import tabuleiro as tab
from Jogo import jogada
import pandas as pd
from random import randint

db = pd.read_table('dados.txt', index_col=0)


class Jogo:
    def __init__(self):
        pass


def start():
    tabu = getVariables()
    tabu.getTabJog()




def gerar(num):
    lista = list()
    for i in range(num):
        while True:
            j = randint(0, num)
            if j not in lista:
                lista.append(j)
                break

    aux = db.iloc[lista, :]
    palavras = []
    for index, linha in aux.iterrows():
        aux = pl.palavra(index, linha['Definicao'], linha['Dica'])
        palavras.append(aux)

    palavras = quick(palavras, 0, len(palavras) - 1)
    return palavras


def sep(pals, menor, maior):
    ind = menor - 1
    p = pals[maior].getTam()

    for i in range(menor, maior):
        if pals[i].getTam() <= p:
            ind += 1
            pals[ind], pals[i] = pals[i], pals[ind]

    pals[ind + 1], pals[maior] = pals[maior], pals[ind + 1]
    return ind + 1


def quick(pals, menor, maior):
    if menor < maior:
        pi = sep(pals, menor, maior)
        quick(pals, menor, pi - 1)
        quick(pals, pi + 1, maior)
    return pals[::-1]


def getVariables():
    palavras = gerar(6)
    dici = dc.dicionario(palavras)
    tabu = tab.tabuleiro(dici)
    tabu.criarTab()
    tabu.colocarPalavras(dici.getMaior())
    return tabu