# Para este código lo hago general, que se pueda pedir cualquier número de horas de trabajo, cualquier tarifa de hora y cualquier retención en la fuente.
# En la siguiente línea de código se le solicita al usuario que ingrese las horas de trabajo.
horas_trabajadas = float(input("Ingrese el número de horas trabajadas: "))
# En la siguiente línea de código se le solicita al usuario que ingrese la tarifa por hora
tarifa_por_hora = float(input("Ingrese la tarifa por hora: "))
# En la siguiente línea de código se le solicita al usuario que ingrese el porcentaje de retención
porcentaje_retencion = float(input("Ingrese el porcentaje de retención (%): "))
# En la siguiente línea de código se hace el cálculo del salario bruto, el cual es las horas de trabajo multiplicado por la tarifa por hora.
salario_bruto = horas_trabajadas * tarifa_por_hora
# En la siguiente línea se hace el cálculo de la retención en la fuente, primero se divide el porcentaje de retención entre 100, para luego poder multiplicar por el salario bruto y de esta forma nos da la retención en la fuente.
retencion_fuente = (porcentaje_retencion / 100) * salario_bruto
# En la siguiente linea se hace el cálculo del salario neto, que es restar la retención en la fuente a el salario bruto.
salario_neto = salario_bruto - retencion_fuente
# En las siguientes 3 lineas se muestra la Impresión de los resultados.
print("Salario bruto:", salario_bruto)
print("Retención en la fuente:", retencion_fuente)
print("Salario neto:", salario_neto)
