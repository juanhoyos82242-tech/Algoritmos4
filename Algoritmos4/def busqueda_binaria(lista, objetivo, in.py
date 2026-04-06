def busqueda_binaria(lista, objetivo, inicio=0, fin=None):
    if fin == None:
        fin = len(lista) - 1

    # Caso base: si el rango ya no es válido
    if inicio > fin:
        return -1  # No encontrado

    # Punto medio
    medio = (inicio + fin) // 2

    # Caso encontrado
    if lista[medio] == objetivo:
        return medio

    # Caso recursivo: buscar en la mitad izquierda
    elif objetivo < lista[medio]:
        return busqueda_binaria(lista, objetivo, inicio, medio - 1)

    # Caso recursivo: buscar en la mitad derecha
    else:
        return busqueda_binaria(lista, objetivo, medio + 1, fin)
    
# permutaciones
def permutaciones(lista):
    if len(lista) == 1:
        return [lista]
    resultado = []
    for i in range(len(lista)):
        actual = lista[i]
        resto = lista[:i] + lista[i+1:]
        for p in permutaciones(resto):
            resultado.append([actual] + p)
    return resultado

