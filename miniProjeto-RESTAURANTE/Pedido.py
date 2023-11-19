class Pedido():
    def __init__(self, cliente, pedido): 
        assert type(pedido) == str, 'Pedido incompleto!'
        self.__cliente = cliente
        self.__pedido = pedido

    @property
    def cliente(self)-> str:
        return self.__cliente

    @property
    def pedido(self)-> str:
        return self.__pedido

    @pedido.setter
    def pedido(self, novoPedido)-> None:
        assert type(novoPedido) == str, 'Pedido incompleto!'
        self.__pedido = novoPedido
    
    def __eq__(self, other):
        if isinstance(other, Pedido):
            return self.__cliente == other.__cliente and self.__pedido == other.__pedido
        return False

    def __str__(self):
        return f'Pedido de {self.__cliente}: {self.__pedido}'