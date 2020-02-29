# Autor: Fernando Pérez González, A01376508
# Descripcion: Elaborar un algoritmo que muestre la velocidad, la distancia y el tiempo

# Escribe tu programa después de esta línea

v = int(input("Teclea la velocidad de un auto en km/hr (números enteros): "))

d1 = v*6
d2 = v*3.5
t = 485/v

print("Un coche recorre %d km, con una velocidad de %d km/h " % (d1,v))
print("Un coche recorre %.2f km, con una velocidad de %d km/h " % (d2,v))
print("Un coche tarda %.2f km, con una velocidad de %d km/h, para recorrer 485 km " % (t,v))