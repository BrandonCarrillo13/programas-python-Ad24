## p139-ventas
# p139_ventas - Aplicacion orientada a objetos que simula las ventas de una tienda 

class Venta:
    def _init_(self, articulo, cantidad, precio):
        self.articulo = articulo
        self.cantidad = cantidad
        self.precio = precio
        self.total = cantidad * precio
    def _str_(self):
        return f"Articulo:  {self.articulo:<15} Cantidad:  {self.cantidad:>10,.2f} Total: {self.total:>10,.2f}"

class Cliente:
    def _int_(self, rfc, nombre, domicilio, correo):
        self.rfc = rfc
        self.nombre = nombre
        self.domicilio = domicilio
        self.correo = correo
        self.ventas = list()
    def agregarVenta(self, venta):
        self.ventas.append(venta)
    def totalTienda(self):
        total=0
        for venta in self.ventas:
            total += venta.total
        return total
    def _str_(self):
        return f"Cliente [Nombre = {self.nombre:>15}  RFC: {self.rfc:<12} Domicilio: {self.domicilio:<20} Correo: {self.correo:<30}]"
    
class Tienda:
    def _init_(self, nombre, domicilio, propietario):
        self.nombre = nombre
        self.domicilio = domicilio
        self.propietario = propietario
        self.clientes = list()
    def agregarCliente(self, cliente):
        self.clientes.append(cliente)
    def totalVentas(self):
        total = 0
        for cliente in self.clientes:
            total += len(cliente.ventas)
        return total
    def totalImporteVentas(self):
        total = 0
        for cliente in self.clientes:
            total += cliente.totalVentas()
        return total
    def _str_(self):
        return f"Cliente [ Nombre = {self.nombre:>15}  Domicilio: {self.domicilio:<20} Propietario: {self.propietario}] - Total ventas: {self.totalImporteVentas():,.2f}"


# permite capturar un clientre y sus ventas 
def capturaCliente():
    print("Dame los datos del ciente")
    rfc = input("RFC     :")
    nombre = input("Nombre  :")
    domicilio = input("Domicilio: ")
    correo = input("Correo  :")
    cliente = Cliente(rfc, nombre, domicilio, correo)
    return cliente

def agregarVentas(cliente):
    print("Captura de Ventas ", cliente.nombre)
    while True:
        articulo = input("Articulo:   ")
        if articulo=="" : break
        cantidad = int(input("Cantidad: "))
        precio = float(input("Precio:  "))
        cliente.agregarVenta(Venta(articulo, cantidad, precio))
    

def main():
    # Importa librería para limpiar la terminal
    import os

    os.system("cls")
    mitienda = Tienda("Ferreteria las lomas", "Av Luis Moya 345)", "Carlos Castañeda")
    mitienda.agregarCliente(Cliente( "CARC711202", "Carlos Castañeda", "Av Mexico 115", "castr@uaz.edu.mx"))
    mitienda.clientes[0].agregarVenta{Venta("Martillo", 10, 200)}
    mitienda.clientes[0].agregarVenta{Venta("Pala", 5, 200)}
    mitienda.clientes[0].agregarVenta{Venta("Cinta de aislar", 15, 35)}
    mitienda.agregarCliente(Cliente("JOSE850324", "Jose Perez",  "Sierra Nevada 354", "Jose@gmail.com"))
    mitienda.cliente[1].agregarVenta(Venta("Pinzas", 10, 650.33)) 
    mitienda.cliente[1].agregarVenta(Venta("Thiner", 50, 65))
    mitienda.agregarCliente(Cliente("SOBR731123", "Rocio Soto",  "Sierra Tecuan 354", "rocio@gmail.com"))
    mitienda.cliente[1].agregarVenta(Venta("Talache", 2, 1650.33))     

    cliente = capturaCliente()
    agregarVentas(cliente)
    mitienda.agregarCliente(cliente)



if _name== '_main':
    main()