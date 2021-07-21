def check(l1, l2):
    """
        Função responsavel por verificar condições de 'Conexão' entre duas Letras
    :param l1: Char
    :param l2: Char
    :return: Boolean
    """
    if l1[1] != "-" and (l1[1].upper() == l2[1].upper()) and (not l1[2] and not l2[2]) and (
            l1[2] is not None and l2[2] is not None):
        """
            Condições: 
                Não pode ser o caractere '-' :                   (l1[0] != '-')
                Precisam ser a mesma letra :                     (l1[0].upper() == l2[0].upper())
                Precisam não estar conectadas a outra letra :    (not l1[1] and not l2[1])
        """

        return True
    else:
        return False


def maior(palavras):
    """
        Retorna a maior palavra no grupo de palavras indicado
    :param palavras: List(Palavra)
    :return: Palavra
    """
    maioraux = palavras[1]
    for index, pal in enumerate(palavras):
        if pal.getTam() > maioraux.getTam() or index == 0:
            maioraux = pal
    return maioraux


class dicionario:

    def __init__(self, pals):
        """
            Init da classe Dicionario, responsavel por organizar as palavras na estrutura de arvore
        :param pals: List(Palavra)
        """
        self.matriz = []
        self.pals = pals
        self.num_pals = len(pals)
        self.Bpal = maior(pals)
        self.criarArvore()

    def dicionario(self, pals):
        """
        Instanciador da classe Dicionario, responsavel por organizar as palavras na estrutura de arvore
        :param pals: List(Palavra)
        :return: None
        """
        self.pals = pals
        self.matriz = []
        self.num_pals = len(pals)
        self.Bpal = maior(pals)
        self.criarArvore()

    def getMaior(self):
        return self.Bpal

    def getPals(self):
        """
            Retorna as palavras escolhidas para o jogo
        :return: List(Palavras)
        """
        return self.pals

    def criarArvore(self):
        """
        Organiza as palavras em uma estrutura de Arvore
        :return: None
        """
        for palavra in self.pals:
            self.letraForm(palavra)

        palavras = self.pegarPalavras(self.Bpal)
        self.Bpal.setAnt(palavras[0])
        self.Bpal.setPos(palavras[1])
        self.Bpal.setRaiz("Raiz")
        palavras[1].setRaiz(self.Bpal)
        palavras[0].setRaiz(self.Bpal)


        for palavra in self.pals:
            if palavra == self.Bpal:
                pass
            else:
                palavras = self.pegarPalavras(palavra)
                if not palavras:
                    break
                elif len(palavras) >= 2:
                    palavras[1].setRaiz(palavra)
                    palavra.ant = palavras[1]
                palavra.pos = palavras[0]
                palavras[0].setRaiz(palavra)

    def pegarPalavras(self, pal2):
        """
           Função responsavel por retornar as 2 palavras que serão conectadas com a palavra passada por parametro

        :param pal2: Palavra
        :return: List(Palavra)
        """
        aux = []  # array para guardar as palaras
        if pal2 == self.Bpal:  # Se a segunda palavras nao for passada, logo primeira palavra da cruzadinha
            for palavra in self.getPals():
                if len(aux) < 2 and pal2 != palavra:
                    if self.seConnect(pal2, palavra):  # se não tiver 2 palavras selecionadas
                        aux.append(palavra)
        else:
            for palavra in self.getPals():
                if self.pegarPalavraCond(pal2, palavra):  # A palavra não pode ser a palavra na qual ela esta ligada
                    if len(aux) < 2:
                        if self.seConnect(pal2, palavra):  # se elas se conectarem
                            aux.append(palavra)
        return aux  # Retorna Lista com as palavras conectadas

    def pegarPalavraCond(self, palavra1, palavra2):
        """
        Verifica as condições de disponibilidade das duas palavras passadas como parametro
        :param palavra1: Palavra
        :param palavra2: Palavra
        :return: Boolean
        """
        if palavra1.getRaiz() != palavra2 and palavra2 != palavra1 and palavra1.getRaiz() != palavra2.getRaiz() and palavra1 != palavra2.getRaiz() and palavra2.getRaiz() is None:
            return True
        else:
            return False

    def seConnect(self, pal1, pal2):
        """
        Função que itera letra por letra em duas palavras para verificar se elas podem se conectar

        :param pal1: Palavra
        :param pal2: Palavra
        :return : Boolean
        """
        for index2, l2 in enumerate(pal2.getLetras()):  # Para cada letra na primeira palavra
            for index1, l1 in enumerate(pal1.getLetras()):  # Para cada letra na segunda palavra
                if check(l1, l2):  # chama função para verificar condições de ligação
                    if pal1.getLetra(index1) != pal1.getLetra(pal1.getTam() - 1):
                        if (pal1.getLetra(index1 - 1)[2] is False and not None) and (
                                pal1.getLetra(index1 + 1)[2] is False and not None):
                            pal1.conectar(index1, pal2)  # Conecta a letra da palavra 1 com a letra da palavra 2
                            pal2.getLetra(index2)[2] = None
                            return True
        return False

    def letraForm(self,palavra):
        for i in palavra.getLetras():
            i.insert(0,palavra)

