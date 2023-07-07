import sys
import pymysql
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

def escribe_archivo(c,ruta):
    consulta = f"use bienestar;"
    cursor.execute(consulta)
    consulta = c
    try:
        cursor.execute(consulta)
        resultados = cursor.fetchall()
        lineas = []
        for linea in resultados:
            lineas.append(f'{linea}\n')

        with open(ruta,"w") as file: file.writelines(lineas)

    except pymysql.Error as error:
        print("Error al ejecutar la consulta:", error)


        

# Ejemplo de importación para un archivo CSV y una tabla específica
c1="select * from bienestarComunal order by TOTAL DESC;"
c2 = "select c.NOMBRE_COMUNA, bc.total, c.poblacion from bienestarComunal bc join comuna c on bc.FK_ID_COMUNA=c.PK_ID_COMUNA where TOTAL = 3 order by c.poblacion DESC;"

escribe_archivo(c1,"../output/tablaBienstarComunal.txt")
escribe_archivo(c2,"../output/comunasSeleccionadas.txt")

conn.close()

