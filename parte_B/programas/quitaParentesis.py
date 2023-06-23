import csv

def procesar_csv(archivo_entrada, archivo_salida):
    with open(archivo_entrada, 'r') as f_input, open(archivo_salida, 'w', newline='') as f_output:
        reader = csv.reader(f_input, delimiter=';')
        writer = csv.writer(f_output, delimiter=';')

        for i, row in enumerate(reader):
            if i == 1:
                # Procesar línea 2 eliminando contenido entre paréntesis
                for j, valor in enumerate(row):
                    indice_parentesis_inicio = valor.find('(')
                    indice_parentesis_fin = valor.find(')')

                    if indice_parentesis_inicio != -1 and indice_parentesis_fin != -1:
                        valor = valor[:indice_parentesis_inicio] + valor[indice_parentesis_fin + 1:]
                        valor = valor.strip()

                    row[j] = valor
            writer.writerow(row)

    print("Archivo procesado correctamente.")

# Ejemplo de uso
archivo_entrada = 'entrada.csv'
archivo_salida = 'salida.csv'

procesar_csv(archivo_entrada, archivo_salida)