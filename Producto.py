#POO
#entidad: Producto. clase.
#propiedades, campos, atributos: id,nombre,unidades, precio, fechaFabricacion
#metodos: reponerStock, aplicarDescuentos,


class Producto:
    def __init__(self, id, nombre, unidades, precio, fechaFabricacion):
        self.id = id # almacenar en la instacia el parametro
        self.nombre = nombre #string
        self.unidades = unidades #int
        self.precio = precio #float
        self.fechaFabricacion = fechaFabricacion #date

#Python utiliza interferencia de tipos. Por eso NO es necesario
#indicar el tipo de dato al declarar la variable si Python
#NO tiene todavia el dato, por defecto el tipo es An
#Explicar en memoria que diferencia hay entre tipado fuerte, debil y inferencia
#compilados son normalmente de tipado fuerte
#interpretados son normalmente de tipador por inferencia o a veces, tipado debil

    def reponerStock(self):
        if self.unidades < 10:
            print("Tenemos que reponer")
        else:
            print(f"Mi stock actual es de {self.unidades}")

producto1= Producto(100,"camisa",7, 5.59, "10/05/2022")
producto1.reponerStock()


