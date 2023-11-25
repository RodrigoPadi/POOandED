from datetime import date

class VideogameException(Exception):
    def __init__(self, msg):
        super().__init__(msg)

class Videogame():

    def __init__(self, marca, dataFabricacao, modelo, numSerie):
        self.__dataFabricacao = dataFabricacao
        self.__marca = marca
        self.__modelo = modelo
        self.__numSerie = numSerie + '-' + str(date.today())

    @property
    def dataFabricacao(self):
        return self.__dataFabricacao
        
    @dataFabricacao.setter
    def dataFabricacao(self, novaData):
        self.__dataFabricacao = novaData
        
    @property
    def marca(self):
        return self.__marca

    @marca.setter
    def marca(self, novaMarca):
        self.__marca = novaMarca
        
    @property
    def modelo(self):
        return self.__modelo
        
    @modelo.setter
    def modelo(self, novoModelo):
        self.__modelo = novoModelo
        
    @property
    def numSerie (self):
        return self.__numSerie
        
    @numSerie.setter
    def numSerie(self, novoNumSerie):
        self.__numSerie = novoNumSerie + '-' + str(date.today())
        
    def __str__(self):
        return f'Videogame: {self.__modelo}/ Data de fabricação: {self.__dataFabricacao}/ Marca: {self.__marca}/ Número de série: {self.__numSerie}'