import csv

# Datos que deseas escribir en el archivo CSV
datosPais = [
    ["Chile","1"],
    
]
datosRegion = []
datosComuna = []
datosTener = []
datosBienestar = []

#aqui se deben conseguir los datos del bienestar de los sitios web 

# Ruta y nombre del archivo CSV
Pais = 'INFO133-equipo09\parte_B\datos\Pais.csv'
Region = 'INFO133-equipo09\parte_B\datos\Region.csv'
Comuna = 'INFO133-equipo09\parte_B\datos\Comuna.csv'
Tener = 'INFO133-equipo09\parte_B\datos\Tener.csv'
Bienestar = 'INFO133-equipo09\parte_B\datos\Bienestar.csv'

# Escribir los datos en el archivo CSV
with open(Pais, 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(datosPais)

print("Archivo CSV creado exitosamente.")