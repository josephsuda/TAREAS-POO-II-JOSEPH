class Tour:
    def __init__(self, codigo: int, nombre: str, precio: float, cupos: int):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.cupos = cupos

    def reservar(self, cantidad: int):
        if cantidad <= 0:
            print("Error: la cantidad debe ser mayor que cero.")
            return False
        if cantidad > self.cupos:
            print(f"Error: solo hay {self.cupos} cupos.")
            return False
        self.cupos -= cantidad
        print(f"el total de {self.cupos}")
        return True

    def __str__(self):
        return (
            f"Código: {self.codigo} | {self.nombre} | "
            f"Precio: ${self.precio:.2f} | Cupos disponibles: {self.cupos}"
        )


class Lista_tour:
    def __init__(self):
        self.lista_tour = []
        self.cargar_datos()

    def cargar_datos(self):
        lista = [
            Tour(1, "Centro histórico", 15.00, 20),
            Tour(2, "El cajas ", 35.50, 12)
        ]
        for f in lista:
            self.lista_tour.append(f)

    def registrar_tour(self, codigo: int, nombre: str, precio: float, cupos: int):
        self.lista_tour.append(Tour(codigo, nombre, precio, cupos))
        print(f"Registrado con el código {codigo}")

    def buscar_tour(self, codigo: int):
        for tour in self.lista_tour:
            if tour.codigo == codigo:
                return tour
        return None

    def vender_tour(self, codigo: int, cantidad: int):
        tour = self.buscar_tour(codigo)
        if tour is None:
            print("Error: no existe ese código.")
            return False
        return tour.reservar(cantidad)

    def mostrar_lista(self):
        return self.lista_tour

        
