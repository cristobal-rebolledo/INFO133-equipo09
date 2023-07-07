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

# Crear cursor para ejecutar consultas
cursor = conn.cursor()


def sumaVar(nombre_var, filtro):
    consulta = filtro
    try:
        cursor.execute(consulta)
        resultados = cursor.fetchall()

        for fila in resultados:
        # Obtener el ID de la comuna
            id_comuna = fila[0]
            
            # Actualizar la variable y el total en bienestarCOmunal
            insertar = f"UPDATE BienestarComunal SET {nombre_var} = {nombre_var} + 1,  TOTAL = TOTAL +1 WHERE FK_ID_COMUNA = {id_comuna};"
            
            cursor.execute(insertar)

    except pymysql.Error as error:
        print("Error al ejecutar la consulta:", error)


consulta = f"use bienestar;"
cursor.execute(consulta)
# Consulta para filtrar las comunas con DMCS menor a la media
consulta = """
    SELECT * 
    FROM Comuna c 
    WHERE c.DMCS < (
        SELECT SUM(DMCS) / (SELECT COUNT(*) FROM Comuna) AS media 
        FROM Comuna
    )
"""

try:
    # Ejecutar consulta
    cursor.execute(consulta)
    
    # Obtener resultados
    resultados = cursor.fetchall()
    
    # Recorrer los resultados
    for fila in resultados:
        # Obtener el ID de la comuna
        id_comuna = fila[0]
        
        # Insertar el ID de la comuna en la tabla BienestarComunal
        insert_query = f"INSERT IGNORE INTO BienestarComunal (FK_ID_COMUNA) VALUES ({id_comuna})"
        cursor.execute(insert_query)
    
    # Confirmar los cambios en la base de datos
    
    #flitros para sumarle a la variable que tenga mas de la media
    sumaVar('var1',"select PK_ID_COMUNA, totalCentros/poblacion as centrosVsPoblacion from Comuna c join (Select FK_ID_COMUNA, count(*) as totalCentros  from CentrosMedicos cm group by FK_ID_COMUNA) c2 on c.PK_ID_COMUNA = c2.FK_ID_COMUNA having centrosVsPoblacion > (select count(*)/(select sum(c3.poblacion) from comuna c3) from CentrosMedicos) order by centrosVsPoblacion;")
    sumaVar('var2', "Select PK_ID_COMUNA, totalEstadios/poblacion as estadiosVsPoblacion from Comuna c join (Select FK_ID_COMUNA, count(*) as totalEstadios  from Estadios cm group by FK_ID_COMUNA) c2 on c.PK_ID_COMUNA = c2.FK_ID_COMUNA having estadiosVsPoblacion > (select count(*)/(select sum(c3.poblacion) from comuna c3) from Estadios) order by estadiosVsPoblacion;")
    sumaVar('var3',"Select PK_ID_COMUNA, totalEscuelas/poblacion as escuelasVsPoblacion from Comuna c join (Select FK_ID_COMUNA, count(*) as totalEscuelas  from Escuelas cm group by FK_ID_COMUNA) c2 on c.PK_ID_COMUNA = c2.FK_ID_COMUNA having escuelasVsPoblacion > (select count(*)/(select sum(c3.poblacion) from comuna c3) from Escuelas) order by escuelasVsPoblacion;")

    conn.commit()
except pymysql.Error as error:
    print("Error al ejecutar la consulta:", error)

finally:
    # Cerrar conexión y cursor
    cursor.close()
    conn.close()

