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
            #print(consulta)
            cursor.execute(consulta)

        conn.commit()

def importar_csv1(nombre_archivo, nombre_tabla,Nombre_Indicador):
    consulta = f"use bienestar;"
    cursor.execute(consulta)
    with open(nombre_archivo, 'r', encoding='utf-8-sig') as archivo:
        cabecera = archivo.readline().rstrip().split(";")
        columnas = ','.join(cabecera)
        print(columnas)
        print(cabecera)
        for linea in archivo:
            linea = linea.replace("'","")
            linea = linea.replace('"','')
            valores = ','.join([f"'{v.strip()}'" if isinstance(v, str) else str(v.strip()) for v in linea.rstrip().split(";")])
            valores = valores.rstrip("'")
            consulta = f"INSERT IGNORE INTO {nombre_tabla} ({columnas}FK_NOMBRE_INDICADOR) VALUES ({valores}'{Nombre_Indicador}');"
            print(consulta)
            cursor.execute(consulta)
        conn.commit()
def importar_csv2(nombre_archivo, nombre_tabla,Nombre_Indicador):
    consulta = f"use bienestar;"
    cursor.execute(consulta)
    with open(nombre_archivo, 'r', encoding='utf-8-sig') as archivo:
        cabecera = archivo.readline().rstrip().split(";")
        columnas = ','.join(cabecera)
        print(columnas)
        print(cabecera)
        for linea in archivo:
            linea = linea.replace("'","")
            linea =linea.replace('"','')
            valores = ','.join([f"'{v.strip()}'" if isinstance(v, str) else str(v.strip()) for v in linea.rstrip().split(";")])
            consulta = f"INSERT IGNORE INTO {nombre_tabla} ({columnas},FK_NOMBRE_INDICADOR) VALUES ({valores},'{Nombre_Indicador}');"
            print(consulta)
            cursor.execute(consulta)
        conn.commit()

# Ejemplo de importación para un archivo CSV y una tabla específica
#importar_csv("../datos/Pais.csv", "Pais")
#importar_csv("../datos/Region.csv", "Region")
#importar_csv("../datos/Comuna.csv","Comuna")
#importar_csv("../datos/Bienestar.csv","Bienestar")

#importar_csv2("../datos/Salud_salida.csv","CentrosMedicos","Cantidad de centros medicos")
#importar_csv1("../datos/DMCS_Tasa_Salida.csv","Tener")
#importar_csv1("../datos/estadios_Salida_SIN_TILDES.csv","Estadios","Cantidad de estadios")
importar_csv2("../datos/planesYProgramas_Salida.csv","Escuelas","Cantidad de establecimientos educativos")

conn.close()

