p1 = float(input("Precio por libra paquete A: "))
p1a = float(input("Porcentaje magro paquete A: "))
p2 = float(input("Precio por libra paquete B: "))
p2b = float(input("Porcentaje magro paquete B: "))
c1 =(p1/p1a)
c2 =(p2/p2b)
print("Costo por libra de carne magra en Paquete A: " ,c1)
print("Costo por libra de carne magra en Paquete B: " ,c2)

if c1 > c2:
    print("El paquete B es mejor")
else:
    print("El paquete A es mejor")
               
