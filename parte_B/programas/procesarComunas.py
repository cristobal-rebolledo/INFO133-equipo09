#output = open("infoComunasOutputArray","w")
import os
import codecs

outputFile = codecs.open("../datos/comunasProcesadas.txt","w","utf-8")
with codecs.open("infoPais.txt","r","utf-8") as file:
#    output.write("[")
    lines = file.readlines()
    outputLines = []
    for line in lines:
        outputLines.append(line.strip().split("	"))
    outputFile.write(str(outputLines))


outputFile.close()