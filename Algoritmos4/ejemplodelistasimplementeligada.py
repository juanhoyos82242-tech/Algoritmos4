class Nodo:
    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula
        self.siguiente = None

class Lista:
    def __init__(self):
        self.cabeza = None

    def agregar_nodo(self, nombre, cedula):
        nuevo = Nodo(nombre, cedula)

        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo   # enlaza el nuevo nodo

        print("Creaste un nuevo nodo")

    def mostrar_lista(self):
        actual = self.cabeza
        while actual:
            print(f"{actual.nombre} ({actual.cedula})", end=" ==> ")
            actual = actual.siguiente
        print("fin")

# Uso
lista = Lista()
lista.agregar_nodo("Juan", 1234566)
lista.agregar_nodo("Felipe", 1244566)
lista.agregar_nodo("Luan", 1235566)
lista.mostrar_lista()