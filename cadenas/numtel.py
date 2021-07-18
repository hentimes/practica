# Pedir numero de telefono con prefijo + numero +  ext.
# Imprimir solo numero de telefono

print ("Ingrese el numero telefonico con codigo y extension:")
c = input("Ingrese el codigo de pais: +")
n = input(f"Ingrese el numero telefonico: +{c} ")
e = input(f"Ingrese el numero de extension: +{c} {n} ")

print (f"El numero telefonico registrado es: {n}")

"""
Respuesta sugerida:

tel = input("Introduce un numero de tel con formato +xx-xxxxxxxxx-xx: ")
print ('El numero de tel es ', tel[4:-3])
"""
