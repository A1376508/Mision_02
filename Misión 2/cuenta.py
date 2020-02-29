# Autor: Fernando Pérez González, A01376508
# Descripcion: Elaborar un algoritmo que muestre el subtotal y el costo total de una comida

# Escribe tu programa después de esta línea

costo = float(input("Teclea el costo de tu comida: "))

propina= (costo*13)/100
IVA = (costo*16)/100
total = costo + propina + IVA

print("El subtotal de la comida es de: $%.2f  " % costo)
print("La propina de la comida es de: $%.2f " % propina)
print("El IVA de la comida es de: $%.2f  " % IVA)
print("El total de la comida es de $%.2f " % total)