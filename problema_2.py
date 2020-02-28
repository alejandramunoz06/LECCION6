
mi = float(input("Indique las millas por galon: "))
tan = float(input("Indique la capacidad del tanque: "))
med = float(input("Indique cuanto marca el medidor: "))
camino = tan*med*mi
if camino > 200:
    print("seguro, proceder")
else:
    print("Solo es posible recorrer: ", camino, " millas. Consigue gasolina")
               
