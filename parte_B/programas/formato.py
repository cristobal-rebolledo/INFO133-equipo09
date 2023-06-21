import unicodedata

def remove_accents(text):
    return ''.join(c for c in unicodedata.normalize('NFD', text) if unicodedata.category(c) != 'Mn')

def format_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    formatted_lines = []

    for line in lines:
        line = line.strip()
        line = remove_accents(line)
        line = line.lower()
        line = line.capitalize()
        formatted_lines.append(line)

    formatted_text = '\n'.join(formatted_lines)

    return formatted_text

# Ejemplo de uso
input_file = "../datos/infoPais.txt"
output_file = '../datos/infoPais.txt'

formatted_text = format_text(input_file)

with open(output_file, 'w', encoding='utf-8') as file:
    file.write(formatted_text)

print('Archivo procesado y guardado exitosamente.')