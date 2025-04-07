# Despues de crear el archivo de texto
# Llamamos a las notas
with open('notas_personales.txt', 'w') as file:
    file.write("Nota 1: Estudiar para el examen de ingles.\n")
    file.write("Nota 2: Estudiar el conversacion.\n")
    file.write("Nota 3: Estudiar gramatica.\n")
    file.write("Nota 4: Dare el examen despues de lo aprendido.\n")

# Abrimos el archivo de texto en modo lectura "r"
with open('notas_personales.txt', 'r') as file:
    for line in file:
        print(line.strip())

#el ciclo se cierra en with imprimiento la nota de texto ya mostrada
# sin generan un bucle