from datetime import date

ARCHIVO_LIBROS = "libros.txt"
ARCHIVO_PRESTAMOS = "prestamos.txt"
LIBROS_INICIALES = [
    {"codigo": 1, "titulo": "Python para todos",
     "autor": "Charles Severance", "estado": "Disponible"},
    {"codigo": 2, "titulo": "Aprende Java",
     "autor": "Ana Torres", "estado": "Disponible"},
    {"codigo": 3, "titulo": "Bases de datos",
     "autor": "Carlos Mora", "estado": "Disponible"},
]


# FUNCIONES DE CREACION/INSPECCION DEL PROGRAMA

def guardar_libros(libros):
    with open(ARCHIVO_LIBROS, "w", encoding="utf-8") as archivo:
        for l in libros:
            archivo.write(f"{l['codigo']},{l['titulo']},{l['autor']},{l['estado']}\n")
#cambio 3
def cargar_libros():
    libros = []
    try:
        with open(ARCHIVO_LIBROS, "r", encoding="utf-8") as archivo:
            num_linea = 0
            for linea in archivo:
                num_linea = num_linea + 1
                linea_limpia = linea.strip()
                if linea_limpia == "":
                    linea_valida = False
                else:
                    linea_valida = True
                
                if linea_valida:
                    datos = linea_limpia.split(",")
                    if len(datos) < 4:
                        print(f"Advertencia: Línea {num_linea} en libros.txt incompleta.")
                    else:
                        try:
                            libros.append({
                                "codigo": int(datos[0]),
                                "titulo": datos[1],
                                "autor": datos[2],
                                "estado": datos[3]
                            })
                        except ValueError:
                            print(f"Advertencia: Error de formato numérico en línea {num_linea}.")
                            
    except FileNotFoundError:
        print("No se encontró libros.txt: se usan los libros iniciales.")
        for libro in LIBROS_INICIALES:
            libros.append(dict(libro))
        guardar_libros(libros)
    
    if len(libros) == 0:
        print("El archivo de libros está vacío. Se restaurarán los libros iniciales.")
        for libro in LIBROS_INICIALES:
            libros.append(dict(libro))
        guardar_libros(libros)
        
    return libros


def guardar_prestamos(prestamos):
    with open(ARCHIVO_PRESTAMOS, "w", encoding="utf-8") as archivo:
        for p in prestamos:
            archivo.write(f"{p['numero']},{p['codigo_libro']},{p['estudiante']},{p['fecha']},{p['estado']}\n")

# cambio 2
def cargar_prestamos():
    prestamos = []
    try:
        with open(ARCHIVO_PRESTAMOS, "r", encoding="utf-8") as archivo:
            num_linea = 0
            for linea in archivo:
                num_linea = num_linea + 1
                linea_limpia = linea.strip()

                if linea_limpia != "":
                    datos = linea_limpia.split(",")
                    if len(datos) >= 5:
                        try:
                            prestamos.append({
                                "numero": int(datos[0]),
                                "codigo_libro": int(datos[1]),
                                "estudiante": datos[2],
                                "fecha": datos[3],
                                "estado": datos[4]
                            })
                        except ValueError:
                            print(f"Advertencia: Error de formato en préstamo (línea {num_linea}).")
                    else:
                        print(f"Advertencia: Línea {num_linea} en prestamos.txt incompleta.")
                        
    except FileNotFoundError:
        print("El archivo prestamos.txt no existe todavía, se iniciará vacío.")
        
    return prestamos


# VALIDADORES DEL PROGRAMA Y FUNCIONES DE INPUT

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


def buscar_por_codigo(libros, codigo):
    for l in libros:
        if l["codigo"] == codigo:
            return l
    return None


# FUNCIONES DIRECTAS DEL MENU

def registrar_libro(libros):
    print("\n--- 1. REGISTRAR LIBRO ---")
    titulo = leer_texto("Titulo del libro: ")
    autor = leer_texto("Autor del libro: ")

    mayor = 0
    for l in libros:
        if l["codigo"] > mayor:
            mayor = l["codigo"]

    libro = {"codigo": mayor + 1, "titulo": titulo, "autor": autor, "estado": "Disponible"}
    libros.append(libro)
    guardar_libros(libros)
    print(f"Libro '{titulo}' registrado con el codigo {libro['codigo']}.")
    return libro


def mostrar_libros(libros):
    print("\n--- 2. LISTA DE LIBROS ---")
    print(f"{'Codigo':<8} {'Titulo':<28} {'Autor':<22} {'Estado':<12}")
    print("-" * 72)
    for l in libros:
        print(f"{l['codigo']:<8} {l['titulo']:<28} {l['autor']:<22} {l['estado']:<12}")
    return len(libros)


