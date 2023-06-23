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
        print(cabecera)
        #aqui se debe rellenar
        for linea in reader:
            #valores = ','.join(linea)
            valores = ','.join([f"'{v}'" if isinstance(v, str) else str(v) for v in linea])
            consulta = f"INSERT INTO {nombre_tabla} ({columnas}) VALUES ({valores});"
            print(consulta)
            cursor.execute(consulta)

        conn.commit()

def importar_csv1(nombre_archivo, nombre_tabla,Nombre_Indicador):
    #consulta = f"use bienestar;"
    #cursor.execute(consulta)
    with open(nombre_archivo, 'r') as archivo:
        cabecera = archivo.readline().rstrip().split(";")
        columnas = ','.join(cabecera)
        print(columnas)
        print(cabecera)
        for linea in archivo:
            valores = ','.join([f"'{v.strip()}'" if isinstance(v, str) else str(v.strip()) for v in linea.rstrip().split(";")])
            consulta = f"INSERT INTO {nombre_tabla} ({columnas}) VALUES ({valores});"
            print(consulta)

# Ejemplo de importación para un archivo CSV y una tabla específica
#importar_csv("../datos/Pais.csv", "Pais")
#importar_csv("../datos/Region.csv", "Region")
#importar_csv("../datos/Comuna.csv","Comuna")
#importar_csv("../datos/Bienestar.csv","Bienestar")
importar_csv1("../datos/Estudio_salida.csv","Escuelas","Educacion")
importar_csv1("../datos/Salud_salida.csv","CentrosMedicos","Salud")
#importar_csv1("../datos/DMCS_Tasa_Salida.csv","Tener")
importar_csv1("../datos/estadios_Salida_SIN_TILDES.csv","Estadios","Entretencion")

conn.close()

