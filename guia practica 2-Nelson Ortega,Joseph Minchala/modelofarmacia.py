
class Medicamento ():
    def __init__(self,codigo, nombre,precio,unidades,controlado):
        self.codigo=codigo
        self.nombre=nombre
        self.precio=precio
        self.unidades=unidades
        self.controlado=controlado


class Dispensacion ():
    def __init__(self,numero,codigo_medicamneto,cantidad,total,fecha,estado):
        self.numero=numero
        self.codigo=codigo_medicamneto
        self.cantidad=cantidad
        self.total=total
        self.fecha=fecha
        self.estado=estado


class Farmacia ():
    def __init__(self, lista_medicamentos, lista_dispensacion):
        self.lista_medicamentos = lista_medicamentos
        self.lista_dispensacion = lista_dispensacion
    
    def registrar(self):
        return ("Mensaje 1")
    def buscar_codigo(self):
        return ("Mensaje 1")
    def buscar(self):
        return ("Mensaje 1")
    def dispensar(self):
        return ("Mensaje 1")
    def anular(self):
        return ("Mensaje 1")
    def reporte(self):
        return ("Mensaje 1")
    def guardar(self):
        return ("Mensaje 1")
    def cargar(self):
        return ("Mensaje 1 ")