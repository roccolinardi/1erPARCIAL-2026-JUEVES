from datetime import date

class ProductoKwikE:
    def __init__(self, descripcion, id_producto, fecha_vencimiento, precio, stock, categoria="General"):
        self.descripcion = descripcion
        self.id_producto = id_producto
        self.fecha_vencimiento = fecha_vencimiento
        self.precio = precio
        self.stock = stock
        self.categoria = categoria

    def modificar(self, descripcion=None, precio=None, stock=None):
        if descripcion is not None:
            self.descripcion = descripcion
        if precio is not None:
            self.precio = precio
        if stock is not None:
            self.stock = stock

    def dias_para_vencer(self):
        dias = (self.fecha_vencimiento - date.today()).days
        if dias < 0:
            print(f"El producto {self.descripcion} vencio. Stock en 0")
            self.stock = 0
        return dias

    def __str__(self):
        return f"Producto: {self.descripcion} | ID: {self.id_producto} | Precio: ${self.precio} | Stock: {self.stock}"

    def __eq__(self, otro):
        return self.id_producto == otro.id_producto and self.descripcion == otro.descripcion
