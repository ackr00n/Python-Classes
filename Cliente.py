#POO : patron de desarrollo. Clase - Objeto
#empresa : CRM : Customer relational manager
#cliente : Objeto. clase (plantilla)
#propiedades: codigo_cliente,NIF, email, ciudad, activo
#metodos: añadir al carrito, añadir lista de deseos, compra, pago, pago aplazado, seguimiento, recomendar compras
#producto : objeto. classe (Plantilla)
#propiedades: codigo,nombre,familia,precio,unitstock,descuento ,etc
#metodos: pedirnuevostock, devolveproductodevuelto
#proveedor. clase. objeto
#pedidos : clase, objetos
#propiedades: fecha fra, numero fra , fecha de entrega, producto, cliente, transportista, etc
#metodos: firmaentrega

#Crear una clase
class Cliente:
    #propiedades / atributos / campos / adjetivos
    def __init__(self,id,nombre,ciudad,prime):#constructor
        self.id = id
        self.nombre = nombre
        self.ciudad = ciudad
        self.prime = prime

    def comprar (self): #metodo de instancia
        print("cliente compra") #metodo

    def valorar(self):
        print("cliente valora")

    def consultarFicha(self):
        print(f"Nombre: {self.nombre}, ciudad: {self.ciudad}, Eres Prime? {self.prime}")

    def fichaPDF(self):
        print(f"Cliente {self.nombre} en PDF")

#Usar la clase

cliente1 = Cliente(1,"Juan","Madrid",True)#dar de alta, Instanciar clase
print(cliente1.nombre)
cliente1.consultarFicha()
cliente1.fichaPDF()



class Pedido:
    pass




