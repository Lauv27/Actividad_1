# Primero se importa la libreria math la cual nos sirve para utilizar la funcion math.pi la cual sirve para utilizar el numero pi.
import math
# En la siguiente linea de tiempo se le pide al usuario ingresar el radio de un círculo.
radio = float(input("Ingrese el radio del círculo: "))
# En la siguiente linea se calcula el área del círculo usando la fórmula A = π * r^2
area = math.pi * (radio ** 2)
# En la siguiente linea se calcula la longitud de la circunferencia usando la fórmula C = 2πr
circunferencia = 2 * math.pi * radio
# En la siguiente linea se muestra los resultados del area y la circunferencia. 
print("El área del círculo es:", area)
print("La longitud de la circunferencia es:", circunferencia)
