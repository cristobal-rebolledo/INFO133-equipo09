import unicodedata
import codecs

def remove_accents(text):
    return ''.join(c for c in unicodedata.normalize('NFD', text) if unicodedata.category(c) != 'Mn')

file = codecs.open("Salud.csv","r","utf-8")
text = "".join(file.readlines())
output = open("Salud_salida.csv","w")
output.write(remove_accents(text))
file.close()
output.close()