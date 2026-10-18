'''
INICIO
LEER stock
pedidos = 0
PARA dia DESDE 1 HASTA 7:
    LEER ventas
    stock = stock - ventas
    SI stock < 10 :
        ESCRIBIR "Reponer", dia
        stock = stock + 50
        pedidos = pedidos + 1
    FIN SI
FIN PARA
ESCRIBIR stock, pedidos
FIN
'''