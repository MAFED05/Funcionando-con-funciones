#Le solicitamos al usuario que ingrese los datos con los cuales realizaremos el cálculo
Dias = int(input("Ingrese la cantidad de días a partir de hoy: "))
Contagiados = int (input("Ingrese la cantidad de contagiados actuales: "))

#Definimos la función 
def calcularContagiados (Dias, Contagiados):
    totalContagiados = Contagiados * (2 ** Dias)
    return totalContagiados

#Le indicamos al programa que la cantidad de contagios es igual al resultado de la función
totalContagios = calcularContagiados (Dias, Contagiados)

#Imprimimos el resultado
print ("El número de personas contagiadas en ", Dias , " días será de:",  totalContagios)
