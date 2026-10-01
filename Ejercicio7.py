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
        return f"Producto: {self.descripcion} | ID: {self.id_producto} | Precio: ${self.precio:.2f} | Stock: {self.stock}"

    def __eq__(self, otro):
        return self.id_producto == otro.id_producto and self.descripcion == otro.descripcion

class KwikEMart:
    def __init__(self):
        self.pasillos = {
            "Bebidas": [],
            "Snacks": [],
            "Conveniencia": []
        }

    def agregar_producto(self, pasillo, producto):
        if pasillo not in self.pasillos:
            self.pasillos[pasillo] = []
        self.pasillos[pasillo].append(producto)

    def buscar_por_id(self, id_producto):
        for lista in self.pasillos.values():
            for producto in lista:
                if producto.id_producto == id_producto:
                    return producto
        return None

    def remover_producto(self, id_producto):
        for lista in self.pasillos.values():
            for producto in lista:
                if producto.id_producto == id_producto:
                    lista.remove(producto)
                    return True
        return False

    def actualizar_stock(self, id_producto, nuevo_stock):
        prod = self.buscar_por_id(id_producto)
        if prod:
            prod.modificar(stock=nuevo_stock)
            return True
        return False

    def descartar_por_vencer(self):
        descartados = 0
        for nombre in self.pasillos:
            quedan = []
            for prod in self.pasillos[nombre]:
                if prod.dias_para_vencer() <= 1:
                    descartados += 1
                else:
                    quedan.append(prod)
            self.pasillos[nombre] = quedan
        return descartados
