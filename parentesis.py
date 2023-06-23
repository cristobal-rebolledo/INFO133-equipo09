import csv
import re

def eliminar_parentesis_archivo_csv(archivo_entrada, archivo_salida):
    with open(archivo_entrada, 'r', newline='') as archivo_lectura, open(archivo_salida, 'w', newline='') as archivo_escritura:
        lector_csv = csv.reader(archivo_lectura)
        escritor_csv = csv.writer(archivo_escritura)

        for fila in lector_csv:
            fila = [re.sub(r'\([^()]+\)', '', celda) for celda in fila]
            escritor_csv.writerow(fila)

    print("Las palabras entre paréntesis se han eliminado correctamente.")

# Ejemplo de uso:
archivo_entrada = 'estadios.csv'
archivo_salida = 'estadios_Salida.csv'
eliminar_parentesis_archivo_csv(archivo_entrada, archivo_salida)


