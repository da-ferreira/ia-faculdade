from os import path
from No import No
from Estado import Estado

estadoInicial = Estado()
raiz = No(estadoInicial)

estadosFilhos = raiz.estado.funcaoSucessora()
#print(estadosFilhos)

for estadoFilho in estadosFilhos:
    noFilho = No(Estado(estadoFilho))
    raiz.addFilho(noFilho)

print("Local do estado:", raiz.estado.path)
print("Profundidade:", raiz.profundidade)
print("Filhos:", [x.estado.path for x in raiz.filhos])
print("Nó pai:", raiz.pai)
    
raiz.printArvore()
