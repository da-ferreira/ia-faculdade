
import pydot 
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

grafo = pydot.Dot(graph_type='graph', dpi = 300)  # Cria um objeto grafo

# Cria e adiciona o noh raiz
nohRaiz = pydot.Node("0 Raiz", style="filled", fillcolor = "#00ee11", xlabel = "0")
grafo.add_node(nohRaiz)

for i in range(3):
    #cria e adiciona novo noh
    nohFilho = pydot.Node("Filho %d" %(i+1), style="filled", fillcolor = "#ee0011", xlabel = "1")
    grafo.add_node(nohFilho)
    
    #cria um arco entre os nos
    arco = pydot.Edge(nohRaiz, nohFilho)
    #adiciona o arco ao grafo
    grafo.add_edge(arco)

#mostra o diagrama
grafo.write_png('grafo.png')
img=mpimg.imread('grafo.png')
plt.imshow(img)
plt.axis('off')
mng = plt.get_current_fig_manager()
mng.window.state('normal')
plt.show()




