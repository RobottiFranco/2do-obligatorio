
def transformacion(numero1, numero2):

    #descomponer en primos
    numeroDescompuesto1 = descomponer(numero1)
    numeroDescompuesto2 = descomponer(numero2)
    
    #potencias
    diccionarioDescompuesto1 = potencia(numeroDescompuesto1)
    diccionarioDescompuesto2 = potencia(numeroDescompuesto2)
    
    #mcd
    maximoComunDivisor = mcd(diccionarioDescompuesto1, diccionarioDescompuesto2)
    
    #impresoras
    numero1AImprimir = impresoraNumeros(numero1, diccionarioDescompuesto1)
    numero2AImprimir = impresoraNumeros(numero2, diccionarioDescompuesto2)
    mcdAimprimir = impresoraMCD(numero1, numero2, maximoComunDivisor)

    return impresora(numero1AImprimir, numero2AImprimir, mcdAimprimir)

#se encarga de ver la lista de numeros primos del 1 al 100 y dividir comprando si existe un resultado 0, si la division da 0 agrega a la lista y vuelve a dividir, sino, paso al siguiente de la lista de primos

def descomponer(numero):
    listaNumerosPrimos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    primoNumList = []
    recorrerListaPrimos = 0

    while (numero != 1):
        if numero % listaNumerosPrimos[recorrerListaPrimos] != 0: 
            recorrerListaPrimos += 1
        else:
            numero = numero / listaNumerosPrimos[recorrerListaPrimos]
            primoNumList.append(listaNumerosPrimos[recorrerListaPrimos])

    return primoNumList

#esta funcion se encarga  de toma el resultado la funcion descomponer y se fija en cada resultado, si hay un valor repetido lo guarda en un diccionario asi pueden ser utilizados como potencia

def potencia(numeroDescompuesto):
    diccionario = {}
    for aDiccionario in numeroDescompuesto:
        if aDiccionario not in diccionario:
            diccionario[aDiccionario] = 0
        diccionario[aDiccionario] += 1

    return diccionario

#se encarga de toma las descomposiciones de primos y se fija si un valor se repite, si es asi, lo agrega a una lista que los contenga ej: entre 24 y 30 esta [2,3]
#en caso de que no haya ninguno agrego un 1

def mcd(diccionario1, diccionario2):
    listaMCD = []
    for clave in diccionario1:
        if clave in diccionario2:
            listaMCD.append(clave)
    if len(listaMCD) == 0:
        listaMCD.append(1)
    return listaMCD

#impresoras
#se encargan de preparar el texto para ser impreso, le da formato

#se encarga de los numeros para potencia "El numero 24 = 2^3 x 3^1"
def impresoraNumeros(numero, diccionario):
    text = f"el numero {numero} ="
    for clave in diccionario:
        valor = diccionario[clave]
        text += f" {clave}^{valor} x"

    return text

#se encarga de el MCD "y el mcd(20,63) = 1"
def impresoraMCD(numero1, numero2, maximoComunDivisor):
    text = f"y el mcd({numero1},{numero2}) = "
    for num in maximoComunDivisor:
        text +=  f"{num} x "
    return text

#es el restulado final "el numero 20 = 2^2 x 5^1 , el numero 63 = 3^2 x 7^1 y el mcd(20,63) = 1"
def impresora(numero1AImprimir, numero2AImprimir, mcdAimprimir):
    return numero1AImprimir[0:-1] + ", " + numero2AImprimir[0:-1] + mcdAimprimir[0:-2]

#main
 
#caso de prueba 1
numero1 = 24
numero2 = 30

print(transformacion(numero1, numero2))

#caso de prueba 2
numero1 = 20
numero2 = 63

print(transformacion(numero1, numero2))