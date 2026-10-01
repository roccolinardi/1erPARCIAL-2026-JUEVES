from datetime import date
class ProductoKwikE:
    def __init__(self, descripcion, id_producto, fecha_vencimiento,
                 precio, stock, categoria="General"):
        self.descripcion = descripcion              # str
        self.id_producto = id_producto              # int
        self.fecha_vencimiento = fecha_vencimiento  # datetime.date
        self.precio = precio                        # float
        self.stock = stock                          # int
        self.categoria = categoria                  # str (atributo extra)
 
    def modificar(self, descripcion=None, precio=None, stock=None):
        """Cambia uno o varios datos: solo los que se pasen por parámetro."""
        if descripcion is not None:
            self.descripcion = descripcion
        if precio is not None:
            self.precio = precio
        if stock is not None:
            self.stock = stock
 
    def dias_para_vencer(self):
        dias = (self.fecha_vencimiento - date.today()).days
        if dias < 0:
            print(f"¡Atención! '{self.descripcion}' ya expiró. Stock puesto en 0.")
            self.stock = 0
          
        return dias
