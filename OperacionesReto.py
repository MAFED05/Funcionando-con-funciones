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
