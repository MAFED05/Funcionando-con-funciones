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