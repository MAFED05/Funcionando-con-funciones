#Importamos pi desde la libreria math
from math import pi

#Definimos las funciones que vamos a utilizar para hallar los datos que necesitamos
def calcularAreaCírculo(r:float)->float:
   areaCírculo=((pi)*(r**2))
   return areaCírculo

def calcularAreaRectángulo (base:float, altura:float)->float:
   areaRectángulo=base*altura
   return areaRectángulo

def calcularPerímetroRectángulo (base:float, altura:float)->float:
   perímetroRectángulo=(base*2)+(altura*2)
   return perímetroRectángulo

def calcularPerímetroCírculo (r:float)->float:
   perímetroCírculo=(2*pi*r)
   return perímetroCírculo

#Definimos las siguentes funciones haciendo uso de las anteriormente realizadas
def calcularAreaFigura (altura:float, base:float, r:float)->float:
 areaFigura= (calcularAreaCírculo(r)*2)  + calcularAreaRectángulo(base, altura)
 return areaFigura
def calcularPerimetroFigura (altura:float, base:float, radio:float)->float:
 perimetroFigura= (calcularPerímetroCírculo(r)*2) + calcularPerímetroRectángulo(base, altura)
 return perimetroFigura

#Llamamos la función principal
if __name__=="__main__":
    #Colocamos todos los input
    altura = float(input("Ingrese la altura: "))
    base = float(input("Ingrese la base: "))
    r = float(input("Ingrese el radio: " ))
    #Definimos los resultados
    Área= calcularAreaFigura(altura, base, r)
    Perímetro= calcularPerimetroFigura(altura, base, r)
    #Imprimimos los resultados redondeando su respuesta a 6 decimales
    print ("El perimetro de la figura es "+ str(round(Perímetro,6)))
    print ("El area de la figura es "+ str(round(Área,6)))
