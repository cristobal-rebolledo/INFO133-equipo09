import csv


# Datos que deseas escribir en el archivo CSV
datosPais = [["PK_NOMBRE_PAIS"],
    ["Chile"],
    
]
datosRegion = [["PK_NOMBRE_REGION","FK_NOMBRE_PAIS"],["Region de Tarapaca", "Chile"],["Region de Antofagasta", "Chile"],["Region de Atacama", "Chile"],["Region de Coquimbo", "Chile"],
["Region de Valparaiso", "Chile"],["region del libertador general bernardo ohiggins", "Chile"],["Region del Maule", "Chile"],
["Region del Bio Bio", "Chile"],["Region de la Araucania", "Chile"],["Region de Los Lagos", "Chile"],["Region de Aysen del General Carlos Ibanez del Campo", "Chile"],
["Region de Magallanes y de la Antartica Chilena", "Chile"],["Region Metropolitana de Santiago", "Chile"],["Region de Los Rios", "Chile"],
["Region de Arica y Parinacota", "Chile"],["Region de Nuble", "Chile"]]

datosComuna = [["PK_NOMBRE_COMUNA","FK_NOMBRE_REGION"],['Penaflor', 'region metropolitana de santiago'], ['Padre hurtado', 'region metropolitana de santiago'], ['Isla de maipo', 'region metropolitana de santiago'], ['El monte', 'region metropolitana de santiago'], ['Talagante', 'region metropolitana de santiago'], ['San pedro', 'region metropolitana de santiago'], ['Maria pinto', 'region metropolitana de santiago'], ['Curacavi', 'region metropolitana de santiago'], ['Alhue', 'region metropolitana de santiago'], ['Melipilla', 'region metropolitana de santiago'], ['Paine', 'region metropolitana de santiago'], ['Calera de tango', 'region metropolitana de santiago'], ['Buin', 'region metropolitana de santiago'], ['San bernardo', 'region metropolitana de santiago'], ['Til til', 'region metropolitana de santiago'], ['Lampa', 'region metropolitana de santiago'], ['Colina', 'region metropolitana de santiago'], ['San jose de maipo', 'region metropolitana de santiago'], ['Pirque', 'region metropolitana de santiago'], ['Puente alto', 'region metropolitana de santiago'], ['Vitacura', 'region metropolitana de santiago'], ['San ramon', 'region metropolitana de santiago'], ['San miguel', 'region metropolitana de santiago'], ['San joaquin', 'region metropolitana de santiago'], ['Renca', 'region metropolitana de santiago'], ['Recoleta', 'region metropolitana de santiago'], ['Quinta normal', 'region metropolitana de santiago'], ['Quilicura', 'region metropolitana de santiago'], ['Pudahuel', 'region metropolitana de santiago'], ['Providencia', 'region metropolitana de santiago'], ['Penalolen', 'region metropolitana de santiago'], ['Pedro aguirre cerda', 'region metropolitana de santiago'], ['Nunoa', 'region metropolitana de santiago'], ['Maipu', 'region metropolitana de santiago'], ['Macul', 'region metropolitana de santiago'], ['Lo prado', 'region metropolitana de santiago'], ['Lo espejo', 'region metropolitana de santiago'], ['Lo barnechea', 'region metropolitana de santiago'], ['Las condes', 'region metropolitana de santiago'], ['La reina', 'region metropolitana de santiago'], ['La pintana', 'region metropolitana de santiago'], ['La granja', 'region metropolitana de santiago'], ['La florida', 'region metropolitana de santiago'], ['La cisterna', 'region metropolitana de santiago'], ['Independencia', 'region metropolitana de santiago'], ['Huechuraba', 'region metropolitana de santiago'], ['Estacion central', 'region metropolitana de santiago'], ['El bosque', 'region metropolitana de santiago'], ['Conchali', 'region metropolitana de santiago'], ['Cerro navia', 'region metropolitana de santiago'], ['Cerrillos', 'region metropolitana de santiago'], ['Santiago', 'region metropolitana de santiago'], ['Torres del paine', 'region de magallanes y de la antartica chilena'], ['Natales', 'region de magallanes y de la antartica chilena'], ['Timaukel', 'region de magallanes y de la antartica chilena'], ['Primavera', 'region de magallanes y de la antartica chilena'], ['Porvenir', 'region de magallanes y de la antartica chilena'], ['Antartica', 'region de magallanes y de la antartica chilena'], ['Cabo de hornos', 'region de magallanes y de la antartica chilena'], ['San gregorio', 'region de magallanes y de la antartica chilena'], ['Rio verde', 'region de magallanes y de la antartica chilena'], ['Laguna blanca', 'region de magallanes y de la antartica chilena'], ['Punta arenas', 'region de magallanes y de la antartica chilena'], ['Rio ibanez', 'region de aysen del general carlos ibanez del campo'], ['Chile chico', 'region de aysen del general carlos ibanez del campo'], ['Tortel', 'region de aysen del general carlos ibanez del campo'], ["Ohiggins", 'region de aysen del general carlos ibanez del campo'], ['Coyhaique / coihaique', 'region de aysen del general carlos ibanez del campo'], ['Cochrane', 'region de aysen del general carlos ibanez del campo'], ['Guaitecas', 'region de aysen del general carlos ibanez del campo'], ['Cisnes', 'region de aysen del general carlos ibanez del campo'], ['Aysen / aisen', 'region de aysen del general carlos ibanez del campo'], ['Lago verde', 'region de aysen del general carlos ibanez del campo'], ['Palena', 'region de los lagos'], ['Hualaihue', 'region de los lagos'], ['Futaleufu', 'region de los lagos'], ['Chaiten', 'region de los lagos'], ['San pablo', 'region de los lagos'], ['San juan de la costa', 'region de los lagos'], ['Rio negro', 'region de los lagos'], ['Puyehue', 'region de los lagos'], ['Purranque', 'region de los lagos'], ['Puerto octay', 'region de los lagos'], ['Osorno', 'region de los lagos'], ['Quinchao', 'region de los lagos'], ['Quemchi', 'region de los lagos'], ['Quellon', 'region de los lagos'], ['Queilen', 'region de los lagos'], ['Puqueldon', 'region de los lagos'], ['Dalcahue', 'region de los lagos'], ['Curaco de velez', 'region de los lagos'], ['Chonchi', 'region de los lagos'], ['Ancud', 'region de los lagos'], ['Castro', 'region de los lagos'], ['Puerto varas', 'region de los lagos'], ['Maullin', 'region de los lagos'], ['Llanquihue', 'region de los lagos'], ['Los muermos', 'region de los lagos'], ['Frutillar', 'region de los lagos'], ['Fresia', 'region de los lagos'], ['Cochamo', 'region de los lagos'], ['Calbuco', 'region de los lagos'], ['Puerto montt', 'region de los lagos'], ['Rio bueno', 'region de los rios'], ['Lago ranco', 'region de los rios'], ['Futrono', 'region de los rios'], ['La union', 'region de los rios'], ['Panguipulli', 'region de los rios'], ['Paillaco', 'region de los rios'], ['Mariquina', 'region de los rios'], ['Mafil', 'region de los rios'], ['Los lagos', 'region de los rios'], ['Lanco', 'region de los rios'], ['Corral', 'region de los rios'], ['Valdivia', 'region de los rios'], ['Victoria', 'region de la araucania'], ['Traiguen', 'region de la araucania'], ['Renaico', 'region de la araucania'], ['Puren', 'region de la araucania'], ['Lumaco', 'region de la araucania'], ['Los sauces', 'region de la araucania'], ['Lonquimay', 'region de la araucania'], ['Curacautin', 'region de la araucania'], ['Collipulli', 'region de la araucania'], ['Ercilla', 'region de la araucania'], ['Angol', 'region de la araucania'], ['Cholchol', 'region de la araucania'], ['Villarrica', 'region de la araucania'], ['Vilcun', 'region de la araucania'], ['Tolten', 'region de la araucania'], ['Teodoro schmidt', 'region de la araucania'], ['Saavedra', 'region de la araucania'], ['Pucon', 'region de la araucania'], ['Pitrufquen', 'region de la araucania'], ['Perquenco', 'region de la araucania'], ['Padre las casas', 'region de la araucania'], ['Nueva imperial', 'region de la araucania'], ['Melipeuco', 'region de la araucania'], ['Loncoche', 'region de la araucania'], ['Lautaro', 'region de la araucania'], ['Gorbea', 'region de la araucania'], ['Galvarino', 'region de la araucania'], ['Freire', 'region de la araucania'], ['Curarrehue', 'region de la araucania'], ['Cunco', 'region de la araucania'], ['Carahue', 'region de la araucania'], ['Temuco', 'region de la araucania'], ['Alto bio bio', 'region del bio bio'], ['Yumbel', 'region del bio bio'], ['Tucapel', 'region del bio bio'], ['Santa barbara', 'region del bio bio'], ['San rosendo', 'region del bio bio'], ['Quilleco', 'region del bio bio'], ['Quilaco', 'region del bio bio'], ['Negrete', 'region del bio bio'], ['Nacimiento', 'region del bio bio'], ['Mulchen', 'region del bio bio'], ['Laja', 'region del bio bio'], ['Cabrero', 'region del bio bio'], ['Antuco', 'region del bio bio'], ['Los angeles', 'region del bio bio'], ['Tirua', 'region del bio bio'], ['Los alamos', 'region del bio bio'], ['Curanilahue', 'region del bio bio'], ['Contulmo', 'region del bio bio'], ['Canete', 'region del bio bio'], ['Arauco', 'region del bio bio'], ['Lebu', 'region del bio bio'], ['Hualpen', 'region del bio bio'], ['Tome', 'region del bio bio'], ['Talcahuano', 'region del bio bio'], ['Santa juana', 'region del bio bio'], ['San pedro de la paz', 'region del bio bio'], ['Penco', 'region del bio bio'], ['Lota', 'region del bio bio'], ['Hualqui', 'region del bio bio'], ['Florida', 'region del bio bio'], ['Chiguayante', 'region del bio bio'], ['Coronel', 'region del bio bio'], ['Concepcion', 'region del bio bio'], ['Yungay', 'region de nuble'], ['Treguaco / trehuaco', 'region de nuble'], ['San nicolas', 'region de nuble'], ['San ignacio', 'region de nuble'], ['San fabian', 'region de nuble'], ['San carlos', 'region de nuble'], ['Ranquil', 'region de nuble'], ['Quirihue', 'region de nuble'], ['Quillon', 'region de nuble'], ['Portezuelo', 'region de nuble'], ['Pinto', 'region de nuble'], ['Pemuco', 'region de nuble'], ['Niquen', 'region de nuble'], ['Ninhue', 'region de nuble'], ['El carmen', 'region de nuble'], ['Chillan viejo', 'region de nuble'], ['Coihueco', 'region de nuble'], ['Coelemu', 'region de nuble'], ['Cobquecura', 'region de nuble'], ['Bulnes', 'region de nuble'], ['Chillan', 'region de nuble'], ['Yerbas buenas', 'region del maule'], ['Villa alegre', 'region del maule'], ['San javier', 'region del maule'], ['Retiro', 'region del maule'], ['Parral', 'region del maule'], ['Longavi', 'region del maule'], ['Colbun', 'region del maule'], ['Linares', 'region del maule'], ['Vichuquen', 'region del maule'], ['Teno', 'region del maule'], ['Sagrada familia', 'region del maule'], ['Romeral', 'region del maule'], ['Rauco', 'region del maule'], ['Molina', 'region del maule'], ['Licanten', 'region del maule'], ['Hualane', 'region del maule'], ['Curico', 'region del maule'], ['Pelluhue', 'region del maule'], ['Chanco', 'region del maule'], ['Cauquenes', 'region del maule'], ['San rafael', 'region del maule'], ['San clemente', 'region del maule'], ['Rio claro', 'region del maule'], ['Pencahue', 'region del maule'], ['Pelarco', 'region del maule'], ['Maule', 'region del maule'], ['Empedrado', 'region del maule'], ['Curepto', 'region del maule'], ['Constitucion', 'region del maule'], ['Talca', 'region del maule'], ['Santa cruz', "region del libertador general bernardo ohiggins"], ['Pumanque', "region del libertador general bernardo ohiggins"], ['Placilla', "region del libertador general bernardo ohiggins"], ['Peralillo', "region del libertador general bernardo ohiggins"], ['Palmilla', "region del libertador general bernardo ohiggins"], ['Nancagua', "region del libertador general bernardo ohiggins"], ['Lolol', "region del libertador general bernardo ohiggins"], ['Chimbarongo', "region del libertador general bernardo ohiggins"], ['San fernando', "region del libertador general bernardo ohiggins"], ['Chepica', "region del libertador general bernardo ohiggins"], ['Paredones', "region del libertador general bernardo ohiggins"], ['Navidad', "region del libertador general bernardo ohiggins"], ['Marchihue', "region del libertador general bernardo ohiggins"], ['Litueche', "region del libertador general bernardo ohiggins"], ['La estrella', "region del libertador general bernardo ohiggins"], ['Pichilemu', "region del libertador general bernardo ohiggins"], ['San vicente', "region del libertador general bernardo ohiggins"], ['Rengo', "region del libertador general bernardo ohiggins"], ['Requinoa', "region del libertador general bernardo ohiggins"], ['Quinta de tilcoco', "region del libertador general bernardo ohiggins"], ['Pichidegua', "region del libertador general bernardo ohiggins"], ['Peumo', "region del libertador general bernardo ohiggins"], ['Olivar', "region del libertador general bernardo ohiggins"], ['Mostazal', "region del libertador general bernardo ohiggins"], ['Malloa', "region del libertador general bernardo ohiggins"], ['Machali', "region del libertador general bernardo ohiggins"], ['Las cabras', "region del libertador general bernardo ohiggins"], ['Graneros', "region del libertador general bernardo ohiggins"], ['Donihue', "region del libertador general bernardo ohiggins"], ['Coltauco', "region del libertador general bernardo ohiggins"], ['Coinco', "region del libertador general bernardo ohiggins"], ['Codegua', "region del libertador general bernardo ohiggins"], ['Rancagua', "region del libertador general bernardo ohiggins"], ['Olmue', 'region de valparaiso'], ['Quilpue', 'region de valparaiso'], ['Villa alemana', 'region de valparaiso'], ['Limache', 'region de valparaiso'], ['Santa maria', 'region de valparaiso'], ['Putaendo', 'region de valparaiso'], ['Panquehue', 'region de valparaiso'], ['Catemu', 'region de valparaiso'], ['Llaillay / llayllay', 'region de valparaiso'], ['San felipe', 'region de valparaiso'], ['Santo domingo', 'region de valparaiso'], ['El tabo', 'region de valparaiso'], ['El quisco', 'region de valparaiso'], ['Cartagena', 'region de valparaiso'], ['Algarrobo', 'region de valparaiso'], ['San antonio', 'region de valparaiso'], ['Nogales', 'region de valparaiso'], ['La cruz', 'region de valparaiso'], ['Hijuelas', 'region de valparaiso'], ['La calera', 'region de valparaiso'], ['Quillota', 'region de valparaiso'], ['Zapallar', 'region de valparaiso'], ['Petorca', 'region de valparaiso'], ['Papudo', 'region de valparaiso'], ['Cabildo', 'region de valparaiso'], ['La ligua', 'region de valparaiso'], ['San esteban', 'region de valparaiso'], ['Rinconada', 'region de valparaiso'], ['Calle larga', 'region de valparaiso'], ['Los andes', 'region de valparaiso'], ['Isla de pascua', 'region de valparaiso'], ['Vina del mar', 'region de valparaiso'], ['Quintero', 'region de valparaiso'], ['Puchuncavi', 'region de valparaiso'], ['Isla juan fernandez', 'region de valparaiso'], ['Concon', 'region de valparaiso'], ['Casablanca', 'region de valparaiso'], ['Valparaiso', 'region de valparaiso'], ['Rio hurtado', 'region de coquimbo'], ['Punitaqui', 'region de coquimbo'], ['Monte patria', 'region de coquimbo'], ['Combarbala', 'region de coquimbo'], ['Ovalle', 'region de coquimbo'], ['Los vilos', 'region de coquimbo'], ['Salamanca', 'region de coquimbo'], ['Canela', 'region de coquimbo'], ['Illapel', 'region de coquimbo'], ['Vicuna', 'region de coquimbo'], ['Paihuano', 'region de coquimbo'], ['La higuera', 'region de coquimbo'], ['Andacollo', 'region de coquimbo'], ['Coquimbo', 'region de coquimbo'], ['La serena', 'region de coquimbo'], ['Huasco', 'region de atacama'], ['Freirina', 'region de atacama'], ['Alto del carmen', 'region de atacama'], ['Chanaral', 'region de atacama'], ['Tierra amarilla', 'region de atacama'], ['Vallenar', 'region de atacama'], ['Diego de almagro', 'region de atacama'], ['Caldera', 'region de atacama'], ['Copiapo', 'region de atacama'], ['San pedro de atacama', 'region de antofagasta'], ['Sierra gorda', 'region de antofagasta'], ['Mejillones', 'region de antofagasta'], ['Maria elena', 'region de antofagasta'], ['Tocopilla', 'region de antofagasta'], ['Ollague', 'region de antofagasta'], ['Calama', 'region de antofagasta'], ['Taltal', 'region de antofagasta'], ['Antofagasta', 'region de antofagasta'], ['Pica', 'region de tarapaca'], ['Huara', 'region de tarapaca'], ['Colchane', 'region de tarapaca'], ['Camina', 'region de tarapaca'], ['Pozo almonte', 'region de tarapaca'], ['Iquique', 'region de tarapaca'], ['Alto hospicio', 'region de tarapaca'], ['Arica', 'region de arica y parinacota'], ['General lagos', 'region de arica y parinacota'], ['Putre', 'region de arica y parinacota'], ['Camarones', 'region de arica y parinacota']]

