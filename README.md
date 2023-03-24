# Funcionando con funciones

Buen día, el día de hoy les mostraré como desarrollé los puntos del reto #6, que aunque cada vez se pone más difícil, poco a poco se va logrando. Entonces comencemos:

*Nota* = La mayoría de códigos están comentados para que sea más fácil su comprensión

## Punto #1


1. Dado la figura de la imagen, desarrolle:

<div align='center'>
<figure> <img src="https://i.postimg.cc/FRvCmpxx/image.png" alt="" width="400" height="auto"/></br>
<figcaption><b></b></figcaption></figure>
</div>

+ Una función matemática para calcular el volumen y el área superficial.
+ Cree dos funciones en python para calcular los valores antes establecidos, al ingresar por teclado `r1`, `r2` y `h`.
+ Revise como utilizar el valor de `pi` usando *import math* y *math.pi*

### Solución punto #1

Para este punto obtuve el siguiente código :

``` python
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
```
Y al momento de correrlo en el terminal obtenemos algo así:

[![Captura-de-pantalla-2023-03-23-115708.png](https://i.postimg.cc/2SChMMtn/Captura-de-pantalla-2023-03-23-115708.png)](https://postimg.cc/sv0MZ6s2)

## Punto #2

Dado la figura de la imagen, desarrolle:

<div align='center'>
<figure> <img src="https://i.postimg.cc/1t4MrzsL/image.png" alt="" width="400" height="auto"/></br>
<figcaption><b></b></figcaption></figure>
</div>

+ Una función matemática para calcular el área y el perimetro.
+ Cree dos funciones en python para calcular los valores antes establecidos, al ingresar por teclado `r`, `a` y `b`.
+ Revise como utilizar el valor de `pi` usando *import math* y *math.pi*

### Solución punto #2

Para este punto diseñé el siguiente código: 

``` python
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
``` 
Y al momento de correrlo en el terminal obtenemos algo así:

[![Captura-de-pantalla-2023-03-23-120038.png](https://i.postimg.cc/8k61g5QV/Captura-de-pantalla-2023-03-23-120038.png)](https://postimg.cc/nMn8vnhd)

## Punto #3

Diseñe una función que calcule la cantidad de carne de aves en kilos si se tienen N gallinas, M gallos y K pollitos cada uno pesando 
6 kilos, 7 kilos y 1 kilo respectivamente.

### Solución punto #3

En este caso el código quedó algo así:

```python
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
```
Al momento de probarlo obtenemos lo siguiente: 

[![Captura-de-pantalla-2023-03-23-122344.png](https://i.postimg.cc/7Zr72VTt/Captura-de-pantalla-2023-03-23-122344.png)](https://postimg.cc/vcXcR5h5)

Listo, ahora seguimos con el punto #4

## Punto #4

Mi mamá me manda a comprar P panes a 300 cada uno, M bolsas de leche a  3300 cada una y H huevos a  350 cada uno. Hacer un programa 
que me diga las vueltas (o lo que quedo debiendo) cuando me da un billete de B pesos.

### Solución punto #4
Aquí en este punto obtuve el siguiente código: 
```python
#Le solicitamos al usuario que ingrese los datos necesitados para realizar el cálculo
Pan =int (input("Ingrese cantidad de panes que va a comprar: "))
Leche =int (input("Ingrese cantidad de bolsas de leche que va a comprar: "))
Huevos =int (input("Ingrese cantidad de huevos que va a comprar: "))
Billete =int (input("Ingrese el valor del billete con el que va a realizar la compra: "))

def calcularVueltas (Pan, Leche, Huevos, Billete ): #Definimos la función
    totalCompra = ((Pan* 300) + (Leche * 3300) + (Huevos * 350)) #Realizamos la operación de lo que va a ser el total de la compra
    if totalCompra <= Billete: #Le decimos al programa que  si el total de la compra es menor al billete entonces tendremos vueltas
        Vueltas = Billete - totalCompra #Realizamos la operación para que nos indique las vueltas 
        return Vueltas
    else: 
        faltante = Billete - totalCompra #Calculamos el faltante en caso de que toque
        return faltante
       
vueltas= calcularVueltas (Pan, Leche, Huevos, Billete ) #Le decimos al problema que las vueltas va a ser igual al resultado de la función

if vueltas >= 0 :  #Por medio de condicionales le indicamos al programa que imprimir
    print ("Las vueltas de su compra son:", vueltas, "pesos")
else:
    print ("La cantidad faltante de dinero para completar la compra es de:" , -vueltas, " pesos")
```   

Y al probar el código podemos obtener lo siguiente:

[![Captura-de-pantalla-2023-03-23-132357.png](https://i.postimg.cc/NG6c13pw/Captura-de-pantalla-2023-03-23-132357.png)](https://postimg.cc/s1gqz0kn)

Ya llegamos a la mitad del reto, sigamos al punto #5

## Punto #5

Haga un programa que utilice una función para calcular el valor de un préstamo `C` usando interés compuesto del `i` por `n` meses.

### Solución punto #5

``` python
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
```
Y en el momento de probarlo obtenemos lo siguiente:

[![Captura-de-pantalla-2023-03-23-132922.png](https://i.postimg.cc/Y0MSwYtX/Captura-de-pantalla-2023-03-23-132922.png)](https://postimg.cc/2b9YQqbv)

## Punto #6

 El número de contagiados de Covid-19 en el país de NuncaLandia se duplica cada día. Hacer un programa que diga el número total de
 personas que se han contagiado cuando pasen D días a partir de hoy, si el número de contagiados actuales es C.
 
 ### Solución punto #6
 
 Para el sexto punto tenemos el siguiente código:

``` python
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
```

Y al momento de probarlo obtenemos lo siguiente:

[![Captura-de-pantalla-2023-03-23-142133.png](https://i.postimg.cc/KYXjNR18/Captura-de-pantalla-2023-03-23-142133.png)](https://postimg.cc/PC4dffbg)

## Punto #7

Escriba un programa que pida 5 números reales y calcule las siguientes operaciones usando una función para cada una:
  + El promedio
  + La mediana 
  + El promedio multiplicativo (multilplica todos y luego calcula la raíz de la cantidad de operandos)
  + Ordenar los números de forma ascendente
  + Ordenar los números de forma descendente
  + La potencia del mayor número elevado al menor número
  + La raíz cúbica del menor número

### Solución punto #7

``` python
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
```
Al probarlo obtenemos lo siguiente: 

[![Captura-de-pantalla-2023-03-23-142403.png](https://i.postimg.cc/N0gqBcVx/Captura-de-pantalla-2023-03-23-142403.png)](https://postimg.cc/nXwwG6ns)

## Punto #8

Para el punto anterior incluir las funciones en un archivo independiente e importarlas para su uso

### Solución punto #8

En este punto solo definimos todas las funciones que utilizamos en el punto anterior

``` python
#Importamos una libreria pues es necesaria en una de las funciones que definiremos
import statistics

#Definimos todas las funciones que necesitamos y que importaremos en el punto 7
def promedio(n1,n2,n3,n4,n5) : 
    Promedio = (n1+n2+n3+n4+n5)/5
    return Promedio 

def promedioMultiplicativo (n1:float, n2:float, n3:float, n4:float, n5:float)->float:
  promedioM= (n1*n2*n3*n4*n5)**(1/5)
  return promedioM

def calcularMediana (n1:float, n2: float, n3: float, n4: float, n5: float) -> float:
   mediana = statistics.median ([n1,n2,n3,n4,n5])
   return mediana

def ordenarAscendente (n1:float, n2: float, n3: float, n4: float, n5: float) -> float:
  if n1 > n2:
      n1, n2 = n2, n1
  if n2 > n3:
      n2, n3 = n3, n2
  if n3 > n4:
      n3, n4 = n4, n3
  if n4 > n5:
      n4, n5 = n5, n4
  if n1 > n2:
      n1, n2 = n2, n1
  if n2 > n3:
      n2, n3 = n3, n2
  if n3 > n4:
      n3, n4 = n4, n3
  if n1 > n2:
      n1, n2 = n2, n1
  if n2 > n3:
      n2, n3 = n3, n2
  if n1 > n2:
      n1, n2 = n2, n1

  return n1, n2, n3, n4, n5

def ordenarDescendente (n1:float, n2: float, n3: float, n4: float, n5: float) -> float:
  if n1 < n2:
      n1, n2 = n2, n1
  if n2 < n3:
      n2, n3 = n3, n2
  if n3 < n4:
      n3, n4 = n4, n3
  if n4 < n5:
      n4, n5 = n5, n4
  if n1 < n2:
      n1, n2 = n2, n1
  if n2 < n3:
      n2, n3 = n3, n2
  if n3 < n4:
      n3, n4 = n4, n3
  if n1 < n2:
      n1, n2 = n2, n1
  if n2 < n3:
      n2, n3 = n3, n2
  if n1 < n2:
      n1, n2 = n2, n1

  return n1, n2, n3, n4, n5

def potenciaMayorMenor (n1:float, n2: float, n3: float, n4: float, n5: float) -> float:
    máximo = max(n1,n2,n3,n4,n5)
    mínimo = min(n1,n2,n3,n4,n5)
    potencia = máximo ** mínimo
    return potencia

def raizCubicaMenor (n1:float, n2: float, n3: float, n4: float, n5: float) -> float:
  mínimo = min (n1,n2,n3,n4,n5)
  if mínimo>= 0: 
    raiz_cubica = mínimo ** (1/3)
  else:
    raiz_cubica = -((-mínimo) ** (1/3))
  return raiz_cubica
```
Este punto no tenemos como tal una imagen de prueba pues aquí no le pedimos que nos imprima ningún resultado. Sin embargo, podemos deducir que está realizado de manera correcta pues funciona a la perfección en el punto 7 que es donde lo importamos 

## Punto #9

Consultar qué es y cómo funciona *pip* en python.

### Solución punto #9
Pip es un sistema de gestión de paquetes de Python que permite instalar y administrar paquetes de software escritos en Python. Con pip, los usuarios pueden descargar e instalar paquetes desde el repositorio PyPI (Python Package Index), así como también compartir sus propios paquetes con la comunidad de Python.

Pip también se encarga de gestionar las dependencias del paquete, es decir, instalar cualquier otro paquete que el paquete en cuestión necesite para funcionar correctamente. Además, pip permite a los desarrolladores gestionar las diferentes versiones de los paquetes, lo que significa que pueden instalar, actualizar o desinstalar paquetes específicos según sea necesario. Esto es especialmente útil en proyectos grandes o complejos que pueden depender de muchos paquetes diferentes.

En resumen, pip es una herramienta esencial para cualquier desarrollador de Python ya que facilita enormemente la instalación y gestión de paquetes de software, lo que a su vez puede ayudar a acelerar el desarrollo de proyectos y aumentar la productividad.

## Punto #10

Hacer un listado de módulos populares para python que se puedan instalar com *pip* y consultar cómo instalarlos.

+ Numpy: para cálculo numérico en Python
```python
pip install numpy
```
+ Pandas: para manipulación y análisis de datos en Python
```python
pip install pandas
```
+ Matplotlib: para visualización de datos en Python
```python
pip install matplotlib
```
+ SciPy: para computación científica en Python
```python
pip install spicy
```
+ Scikit-learn: para aprendizaje automático en Python
```python
pip install scikit-learn
```
+ TensorFlow: para aprendizaje profundo en Python
```python
pip install tensorflow
```
+ PyTorch: para aprendizaje profundo en Python
```python
pip install torch
```
+ Django: para desarrollo web en Python
```python
pip install django
```
+ Flask: para desarrollo web en Python
```python
pip install flask
```
+ Requests: para hacer solicitudes HTTP en Python
```python
pip install requests
```
Y listo, esto ha sido todo por este reto.

Espero haya sido claro para todos y que yo hubiese sido lo suficientemente clara.

Muchas gracias
