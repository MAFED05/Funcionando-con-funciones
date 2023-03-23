#Importamos pi desde la libreria de Math
from math import pi
#Definimos todas las funciones que nos ayudarán a encontrar las respuestas que necesitamos
def calcularAreaEsfera(r1:float) -> float:
 areaEsfera= ((4*pi)*(r1**2))
 return areaEsfera

def calcularVolumenEsfera(r1:float)->float:
   volumenEsfera=((4/3)*(pi)*(r1**3))
   return volumenEsfera

def calcularAreaCono (r2:float, altura:float)->float:
    operacion=(((r2)**2)+((altura)**2))**0.5
    AreaCono=(pi*r2)*(pi+operacion)
    return AreaCono

def calcularVolumenCono(r2:float, altura:float)->float:
   volumenCono=((1/3)*(pi)*(r2**2))
   return volumenCono

#Definimos las demás funciones que necesitamos, haciendo uso de las funciones anteriormente definidas
def calcularAreaFigura (r1:float, r2:float, altura:float) -> float:
    AreaFigura= calcularAreaEsfera(r1) +calcularAreaCono(r2, altura)
    return AreaFigura 

def calcularVolumenFigura (r1:float, r2:float, altura:float) -> float:
 VolumenFigura=calcularVolumenCono(r2, altura) +calcularVolumenEsfera(r1)
 return VolumenFigura

#LLamamos la funcion principal, , definimos los valores que necesitamos, en este caso el área y el volumen
if __name__ == "__main__":
   #Colocamos los input
   r1 = float(input("Ingrese el radio de la esfera: "))
   r2= float(input("Ingrese el  radio del cono: "))
   altura= float(input("Ingrese la altura del cono: "))
   #definimos los valores que necesitamos, en este caso área y volumen
   area = calcularAreaFigura(r1, r2, altura) 
   volumen = calcularVolumenFigura(r1, r2, altura)
   #Imprimimos los resultados y redondeamos la respuesta
print("El area de la figura es "+ str(round(area,8))) 
print("El volumen de la figura es "+ str(round(volumen,8)))
