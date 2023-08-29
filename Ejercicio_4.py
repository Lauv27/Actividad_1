# Entrada de datos, primero se pide la edad de juan, para de esta forma poder calcular la edad de Alberto, Ana y de esta forma se suma las 3 edades y nos da la edad de la mama.
EDJUAN = int(input("Ingrese la edad de Juan: "))  # con esta línea de código pedimos la edad de juan, el int es para que sea un número entero.
# Proceso, se realiza el proceso de calcular la edad de los dos hermanos de Juan y la mama.
EDALBER = int((2/3) * EDJUAN) # # En esta línea de código calculamos la edad de Alberto que tiene 2/3 de la edad de Juan.
EDANA = int((4/3) * EDJUAN)# En esta línea de código se calcula la edad de Ana que tiene 4/3 de la edad de Juan.
EDMAMA = int(EDJUAN + EDALBER + EDANA) # En esta línea de código calculamos la suma de la edad de los tres hermanos que nos da la edad de la mama.
# Salida de resultados, en las cuatro líneas de código se utiliza el print para mostrar cual es la edad de Juan, sus hermanos y su mama.
print("La edad de Juan es:", EDJUAN)
print("La edad de Alberto es:", EDALBER)
print("La edad de Ana es:", EDANA)
print("La edad de la mamá es:", EDMAMA)
