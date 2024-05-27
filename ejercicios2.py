# 1 - MOSTRAR NUMEROS.
n=0
m= int(input("Ingrese un numero que sirva de limite al contador: "))

while (n<m):
    n=n+1
    print(n)

# 2 - MOSTRAR NUMEROS PARES
n=0
m= int(input("Ingrese un numero que sirva de limite al contador: "))

while (n<m):
    if (n % 2 == 0):
        print(n)
    n=n+1

# 3 - INGRESAR NOMBRES
nombre = input("Ingrese un nombre de persona, si queire finalizar, escriba fin: ")

while (1==1):
    if (nombre != "fin"):
        print(nombre)
        nombre = input("Ingrese un nombre de persona, si queire finalizar, escriba fin: ")
    else:
        break




