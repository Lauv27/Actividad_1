# El siguiente código es un código general para cualquier valor X y Y que ingrese el usuario. 
SUMA = 0 # Primero se define la variable SUMA y esta inicia en 0.
X = float(input("Ingrese el valor de X: ")) # Se le solicita al usuario ingrese el valor de X.
# En la siguiente línea de código se realiza la operación SUMA = SUMA + X, la cual asigna un nuevo valor de la variable SUMA, sumándole el valor que se ingresó de X a el anterior valor de la variable SUMA.
SUMA = SUMA + X
Y = float(input("Ingrese el valor de Y: ")) # Se le solicita al usuario ingresar el valor de Y.
# En la siguiente línea de código se realiza la operación X = X + Y ** 2, donde se asigna un nuevo valor a la variable X, donde al anterior valor X que ingreso el usuario se le suma el valor del cuadrado de Y.
X = X + Y ** 2
# En la siguiente línea de código se realiza la operación SUMA = SUMA + X / Y, donde se le asigna un nuevo valor a la variable SUMA, este nuevo valor se da sumándole a el anterior valor de SUMA la división del nuevo valor de la variable X entre Y. 
SUMA = SUMA + X / Y
# En la siguiente línea de código se muestra el resultado final de la variable SUMA. 
print("EL VALOR DE LA SUMA ES:", SUMA)
