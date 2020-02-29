# Autor: Fernando Pérez González, A01376508
# Descripcion: Elaborar un algoritmo que calcule el porcentaje de hombres y mujeres inscritos en una clase.

# Escribe tu programa después de esta línea

m = int(input("Teclea la cantidad de mujeres inscritas en la clase: "))
h = int(input("Teclea la cantidad de hombres inscritos en la clase: "))

total = m + h
pm = (m*100)/total
ph = (h*100)/total

print("El total de personas inscritas en clase es de: %d" % total)
print("El porcentaje de mujeres inscritas en clase es de: %.1f%%" % pm)
print("El porcentaje de hombres inscritos en clase es de: %.1f%%" % ph)
