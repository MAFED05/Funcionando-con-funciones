#Le solicitamos al usuario que ingrese la cantidad de animales con los que haremos el cálculo
Gallinas = int(input("Ingrese la cantidad de gallinas: "))
Gallos = int(input("Ingrese la cantidad de gallos: "))
Pollitos = int(input("Ingrese la cantidad de pollitos: "))

#Realizamos la función, donde multiplicamos por animales por su peso y luego los sumamos
def calcularCarne (Gallinas, Gallos, Pollitos) :
    pesoGallinas = (6 * Gallinas)
    pesoGallos = ( 7 * Gallos)
    pesoPollitos = (1 * Pollitos)
    pesoTotal = pesoGallinas + pesoGallos + pesoPollitos
    return pesoTotal

#Le indicamos al programa que el peso total es igual al resultado de la función
pesoTotal = calcularCarne (Gallinas, Gallos, Pollitos)
#Imprimimos el resultado
print ("El peso total de todos los animales ingresados es de:", pesoTotal, "kilos")
