import csv

class Analizador:
    def __init__(self, ruta_csv):
        # Guardamos la ruta del archivo CSV
        self.ruta_csv = ruta_csv
        # Leemos el archivo CSV y guardamos los datos en memoria
        self.datos = self.leer_csv()

    def leer_csv(self):
        """Lee el archivo CSV y devuelve una lista de filas."""
        datos = []
        with open(self.ruta_csv, "r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo, delimiter='|')
            for fila in lector:
                # Validamos que existan las columnas necesarias
                if "PROVINCIA" in fila and "TOTAL_VENTAS" in fila:
                    datos.append(fila)
        return datos

    def ventas_totales_por_provincia(self):
        """
        Devuelve un diccionario con el total de ventas por provincia.
        Ejemplo: {'Pichincha': 1000.0, 'Guayas': 2000.5}
        """
        totales = {}

        # Recorremos todas las filas del archivo
        for fila in self.datos:
            provincia = fila["PROVINCIA"].upper()   # normalizamos
            try:
                total_venta = float(fila["TOTAL_VENTAS"])
            except ValueError:
                total_venta = 0.0  # Si no se puede convertir a float, asignamos 0.0

            # Sumamos las ventas por provincia
            totales[provincia] = totales.get(provincia, 0.0) + total_venta

        return totales

    def ventas_por_provincia(self, nombre):
        """
        Devuelve el total de ventas de una provincia específica.
        Lanza KeyError si la provincia no existe.
        """
        totales = self.ventas_totales_por_provincia()

        # Normalizamos el nombre ingresado por el usuario
        nombre_normalizado = nombre.upper()

        # Verificamos si la provincia existe
        if nombre_normalizado not in totales:
            raise KeyError(f"La provincia '{nombre}' no existe en el dataset.")

        return totales[nombre_normalizado]
