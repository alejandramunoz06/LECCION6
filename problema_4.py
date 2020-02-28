from fractions import Fraction as frac
import math
viento = float(input("Ingrese el viento en M/h: "))
t = float(input("Ingrese la temperatura en Farenheit: "))
if 0 <= viento <= 44:
    print("El indice de sensacion termica con el metodo 1 es: ", t)
elif viento >= 45:
    wci = 1.6*t-55
    print("El indice de sensacion termica con la formula 2 es: ",wci )
wci2 = 91.4 + (91.4-t) *(0.0203) * (math.sqrt(viento)-0.474)
print("El indice de sensacion termica con el metodo 3 es: ",wci2 )
                      
    
    



               
