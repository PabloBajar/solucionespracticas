# Ejercicio venta de leche

esjubilado = input("Indique con si o no si es jubilado: ")
litrosLeche = int(input("Indique la cantidad de litros de leche: "))

if (esjubilado=="no"):
    if (litrosLeche<12):
        totalLitros = litrosLeche*1000
    elif (litrosLeche>=12 and litrosLeche<=24):
        totalLitros= litrosLeche*900
    else:
        totalLitros= litrosLeche*850
else:
    if (litrosLeche<12):
        totalLitros = litrosLeche*900
    elif (litrosLeche>=12 and litrosLeche<=24):
        totalLitros= litrosLeche*800
    else:
        totalLitros= litrosLeche*750

print("El total a pagar es de $",totalLitros)

