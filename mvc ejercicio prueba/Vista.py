
class vista_tours:
    def menu(self):
        
        print("----TOURS DE CUENCA----\n")
        print("1. Registrar tour")
        print("2. Mostrar Tours")
        print("3. Reservar Cupos")
        print("4. salir")

        eleccion = input("elija una opcion del (1 al 4): ")
        return eleccion


    def solicitar_tour(self):
        nombre = input("Nombre del tour: ")
        precio = float(input("Precio: "))
        cupos = int(input("Cupos: "))

        return nombre, precio, cupos


    def solicitar_reserva(self):
        codigo = int(input("Ingrese el código del tour: "))
        cantidad = int(input("Cantidad de cupos a reservar: "))

        return codigo, cantidad


    def mostrar_tours(self, tours):
        print("--- LISTA DE TOURS ---\n")
        for tour in tours:
            print(tour)

    def mostrar_mensaje(self, mensaje):
        print(mensaje)

    def mostrar_salir(self):
        print("chao")


    def mostrar_invalido(self):
        print("dato invalido")