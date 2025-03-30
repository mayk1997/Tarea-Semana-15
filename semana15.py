inf_personal = {
    "NOMBRE": "Maycon Caisaguano",
    "EDAD": 27,
    "CIUDAD": "Quito",
    "PROFESION": "Chofer"
}

# Accedemos y modificamos la clave que es ciudad en este caso
# Cambio de ciudad
inf_personal["CIUDAD"] = "Riobamba"

# Añadimos informacion adicional como clave si no tenemos una
if ("CELULAR") not in inf_personal:
    inf_personal["CELULAR"] = "+593 968 785 452"  # Número celular

#no definimos la edad porque no es informacion relevante
del inf_personal["EDAD"]

# Imprimimos el resultado
#diccionario
for clave, valor in inf_personal.items():
    print(f"{clave}:{valor}")