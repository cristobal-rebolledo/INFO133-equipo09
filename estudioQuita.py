import codecs

with codecs.open("Estudio.csv","r","utf-8") as file:
    output = ""
    lastLine = ""
    for line in file.readlines(): 
        if (line != lastLine):
            #print(line)
            line.replace(";",",")
            output+=line
            print(line)
        line.replace(";",",")
        lastLine = line
        print(line)

    with codecs.open("Estudio_salida.csv","w","utf-8") as newFile:
        newFile.write(output)