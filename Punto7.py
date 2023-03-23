#Importamos las funciones que realizamos en el punto 8
import OperacionesReto
#Llamamos la función principal
if __name__ == "__main__":
    n1 = float (input("Ingrese un número real: "))
    n2 = float (input("Ingrese un número real: "))
    n3 = float (input("Ingrese un número real: "))
    n4 = float (input("Ingrese un número real: "))
    n5 = float (input("Ingrese un número real: "))

    #Definimos todos los resultados que luego imprimiremos
    Promedio = OperacionesReto.promedio (n1,n2,n3,n4,n5)  #Es importante no olvidar los argumentos
    print ("El promedio de ", n1,n2,n3,n4,n5, "es:" , Promedio) #Imprimos el resultado

    PromedioMult = OperacionesReto.promedioMultiplicativo (n1,n2,n3,n4,n5)
    print ("El promedio multiplicativo de los números es de: ", PromedioMult)

    Mediana = OperacionesReto.calcularMediana (n1,n2,n3,n4,n5)
    print ( "La mediana de", n1,n2,n3,n4,n5, "es:", Mediana)

    Ascendente = OperacionesReto.ordenarAscendente (n1,n2,n3,n4,n5)
    print ("Números ordenados de forma ascendente:", Ascendente)

    Descendente = OperacionesReto.ordenarDescendente (n1,n2,n3,n4,n5)
    print ("Números ordenados de forma descente:", Descendente)

    Potencia = OperacionesReto.potenciaMayorMenor (n1,n2,n3,n4,n5)
    print ("La potencia del mayor número elevado al menor número es:", Potencia)

    Raíz = OperacionesReto.raizCubicaMenor (n1,n2,n3,n4,n5)
    print ("La raíz cúbica del menor número es: ", Raíz)
