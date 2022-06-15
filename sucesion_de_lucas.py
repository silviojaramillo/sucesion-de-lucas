# Dada la siguiente serie determinar el algoritmo
#para obtener 16 términos
# 2, 1, 3, 4, 7, 11, 18, 29, 47, 76, 123

#Creando el arreglo para guardar los términos
sequence = [2,1]

#Agregando términos al arreglo
for i in range(1,15):
    addTerm = sequence[i] + sequence[i-1]
    sequence.append(addTerm)
print(sequence)