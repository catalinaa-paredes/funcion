#definir si es primo o no
def es_primo(numero):
    if numero < 2:   #numeros menores que dos no son primos
        return False
    for i in range(2, int(numero**0.5) + 1): #funcion 
        if numero % i == 0: 
            return False  #verificar y retornar
    return True

#preguntar y responder
numero = int(input("Ingresa un número: "))
if es_primo(numero):
    print(f"{numero} es un número primo.")
else:
    print(f"{numero} no es un número primo.")




#segunda funcion primos menores que un numero
def numeros_primos_menores(numero):
    numeros_primos = []
    for num in range(2, numero):
        if es_primo(num):
            numeros_primos.append(num)
    return numeros_primos

#primera funcion si es primo o no
def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

#preguntar y responder
numero = int(input("Ingrese un número: "))
primos_menores = numeros_primos_menores(numero)
print("Números primos menores a", numero, ":")
print(primos_menores)