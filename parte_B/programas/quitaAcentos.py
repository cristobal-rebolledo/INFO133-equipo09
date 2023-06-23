import unicodedata
import codecs

def remove_accents(text):
    return ''.join(c for c in unicodedata.normalize('NFD', text) if unicodedata.category(c) != 'Mn')


file = codecs.open("path","r","utf-8")
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