import sys
import pymysql
import csv

try:
    conn = pymysql.connect(
        user="root",
        password="Mandy",
        host="127.0.0.1",
        port=3306
    )

except pymysql.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)


cursor = conn.cursor()
def importar_csv(nombre_archivo, nombre_tabla):
    consulta = f"use bienestar;"
    cursor.execute(consulta)
    with open(nombre_archivo, 'r') as archivo:
        reader = csv.reader(archivo)
        cabecera = next(reader)  # Lee la primera línea como la cabecera de las columnas
        columnas = ','.join(cabecera)

        valores = ""
        #print(cabecera)
        #aqui se debe rellenar
        for linea in reader:
            #valores = ','.join(linea)
            valores = ','.join([f"'{v}'" if isinstance(v, str) else str(v) for v in linea])
            consulta = f"INSERT INTO {nombre_tabla} ({columnas}) VALUES ({valores});"
            #print(consulta)
            cursor.execute(consulta)

        conn.commit()

# Ejemplo de importación para un archivo CSV y una tabla específica
importar_csv("../datos/Pais.csv", "Pais")
importar_csv("../datos/Region.csv", "Region")

conn.close()

