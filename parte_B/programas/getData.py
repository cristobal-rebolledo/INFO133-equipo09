import csv

# Datos que deseas escribir en el archivo CSV
datosPais = [
    ["Chile"],
    
]
datosRegion = [["Region de Tarapaca",1],["Region de Antofagasta",1],["Region de Atacama",1],["Region de Coquimbo",1],
["Region de Valparaiso",1],["Region del Libertador General Bernando O'Higgins",1],["Region del Maule",1],
["Region del Bio-bio",1],["Region de la Araucania",1],["Region de Los Lagos",1],["Region Aysen del General Carlos Ibanez del Campo",1],
["Region de Magallanes y Antartica Chilena",1],["Region Metropolitana de Santiago",1],["Region de Los Rios",1],
["Region de Arica y Parinacota",1],["Region de Nuble",1]]
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

with open(Region, 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(datosRegion)

print("Archivo CSV creado exitosamente.")