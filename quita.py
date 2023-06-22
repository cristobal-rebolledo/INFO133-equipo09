import unicodedata
import codecs

def remove_accents(text):
    return ''.join(c for c in unicodedata.normalize('NFD', text) if unicodedata.category(c) != 'Mn')

file = codecs.open("DMCStasa.csv","r","utf-8-sig")
text = "".join(file.readlines())
output = codecs.open("DMCS_Tasa_Salida.csv","w","utf-8-sig")
output.write(remove_accents(text))
file.close()
output.close()