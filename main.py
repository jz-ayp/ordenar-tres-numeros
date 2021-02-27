"""
Inserta el encabezado aquí y escribe tu código abajo


# Declaraciones
CONSTANTE = valor

# Entradas
entrada = input()

# Proceso


# Salidas
print(salida)
"""

"""
Ordenar tres números de mayor a menor 
"""

# Entradas
a =	eval(input("Introduzca el primer número: "))
b = eval(input("Introduzca el segundo número: "))
c = eval(input("Introduzca el tercer número: "))
	
# Proceso
# Primero se acomodan los dos primeros 
# y luego se coloca el tercero en su lugar
if a >= b:
	mayor = a
	menor = b
else:
	mayor = b
	menor = a

# Ahora acomodar c en su lugar
if c >= mayor:
	medio = mayor
	mayor = c
elif c <= menor:
	medio = menor
	menor = c
else:
	medio = c

# Salidas
print("Los números en orden de mayor a menor son:",)
print(mayor, medio, menor)
