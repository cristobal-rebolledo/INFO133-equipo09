import codecs

output = codecs.open("planesYProgramas_Salida.csv","w","utf-8-sig")
with codecs.open("20230307_Planes_y_programas_de_estudios_2022_20220131_PUBL.csv","r","utf-8-sig") as file:
    file.readline() # Elimina la primera fila
    line = file.readline()
    nombresColegio = set()
    while (line):
        columnas = line.split(";")
        nombre = columnas[3]
        if(nombre not in nombresColegio):
            columnas_importantes = ";".join([columnas[3],columnas[10]])
            output.writelines(columnas_importantes)
            output.write("\n")
            nombresColegio.add(nombre)
        line = file.readline()
        
output.close()
print("Terminado!")