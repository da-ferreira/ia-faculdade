
# Cria um dicionário com todos os mapeamentos

conexoes = {}

conexoes["Ana"] = {"Jose", "Tom"}
conexoes["Jose"] = {"Rui", "Fernanda", "Ana"}
conexoes["Tom"] = {"Pedro", "Ana", "Gil"}
conexoes["Rui"] = {"Jose", "Gil"}
conexoes["Gil"] = {"Maria", "Rui", "Tom"}
conexoes["Maria"] = {"Gil"}
conexoes["Fernanda"] = {"Jose", "Henrique"}
conexoes["Pedro"] = {"Tom"}
conexoes["Henrique"] = {"Fernanda"}


if __name__ == "__main__":
    print(conexoes)
    print(conexoes["Rui"])
     