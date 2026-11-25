from datetime import date

ARCHIVO_LIBROS = "libros.txt"
ARCHIVO_PRESTAMOS = "prestamos.txt"
LIBROS_INICIALES = [
    (1, "Python para todos", "Charles Severance"),
    (2, "Aprende Java", "Ana Torres"),
    (3, "Bases de datos", "Carlos Mora"),
]


class Libro:
    def __init__(self, codigo, titulo, autor, estado="Disponible"):
        self.codigo = codigo
        self.titulo = titulo
        self.autor = autor
        self.estado = estado

    def esta_disponible(self):
        return self.estado == "Disponible"

    def prestar(self):
        self.estado = "Prestado"

    def devolver(self):
        self.estado = "Disponible"

    def a_linea(self):
        # Texto que se guarda en libros.txt
        return f"{self.codigo},{self.titulo},{self.autor},{self.estado}\n"

    def mostrar(self):
        print(f"{self.codigo:<8} {self.titulo:<28} {self.autor:<22} {self.estado:<12}")


class Prestamo:
    def __init__(self, numero, codigo_libro, estudiante, fecha, estado="Activo"):
        self.numero = numero
        self.codigo_libro = codigo_libro
        self.estudiante = estudiante
        self.fecha = fecha
        self.estado = estado

    def esta_activo(self):
        return self.estado == "Activo"

    def devolver(self):
        self.estado = "Devuelto"

    def a_linea(self):
        # Texto que se guarda en prestamos.txt
        return f"{self.numero},{self.codigo_libro},{self.estudiante},{self.fecha},{self.estado}\n"



