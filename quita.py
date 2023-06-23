import unicodedata
import codecs

def remove_accents(text):
    return ''.join(c for c in unicodedata.normalize('NFD', text) if unicodedata.category(c) != 'Mn').replace('"',"").replace("'","")

file = codecs.open("estadios_Salida.csv","r","utf-8-sig")
text = "".join(file.readlines())
output = codecs.open("estadios_Salida_SIN_TILDES.csv","w","utf-8-sig")
output.write(remove_accents(text))
file.close()
output.close()