import numpy as np

class Dado(object):
    def __init__(self,lados=2,trueRand=0):
        self.lado=np.zeros(lados)
        self.length=lados
        self.combo = np.zeros(self.length)
        self.result = -1
        self.TR=trueRand
        if(trueRand==1):
            self.result = self.result #isso é qualquer coisa so pra evitar conflito
            #self.listTrueRand = np.loadtxt("/Users/GabRyeL/OneDrive/Projetos/Python 3/Dado 1.0/List Rand.txt", delimiter="\r")
    def rolarDado(self,jogadas=1,quant=1):
        #Não é possível ter resultados com só uma jogada
        if self.result==-1 and jogadas==1:
            jogadas+=1
            
        for i in range(jogadas):
            self.anterior=self.result
            if(self.TR==1):
                self.result = np.int_(self.listTrueRand[quant]%self.length)
                #print(self.listTrueRand[quant],self.length)
            else:
                self.result = np.random.randint(0,self.length)
                #print(self.result)
            if self.anterior != self.result:
                self.combo[self.result] = 0
            self.combo[self.result] += 1
            self.lado[self.result] += 1
            
    def dados(self):
        auxLado=np.copy(self.lado)
        auxCombo=np.copy(self.combo)
        auxLado[self.result]-=1
        auxCombo[self.result]-=1
        X=np.append(auxLado,auxCombo)
        return X