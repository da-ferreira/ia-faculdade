from Estado import Estado
import os

#estadoInicial = Estado('/home/ec2-user/environment/DiretorioInicial')
estadoInicial = Estado()
print ("Estado Inicial: ", estadoInicial.path)

"""
novosEstados = estadoInicial.funcaoSucessora()
print ("Próximos Estados a visitar: ",novosEstados)
"""

novoCaminho= os.path.join(estadoInicial.path, "d2", "d21","f211.txt")
estadoIntermediario = Estado(novoCaminho)
print ("estadoIntermediario", estadoIntermediario.path)

if estadoIntermediario.funcaoObjetivo():
    print("achou!!!")
else:
    print("não achou.")
