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

## Punto #4

Mi mamá me manda a comprar P panes a 300 cada uno, M bolsas de leche a  3300 cada una y H huevos a  350 cada uno. Hacer un programa 
que me diga las vueltas (o lo que quedo debiendo) cuando me da un billete de B pesos.

### Solución punto #4

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

## Punto #6

 El número de contagiados de Covid-19 en el país de NuncaLandia se duplica cada día. Hacer un programa que diga el número total de
 personas que se han contagiado cuando pasen D días a partir de hoy, si el número de contagiados actuales es C.
 
 ### Solución punto #6

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

## Punto #8

Para el punto anterior incluir las funciones en un archivo independiente e importarlas para su uso

### Solución punto #8

## Punto #9

Consultar qué es y cómo funciona *pip* en python.

## Punto #10

Hacer un listado de módulos populares para python que se puedan instalar com *pip* y consultar cómo instalarlos.
