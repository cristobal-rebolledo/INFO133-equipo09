#output = open("infoComunasOutputArray","w")
import os
import codecs
import unicodedata
def remove_accents(text):
    return ''.join(c for c in unicodedata.normalize('NFD', text) if unicodedata.category(c) != 'Mn')

outputFile = codecs.open("../datos/comunasProcesadas.txt","w","utf-8")
with codecs.open("../datos/infoPais.txt","r","utf-8") as file:
#    output.write("[")
    lines = file.readlines()
    outputLines = []
    for line in lines:
        line = line.strip()
        line = remove_accents(line)
        line = line.lower()
        line = line.capitalize()
        outputLines.append(line.split("	"))
    outputFile.write(str(outputLines))


outputFile.close()