class Biblioteca:
    def __init__(self):
        self.libros = []
        self.prestamos = []
        self.cargar_libros()
        self.cargar_prestamos()

    def guardar_libros(self):
        with open(ARCHIVO_LIBROS, "w", encoding="utf-8") as archivo:
            for libro in self.libros:
                archivo.write(libro.a_linea())

    def cargar_libros(self):
        self.libros = []
        try:
            with open(ARCHIVO_LIBROS, "r", encoding="utf-8") as archivo:
                num_linea = 0
                for linea in archivo:
                    num_linea += 1
                    linea_limpia = linea.strip()
                    if linea_limpia != "":
                        datos = linea_limpia.split(",")
                        if len(datos) < 4:
                            print(f"Advertencia: Línea {num_linea} en libros.txt incompleta.")
                        else:
                            try:
                                libro = Libro(int(datos[0]), datos[1], datos[2], datos[3])
                                self.libros.append(libro)
                            except ValueError:
                                print(f"Advertencia: Error de formato numérico en línea {num_linea}.")
        except FileNotFoundError:
            print("No se encontró libros.txt: se usan los libros iniciales.")
            self.cargar_libros_iniciales()

        if len(self.libros) == 0:
            print("El archivo de libros está vacío. Se restaurarán los libros iniciales.")
            self.cargar_libros_iniciales()

    def cargar_libros_iniciales(self):
        for codigo, titulo, autor in LIBROS_INICIALES:
            self.libros.append(Libro(codigo, titulo, autor))
        self.guardar_libros()

    def guardar_prestamos(self):
        with open(ARCHIVO_PRESTAMOS, "w", encoding="utf-8") as archivo:
            for prestamo in self.prestamos:
                archivo.write(prestamo.a_linea())

    def cargar_prestamos(self):
        self.prestamos = []
        try:
            with open(ARCHIVO_PRESTAMOS, "r", encoding="utf-8") as archivo:
                num_linea = 0
                for linea in archivo:
                    num_linea += 1
                    linea_limpia = linea.strip()
                    if linea_limpia != "":
                        datos = linea_limpia.split(",")
                        if len(datos) >= 5:
                            try:
                                prestamo = Prestamo(int(datos[0]), int(datos[1]),
                                                    datos[2], datos[3], datos[4])
                                self.prestamos.append(prestamo)
                            except ValueError:
                                print(f"Advertencia: Error de formato en préstamo (línea {num_linea}).")
                        else:
                            print(f"Advertencia: Línea {num_linea} en prestamos.txt incompleta.")
        except FileNotFoundError:
            print("El archivo prestamos.txt no existe todavía, se iniciará vacío.")

    def buscar_por_codigo(self, codigo):
        for libro in self.libros:
            if libro.codigo == codigo:
                return libro
        return None

    def registrar_libro(self):
        print("\n--- 1. REGISTRAR LIBRO ---")
        titulo = leer_texto("Titulo del libro: ")
        autor = leer_texto("Autor del libro: ")

        mayor = 0
        for libro in self.libros:
            if libro.codigo > mayor:
                mayor = libro.codigo

        nuevo = Libro(mayor + 1, titulo, autor)
        self.libros.append(nuevo)
        self.guardar_libros()
        print(f"Libro '{titulo}' registrado con el codigo {nuevo.codigo}.")

    def mostrar_libros(self):
        print("\n--- 2. LISTA DE LIBROS ---")
        print(f"{'Codigo':<8} {'Titulo':<28} {'Autor':<22} {'Estado':<12}")
        print("-" * 72)
        for libro in self.libros:
            libro.mostrar()

    def buscar_libro(self):
        print("\n--- 3. BUSCAR LIBRO ---")
        palabra = leer_texto("Palabra clave del titulo: ")

        encontrados = 0
        for libro in self.libros:
            if palabra.lower() in libro.titulo.lower():
                libro.mostrar()
                encontrados += 1

        if encontrados == 0:
            print(f"No se encontro ningun libro con '{palabra}'.")

    def prestar_libro(self):
        print("\n--- 4. PRESTAR LIBRO ---")
        libro = self.buscar_por_codigo(leer_entero("Código del libro a prestar: "))

        if libro is None:
            print("Error: el codigo no existe.")
            return
        if not libro.esta_disponible():
            print("Error: este libro ya esta prestado.")
            return

        estudiante = leer_texto("Nombre del estudiante: ")
        numero = len(self.prestamos) + 1
        prestamo = Prestamo(numero, libro.codigo, estudiante, str(date.today()))
        self.prestamos.append(prestamo)
        libro.prestar()

        self.guardar_libros()
        self.guardar_prestamos()
        print(f"Prestamo #{numero} registrado: '{libro.titulo}' para {estudiante}.")

    def devolver_libro(self):
        print("\n--- 5. DEVOLVER LIBRO ---")
        libro = self.buscar_por_codigo(leer_entero("Codigo del libro a devolver: "))

        if libro is None:
            print("Error: el codigo no existe.")
            return
        if libro.esta_disponible():
            print("Error: este libro no esta prestado.")
            return

        libro.devolver()
        for prestamo in self.prestamos:
            if prestamo.codigo_libro == libro.codigo and prestamo.esta_activo():
                prestamo.devolver()

        self.guardar_libros()
        self.guardar_prestamos()
        print(f"El libro '{libro.titulo}' fue devuelto.")

    def mostrar_prestamos(self):
        print("\n--- 6. LISTA DE PRESTAMOS ---")
        print(f"{'No':<5} {'Libro':<28} {'Estudiante':<20} {'Fecha':<12} {'Estado':<10}")
        print("-" * 77)
        for p in self.prestamos:
            libro = self.buscar_por_codigo(p.codigo_libro)
            if libro is None:
                titulo_libro = "[Libro no encontrado]"
            else:
                titulo_libro = libro.titulo

            print(f"{p.numero:<5} {titulo_libro:<28} {p.estudiante:<20} {p.fecha:<12} {p.estado:<10}")

    def reporte_general(self):
        print("\n--- 7. REPORTE GENERAL ---")
        disponibles = 0
        prestados = 0
        for libro in self.libros:
            if libro.esta_disponible():
                disponibles += 1
            else:
                prestados += 1

        activos = 0
        for p in self.prestamos:
            if p.esta_activo():
                activos += 1

        try:
            porcentaje = prestados / len(self.libros) * 100
        except ZeroDivisionError:
            porcentaje = 0.0

        print(f"Total de libros:             {len(self.libros)}")
        print(f"Libros disponibles:          {disponibles}")
        print(f"Libros prestados:            {prestados}")
        print(f"Prestamos registrados:       {len(self.prestamos)}")
        print(f"Prestamos activos:           {activos}")
        print(f"Porcentaje libros prestados: {porcentaje:.1f}%")

    def guardar_todo(self):
        self.guardar_libros()
        self.guardar_prestamos()


def leer_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("  Error: debe escribir un numero entero.")


def leer_texto(mensaje):
    while True:
        texto = input(mensaje).strip()
        if texto == "":
            print("  Error: el texto no puede estar vacio.")
        elif "," in texto:
            print("  Error: el texto no puede contener comas.")
        else:
            return texto


def main():
    biblioteca = Biblioteca()  
    opcion = 0

    while opcion != 8:
        print("""
==================================
   BIBLIOTECA DIGITAL TEC AZUAY
==================================
1. Registrar libro    5. Devolver libro
2. Mostrar libros     6. Mostrar prestamos
3. Buscar libro       7. Reporte general
4. Prestar libro      8. Salir""")
        opcion = leer_entero("Elija una opcion: ")

        if opcion == 1:
            biblioteca.registrar_libro()
        elif opcion == 2:
            biblioteca.mostrar_libros()
        elif opcion == 3:
            biblioteca.buscar_libro()
        elif opcion == 4:
            biblioteca.prestar_libro()
        elif opcion == 5:
            biblioteca.devolver_libro()
        elif opcion == 6:
            biblioteca.mostrar_prestamos()
        elif opcion == 7:
            biblioteca.reporte_general()
        elif opcion == 8:
            biblioteca.guardar_todo()
            print("Datos guardados. Hasta pronto!")
        else:
            print("Opcion no valida: elija un numero del 1 al 8.")


main()
