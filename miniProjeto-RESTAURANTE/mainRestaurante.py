from Restaurante import Restaurante, RestauranteExcepction
from Pedido import Pedido

restaurante1 = Restaurante('Delizia di Pasta')

while True:
    try:

        print(f'''
----------------------------------------------------
                    << Filas >>
----------------------------------------------------
Espera:
{restaurante1.esperar}
Preparo:
{restaurante1.preparar}
Entrega:
{restaurante1.entregar}
===========================================
(e) Inserir cliente na fila de atendimento.
(c) Chamar cliente em espera.
(i) Iniciar preparo da refeição.
(r) Sair com pedido para entrega.
(s) Encerrar programa.
===========================================''')

        op = input('Opção: ').lower()

        if (op == 'e'):  # Inserir cliente na fila de atendimento.
            nome = input('Digite seu nome: ')
            restaurante1.inserirCliente(nome)
            print(
                f'<< Aguarde... você está na {restaurante1.esperar.busca(nome)} posição no atendimento. Aguarde! >>')

        elif (op == 'c'):  # Chamar cliente em espera.
            pegar_cliente = restaurante1.pegarCliente()
            print(f'Olá {pegar_cliente}!')
            pedido = input('Qual o seu pedido: ')
            pedido_atual = Pedido(pegar_cliente, pedido)
            print(f'Informações do pedido: {pedido}')
            entra = input('Confirma o pedido (s/n)? ').lower()

            if entra == 's':
                restaurante1.preparar.enfileirar(pedido_atual)
                print('Pedido realizado com sucesso!!! Vamos preparar seu prato.')
                print(
                    f'<< Seu pedido está na {len(restaurante1.preparar)}a posição na fila de preparo ')
                print(
                    f'e ficará pronto em {restaurante1.preparar.busca(pedido_atual) * 20} min >>')
            else:
                print('O pedido não foi realizado ou está incompleto. Cliente descartado!')

        elif (op == 'i'):  # Iniciar preparo da refeição.
            if restaurante1.preparar.estaVazia() == False:
                pedido_atual = restaurante1.preparar.desenfileirar()
                print(f'Pedido da vez: {pedido_atual.pedido}')
                print(f'Cliente: Sr(a) {pedido_atual.cliente}')
                confirmacao = input(
                    'Pedido já está pronto para entrega (S/N)? ').lower()

                if confirmacao == 's':
                    restaurante1.entregar.enfileirar(pedido_atual)
                    print(
                        f'<< Seu pedido está na {len(restaurante1.entregar)}ª posição para entrega. É rápido, temos vários entregadores >>')
                else:
                    pedido_atual = restaurante1.preparar.enfileirar(pedido_atual)
                    print('Seu pedido ainda não ficou pronto. Volte para a fila!')

            else:
                print('Fila de clientes vazia!')        

        elif (op == 'r'): # Sair com pedido para entrega.
            if restaurante1.entregar.estaVazia() == False:
                entrega_atual = restaurante1.entregar.desenfileirar()
                print(f'Pedido do(a) Sr(a) {entrega_atual.cliente} saindo para entrega!!!')
                print(entrega_atual.pedido)

        elif (op == 's'): # Encerrar programa.
            break

    except RestauranteExcepction as re:
        print(re)
    except AssertionError as ae:
        print(ae)
    except BaseException as b:
        print('A fila de espera está vazia!')
    except Exception as e:
        print(e)
