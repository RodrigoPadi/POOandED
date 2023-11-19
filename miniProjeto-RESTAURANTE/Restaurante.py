from Fila import Fila, FilaException
from Pedido import Pedido

class RestauranteExcepction(Exception):
    def __init__(self, msg):
        super().__init__(msg)

class Restaurante():
    def __init__(self, nome:str):
        self.__nome = nome
        self.__esperar = Fila()
        self.__preparar = Fila()
        self.__entregar = Fila()

    def __str__(self):
        return f'Nome: {self.__cliente}'
    
    @property
    def esperar(self):
        return self.__esperar

    @property
    def preparar(self):
        return self.__preparar
    
    @property
    def entregar(self):
        return self.__entregar

    def inserirCliente(self, nome):
        self.__esperar.enfileirar(nome)
        return
    
    def pegarCliente(self):
        cliente_atual = self.__esperar.desenfileirar()
        return cliente_atual

    def realizarPedido(self, pedido):
        self.__preparar.enfileirar(pedido)
        return

    def pegarPedido(self):
        pedido_atual = self.__preparar.desenfileirar()
        return pedido_atual

    def iniciarPreparo(self, pedido):
        self.fila__entregar.enfileirar(pedido)
        return
        
    def realizarEntrega(self):
        pedido_entregue = self.__entregar.desenfileirar()
        return pedido_entregue