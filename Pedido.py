from Cliente import Cliente
from Producto import Producto


class Pedido:
    def __init__(self,id,fecha_pedido, id_cliente, id_producto, unidades):
        self.id = id
        self.fecha_pedido = fecha_pedido
        self.id_cliente = id_cliente
        self.id_producto = id_producto
        self.unidades = unidades

    def comprar (self):
        print("el cliente compra")

    def enviarSMS (self):
        print("Enviando SMS")

    def factura(self):
        print (f"Factura {self.id}")
        print(f"Nombre de cliente {self.id_cliente}")
        print(f"Unidades compradas {self.unidades}")

pedido1 = Pedido ("A1","10/05/2022",1,1,5)
pedido1.factura()

cliente100 = Cliente(100,"maria","sevilla",True)
producto20 = Producto(20,"sombrero",15,9.95,"05/10/2022")
pedido2 = Pedido("A2", "11,05/2022",cliente100,producto20,7)