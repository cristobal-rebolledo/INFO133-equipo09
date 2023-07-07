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

        
def importar_comunas_region_csv(nombre_archivo):
    consulta = f"use bienestar;"
    cursor.execute(consulta)
    # Leer los datos desde el archivo de texto
    with open(nombre_archivo, 'r', encoding='utf-8-sig') as archivo:
        consulta_pais = f"INSERT IGNORE INTO Pais(PK_ID_PAIS, Nombre_Pais) VALUES (1,'Chile');"
        cursor.execute(consulta_pais)
        for linea in archivo:
            linea = linea.replace("'","")
            linea =linea.replace('"','')
            datos = linea.rstrip().split(",")

            # Insertar en la tabla Region
            id_region = int(datos[1])
            nombre_region = datos[0]
            consulta_region = f"INSERT IGNORE INTO Region (Nombre_Region, PK_ID_Region,FK_ID_PAIS) VALUES ('{nombre_region}', {id_region},1);"
            cursor.execute(consulta_region)

            # Insertar en la tabla Comuna
            id_comuna = int(datos[3])
            nombre_comuna = datos[2]
            poblacion = int(datos[4])
            id_region_comuna = int(datos[1])
            consulta_comuna = f"INSERT IGNORE INTO Comuna (PK_ID_Comuna, Nombre_Comuna, Poblacion, FK_ID_Region) VALUES ({id_comuna}, '{nombre_comuna}', {poblacion}, {id_region_comuna});"
            cursor.execute(consulta_comuna)

    # Confirmar los cambios y cerrar la conexión
    conn.commit()

def importar_DMSC(nombre_archivo):
    consulta = f"use bienestar;"
    cursor.execute(consulta)
    with open(nombre_archivo, 'r', encoding='utf-8-sig') as archivo:
        for linea in archivo:
            linea = linea.replace("'","")
            linea =linea.replace('"','')
            datos = linea.rstrip().split(",")

            nombre_comuna = datos[0]
            valor_dmcd = float(datos[1])

                # Actualizar el valor de DMCD en la tabla Comuna
            consulta_actualizar = f"UPDATE Comuna SET DMCS = {valor_dmcd} WHERE Nombre_Comuna = '{nombre_comuna}'"
            cursor.execute(consulta_actualizar)
    # Confirmar los cambios y cerrar la conexión
    conn.commit()

def obtener_id_comuna(nombre_comuna):
    # Consulta para obtener el ID de la comuna
    consulta = f"SELECT PK_ID_Comuna FROM Comuna WHERE Nombre_Comuna LIKE '{nombre_comuna}'"
    cursor.execute(consulta)
    
    # Obtener el primer resultado de la consulta
    resultado = cursor.fetchone()
    
    if resultado:
        # Obtener el ID de la comuna
        id_comuna = resultado[0]
        return id_comuna
    else:
        return None

def importar_indicadores(nombre_archivo,nombre_tabla):
    consulta = f"use bienestar;"
    cursor.execute(consulta)
    with open(nombre_archivo, 'r', encoding='utf-8-sig') as archivo:
        
        cabecera = archivo.readline().rstrip().split(";")
        columnas = ','.join(cabecera)
        #print(columnas)
        #print(cabecera)
        for linea in archivo:
            linea = linea.replace("'","")
            linea =linea.replace('"','')
            datos = linea.strip().split(';')
            nombre_centro = datos[0]
            nombre_comuna = datos[1]
    
            # Obtener el ID de la comuna
            id_comuna = obtener_id_comuna(nombre_comuna)
                
            if id_comuna:
                # Insertar los datos en la tabla nombre_tabla
                consulta = f"INSERT INTO {nombre_tabla} ({columnas}) VALUES ('{nombre_centro}', {id_comuna})"
                cursor.execute(consulta)
                conn.commit()

def importar_escuelas(nombre_archivo,nombre_tabla):
    consulta = f"use bienestar;"
    cursor.execute(consulta)
    with open(nombre_archivo, 'r', encoding='utf-8-sig') as archivo:
        
        cabecera = archivo.readline().rstrip().split(";")
        columnas = ','.join(cabecera)
        #print(columnas)
        #print(cabecera)
        for linea in archivo:
            linea = linea.replace("'","")
            linea =linea.replace('"','')
            datos = linea.strip().split(';')
            nombre_centro = datos[0]
            id_comuna = datos[1]
                
            
            # Insertar los datos en la tabla nombre_tabla
            consulta = f"INSERT INTO {nombre_tabla} ({columnas}) VALUES ('{nombre_centro}', {id_comuna})"
            cursor.execute(consulta)
            conn.commit()
# Ejemplo de importación para un archivo CSV y una tabla específica

importar_comunas_region_csv("../datos/datosComunas.csv")

importar_DMSC("../datos/DMCS_Tasa_Salida.csv")




importar_indicadores("../datos/Salud_salida.csv","CentrosMedicos")
importar_indicadores("../datos/estadios_Salida_SIN_TILDES.csv","Estadios")
importar_escuelas("../datos/planesYProgramas_Salida.csv","Escuelas")

conn.close()

