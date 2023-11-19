class FilaException(Exception):
    def __init__(self,msg):
        super().__init__(msg)

class No:
    def __init__(self, carga:any):
        self.__carga = carga
        self.__prox = None

    @property
    def carga(self)->any:
        return self.__carga
    
    @property
    def prox(self)->'No':
        return self.__prox

    @carga.setter
    def carga(self, novaCarga:any):
        self.__carga = novaCarga

    @prox.setter
    def prox(self, novoProx:'No'):
        self.__prox = novoProx
    
    def __str__(self):
        return f'{self.__carga}'

class Head:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0
        
class Fila:
    def __init__(self):
        self.__head = Head()


    def estaVazia(self)->bool:
        return self.__head.tamanho == 0

    def __len__(self)->int:
        return self.__head.tamanho

    def elementoDaFrente(self)->any:
        if self.estaVazia():
            raise FilaException(f'Fila Vazia. Não há elemento a recuperar.')
        return self.__head.inicio.carga

    def busca(self, chave:any)->int:
        cursor = self.__head.inicio
        contador = 1

        while( cursor != None):
            if cursor.carga == chave:
                return contador           
            cursor = cursor.prox
            contador += 1

        raise FilaException(f'Chave {chave} inexistente na fila')

    def elemento(self, posicao:int)->any:
        try:
            if self.estaVazia():
                raise FilaException('Fila Vazia.')
            assert posicao > 0 and posicao <= len(self)
            cursor = self.__head.inicio
            contador = 1
            while(cursor != None and contador < posicao ):
                contador += 1
                cursor = cursor.prox

            return cursor.carga
            
        except TypeError:
            raise FilaException(f'A posicao referente ao elemento deve ser do tipo inteiro')
        except AssertionError:
            raise FilaException(f'Posicao invalida. Forneça um valor entre 1 e {self.__head.tamanho}.')
        except:
            raise

    def enfileirar(self, carga:any ):
        novo = No(carga)
        if self.estaVazia():
            self.__head.inicio = self.__head.fim = novo
        else:
            self.__head.fim.prox = novo
            self.__head.fim = novo
        self.__head.tamanho += 1


    def desenfileirar(self)->any:
        try:
            assert not self.estaVazia()

            carga = self.__head.inicio.carga

            if self.__head.tamanho ==1:
                self.__head.fim = None

            self.__head.inicio = self.__head.inicio.prox
            self.__head.tamanho -= 1
            return carga
            
        except AssertionError as ae:
            raise FilaException(f'A fila está vazia! Não é possivel remover elementos')
                    
    def __str__(self):
        s = 'frente->[ '
        cursor = self.__head.inicio
        while(cursor != None):
            s += f'{cursor.carga}, ' 
            cursor = cursor.prox
        return s[:-2] + " ]" if not self.estaVazia() else  s + ' ]'