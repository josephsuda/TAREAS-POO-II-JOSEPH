
class Controlador_tour:
    def __init__(self,modelo, vista):
        self.modelo = modelo
        self.vista = vista
    def ejecutar(self):
        opcion=""
        while opcion !="4":
            opcion = self.vista.menu()
            if opcion == "1":
                try:
                    nombre, precio, cupos= self.vista.solicitar_tour()
                    mensaje = self.modelo.registrar_tour(nombre, precio, cupos)
                    self.vista.mostrar_mensaje(mensaje)
                except ValueError:
                    self.vista.error("Datos ingresados incorrectamente")
            elif opcion == "2":
                
                try:
                    self.vista.mostrar_tours(self.modelo.mostrar_lista())
                except ValueError:
                    self.vista.mostrar_mensaje("lista vacia")

            elif opcion == "3":
                try:

                    codigo, cantidad= self.vista.solicitar_reserva()

                    restar = self.modelo.vender_tour(codigo, cantidad)
                    if restar == True: 
                        self.vista.mostrar_mensaje("operacion realizada correctamente")
                    else: 
                        self.vista.mostrar_mensaje("no existen cupos disponibles")

                except ValueError:
                     self.vista.mostrar_mensaje("datos ingresados incorrectamente")   

    
            
            


