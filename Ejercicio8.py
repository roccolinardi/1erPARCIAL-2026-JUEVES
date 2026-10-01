from datetime import date, timedelta

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

class Nodo:
    def __init__(self, dato, sig=None):
        self._elem = dato
        self._nxt = sig

class ListaEnlazada:
    def __init__(self):
        self.header = Nodo(0)
        self.tamanio = 0

    def append(self, dato):
        actual = self.header
        while actual._nxt is not None:
            actual = actual._nxt
        actual._nxt = Nodo(dato)
        self.tamanio += 1

    def remove(self, dato):
        anterior = self.header
        actual = self.header._nxt
        while actual is not None:
            if actual._elem == dato:
                anterior._nxt = actual._nxt
                self.tamanio -= 1
                return True
            anterior = actual
            actual = actual._nxt
        return False

    def __len__(self):
        return self.tamanio

    def __iter__(self):
        return IteradorLista(self.header._nxt)

class IteradorLista:
    def __init__(self, inicio):
        self.actual = inicio

    def __iter__(self):
        return self

    def __next__(self):
        if self.actual is None:
            raise StopIteration
        dato = self.actual._elem
        self.actual = self.actual._nxt
        return dato

class KwikEMart:
    def __init__(self):
        self.pasillos = {
            "Bebidas": ListaEnlazada(),
            "Snacks": ListaEnlazada(),
            "Conveniencia": ListaEnlazada()
        }

    def agregar_producto(self, pasillo, producto):
        if pasillo not in self.pasillos:
            self.pasillos[pasillo] = ListaEnlazada()
        self.pasillos[pasillo].append(producto)

    def buscar_por_id(self, id_producto):
        for lista in self.pasillos.values():
            for prod in lista:
                if prod.id_producto == id_producto:
                    return prod
        return None

    def remover_producto(self, id_producto):
        for lista in self.pasillos.values():
            for prod in lista:
                if prod.id_producto == id_producto:
                    lista.remove(prod)
                    return True
        return False

    def actualizar_stock(self, id_producto, nuevo_stock):
        prod = self.buscar_por_id(id_producto)
        if prod:
            prod.modificar(stock=nuevo_stock)
            return True
        return False

    def descartar_por_vencer(self):
        limite = date.today() + timedelta(days=1)
        descartados = 0
        for lista in self.pasillos.values():
            quitar = [p for p in lista if p.fecha_vencimiento <= limite]
            for p in quitar:
                lista.remove(p)
                descartados += 1
        return descartados