def buscar_libro(libros):
    print("\n--- 3. BUSCAR LIBRO ---")
    palabra = leer_texto("Palabra clave del titulo: ")

    encontrados = 0
    for l in libros:
        if palabra.lower() in l["titulo"].lower():
            print(f"{l['codigo']:<8} {l['titulo']:<28} {l['autor']:<22} {l['estado']:<12}")
            encontrados += 1

    if encontrados == 0:
        print(f"No se encontro ningun libro con '{palabra}'.")
    return encontrados


def prestar_libro(libros, prestamos):
    print("\n--- 4. PRESTAR LIBRO ---")
    libro = buscar_por_codigo(libros, leer_entero("Código del libro a prestar: "))

    if libro is None:
        print("Error: el codigo no existe.")
        return False
    if libro["estado"] == "Prestado":
        print("Error: este libro ya esta prestado.")
        return False

    estudiante = leer_texto("Nombre del estudiante: ")
    numero = len(prestamos) + 1
    prestamos.append({"numero": numero, "codigo_libro": libro["codigo"],
                      "estudiante": estudiante, "fecha": str(date.today()),
                      "estado": "Activo"})
    libro["estado"] = "Prestado"

    guardar_libros(libros)
    guardar_prestamos(prestamos)
    print(f"Prestamo #{numero} registrado: '{libro['titulo']}' para {estudiante}.")
    return True


def devolver_libro(libros, prestamos):
    print("\n--- 5. DEVOLVER LIBRO ---")
    libro = buscar_por_codigo(libros, leer_entero("Codigo del libro a devolver: "))

    if libro is None:
        print("Error: el codigo no existe.")
        return False
    if libro["estado"] == "Disponible":
        print("Error: este libro no esta prestado.")
        return False

    libro["estado"] = "Disponible"
    for p in prestamos:
        if p["codigo_libro"] == libro["codigo"] and p["estado"] == "Activo":
            p["estado"] = "Devuelto"

    guardar_libros(libros)
    guardar_prestamos(prestamos)
    print(f"El libro '{libro['titulo']}' fue devuelto.")
    return True

# cambio uno 
def mostrar_prestamos(prestamos, libros):
    print("\n--- 6. LISTA DE PRESTAMOS ---")
    print(f"{'No':<5} {'Libro':<28} {'Estudiante':<20} {'Fecha':<12} {'Estado':<10}")
    print("-" * 77)
    for p in prestamos:
        libro = buscar_por_codigo(libros, p["codigo_libro"])
        if libro == None:
            titulo_libro = "[Libro no encontrado]"
        else:
            titulo_libro = libro['titulo']
            
        print(f"{p['numero']:<5} {titulo_libro:<28} {p['estudiante']:<20} {p['fecha']:<12} {p['estado']:<10}")
    return len(prestamos)


def reporte_general(libros, prestamos):
    print("\n--- 7. REPORTE GENERAL ---")
    disponibles = 0
    prestados = 0
    for l in libros:
        if l["estado"] == "Disponible":
            disponibles += 1
        else:
            prestados += 1

    activos = 0
    for p in prestamos:
        if p["estado"] == "Activo":
            activos += 1

    try:
        porcentaje = prestados / len(libros) * 100
    except ZeroDivisionError:
        porcentaje = 0.0

    print(f"Total de libros:             {len(libros)}")
    print(f"Libros disponibles:          {disponibles}")
    print(f"Libros prestados:            {prestados}")
    print(f"Prestamos registrados:       {len(prestamos)}")
    print(f"Prestamos activos:           {activos}")
    print(f"Porcentaje libros prestados: {porcentaje:.1f}%")
    return porcentaje


# MENU PRINCIPAL

def main():
    libros = cargar_libros()
    prestamos = cargar_prestamos()
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
            registrar_libro(libros)
        elif opcion == 2:
            mostrar_libros(libros)
        elif opcion == 3:
            buscar_libro(libros)
        elif opcion == 4:
            prestar_libro(libros, prestamos)
        elif opcion == 5:
            devolver_libro(libros, prestamos)
        elif opcion == 6:
            mostrar_prestamos(prestamos, libros)
        elif opcion == 7:
            reporte_general(libros, prestamos)
        elif opcion == 8:
            guardar_libros(libros)
            guardar_prestamos(prestamos)
            print("Datos guardados. Hasta pronto!")
        else:
            print("Opcion no valida: elija un numero del 1 al 8.")


main()