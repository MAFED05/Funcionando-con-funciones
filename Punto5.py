#Le solicitamos al usuario que ingrese los datos con los que vamos a realizar la operación
Capital = float(input("Introduce el monto del préstamo: "))
interes = float(input("Introduce la tasa de interés en porcentaje: "))
tiempo = int(input("Introduce el número de meses: "))

#Definimos la función denotando la prioridad de la operación
def valorFinalPrestamo(Capital, interes, tiempo):
    valorFinal = Capital * (1 + (interes/100)) ** tiempo
    return valorFinal

#Le decimos al programa que el valor final es igual a la función previamente realizada
valorFinal = valorFinalPrestamo(Capital, interes, tiempo)

#Imprimimos el resultado final
print("El valor del préstamo después de", tiempo, "meses es:", round(valorFinal, 3))