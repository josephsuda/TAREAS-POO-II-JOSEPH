
from Modelo import*
from Vista import vista_tours
from controlador import Controlador_tour

modelo = Lista_tour()
vista= vista_tours()
controlador = Controlador_tour(modelo,vista)
controlador.ejecutar()

