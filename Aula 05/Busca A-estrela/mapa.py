
# Conexões entre pontos

conexoes = {
	"Carregamento":          {"Estoque Pronto"},
	"Home e Energia":        {"Estacao 1", "Estacao 4", "Estoque Intermediario"},
	"Estoque Intermediario": {"Deposito Insumos 2", "Home e Energia", "Estoque Pronto", "Estacao 3"},
	"Deposito Insumos 1":    {"Estacao 1"},
	"Deposito Insumos 2":    {"Estacao 1", "Estoque Intermediario" , "Estacao 2"},
	"Estoque Pronto":        {"Estacao 4", "Estoque Intermediario", "Carregamento"},
	"Estacao 1":             {"Deposito Insumos 1", "Deposito Insumos 2","Home e Energia"},
	"Estacao 2":             {"Deposito Insumos 2", "Estacao 3"},
	"Estacao 3":             {"Estacao 2", "Estoque Intermediario"},
	"Estacao 4":             {"Home e Energia", "Estoque Pronto"}
}

# Localização (coordenadas x, y do mapa topológico) de todos os lugares 

localizacao = {
	"Carregamento": [6, 0],
	"Home e Energia": [1, 4],
	"Estoque Intermediario": [6, 4],
	"Deposito Insumos 1": [2, 8],
	"Deposito Insumos 2": [6, 8],
	"Estoque Pronto": [6, 1],
	"Estacao 1": [4, 8],
	"Estacao 2": [7, 7],
	"Estacao 3": [7, 5],
	"Estacao 4": [4, 1]
}
