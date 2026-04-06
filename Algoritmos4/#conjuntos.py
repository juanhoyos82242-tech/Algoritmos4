#conjuntos
A={1,2,3}
B={3,4,5}
print(A|B)#union
print(A&B)#intersepcion
print(A-B),print(B-A)#diferencia
print(A^B)#diferencia simetrica

Lista1=[1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10,11,11,12,12,13,13]

Conjunto1=set(Lista1)#utilizar set para convertir lista en conjunto, utilizar list para convertir conjunto en lista
print(Conjunto1)
print(len(Conjunto1))
#add para agregar un elemento a un conjunto"conjunto1.add("14")"
#remove para eliminar elementos "conjunto1.remove("14")
#convertir en lista ordenada"lista_ordenada= sorted(conjunti1)
#saber si un conjunto pertenece a otro conjunto1.issuset(conjuntoU)
