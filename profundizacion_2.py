# Bucles [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

'''
Enunciado:
Realice una calculadora:
Dentro de un bucle se debe ingresar por línea de comando dos números
Luego se ingresará como tercera entrada al programa el símbolo de la operación
que se desea ejecutar:
- Suma (+)
- Resta (-)
- Multiplicación (*)
- División (/)
- Exponente/Potencia (**)
Se debe efectuar el cálculo correcto según la operación ingresada por consola
Imprimir en pantalla la operación realizada y el resultado

El programa se debe repetir dentro del bucle hasta que como operador
se ingrese la palabra "FIN", en ese momento debe terminar el programa

Se debe debe imprimir un cartel de error si el operador ingresado no es
alguno de lo soportados o no es la palabra "FIN".
'''

print("Mi Calculadora (^_^)")
# Empezar aquí la resolución del ejercicio

while (True):
 numero_1 = float(input('Ingrese primer numero:'))
 numero_2 = float(input('Ingrese segundo numero:'))
 operacion = int(input('Ingrese operacion a realizar (1:+,2:-,3:*,4:/,5:**,6:FIN):'))
 if (operacion == 1):
    suma = numero_1 + numero_2
    print('La suma de', numero_1, 'y', numero_2, 'es:', suma)
 elif (operacion == 2):
    resta = numero_1 - numero_2
    print('La resta de', numero_1, 'y', numero_2, 'es:', resta)
 elif (operacion == 3):
    multiplicacion = numero_1 * numero_2
    print('La multiplicacion de', numero_1, 'y', numero_2, 'es:', multiplicacion)
 elif (operacion == 4):
    division = numero_1 / numero_2
    print('La division entre', numero_1, 'y', numero_2, 'es:', division)
 elif (operacion == 5):
    potencia = numero_1 ** numero_2
    print('La potencia de', numero_1, 'al', numero_2, 'es:', potencia)
 elif (operacion == 6):
    print('FIN')
    break    
 else:
    print('Opcion invalida')
print('Hasta pronto')