datosTener = [["Valor","FK_NOMBRE_COMUNA","FK_NOMBRE_INDICADOR"]]

datosBienestar = [["PK_NOMBRE_INDICADOR","Descripcion","Categoria"],
                ["Cantidad de Establecimientos Educativos","Esta variable mide la cantidad de establecimientos educacionales por comuna","Educacion"],
                ["Cantidad de Centros Medicos","Esta variable mide la cantidad de centros medicos por comuna","Salud"],
                ["Tasa de DMCS","Permite acceder a un reporte estadístico por comuna de los Delitos de Mayor Connotación Social (DMCS), como: homicidio, lesiones, violación, robo con fuerza y robo con violencia, por cada 100 mil habitantes","Seguridad"],
                ["Cantidad de Estadios","Esta variable mide la cantidad de estadios por comuna","Entretencion"]]

#aqui se deben conseguir los datos del bienestar de los sitios web 

# Ruta y nombre del archivo CSV
Pais = "../datos/Pais.csv"
Region = "../datos/Region.csv"
Comuna = "../datos/Comuna.csv"
Tener = "../datos/Tener.csv"
Bienestar = "../datos/Bienestar.csv"


# Escribir los datos en el archivo CSV
with open(Pais, 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(datosPais)

with open(Region, 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(datosRegion)

with open(Comuna, 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(datosComuna)

with open(Bienestar, 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(datosBienestar)

print("Archivo CSV creado exitosamente.")



