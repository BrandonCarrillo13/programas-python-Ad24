import os 
os.system("cls")
class Articulo:
    def __init__(self,id, descripcion, cantidad, precio):
        self.id = id
        self.descripcion = descripcion
        self.cantidad = cantidad
        self.precio = precio
    def obtenerTotal(self):
        return self.precio * self.cantidad
    def __str__(self):
        return f"Id: {self.id}, Descripcion: {self.descripcion}, Cantidad: {self.cantidad}, Precio: {self.precio}, Total: {self.obtenerTotal()} "
    
art01 = Articulo('A101', 'Pluma Roja', 888, 0.08)
print(art01)
art01.cantidad = 999
art01.precio = 0.99
print("id = ",art01.id)
print("descripcion = ",art01.descripcion)
print("cantidad = ",art01.cantidad)
print("precio = ",art01.precio)
print("total = ",art01.obtenerTotal())
art02 = Articulo("A102", "Pluma Azul", 934, 1.2)
print(art02)
art3 = Articulo("P103", "Lapiz del 12", 456, 0.5)
print(art3)
total = art01.obtenerTotal() + art02.obtenerTotal() + art3.obtenerTotal()
print('Total todos:', total)