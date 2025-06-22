# Clase Producto
class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def mostrar_info(self):
        print(f"Producto: {self.nombre} - Precio: ${self.precio} - Stock: {self.stock} unidades")

    def vender(self, cantidad):
        if cantidad <= self.stock:
            self.stock -= cantidad
            total = cantidad * self.precio
            print(f"Venta exitosa. Total a pagar: ${total}")
        else:
            print("No hay suficiente stock para realizar la venta.")

# Clase Tienda
class Tienda:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_productos(self):
        print(f"\nInventario de {self.nombre}:")
        for producto in self.productos:
            producto.mostrar_info()

    def comprar_producto(self, nombre_producto, cantidad):
        for producto in self.productos:
            if producto.nombre == nombre_producto:
                producto.vender(cantidad)
                return
        print("Producto no encontrado.")

# --- Programa principal ---

# Crear una tienda
mi_tienda = Tienda("Tienda Escolar")

# Crear productos
lapiz = Producto("Lápiz", 0.50, 100)
cuaderno = Producto("Cuaderno", 1.20, 50)

# Agregar productos a la tienda
mi_tienda.agregar_producto(lapiz)
mi_tienda.agregar_producto(cuaderno)

# Mostrar productos
mi_tienda.mostrar_productos()

# Comprar producto
mi_tienda.comprar_producto("Lápiz", 5)

# Ver inventario actualizado
mi_tienda.mostrar_productos()
