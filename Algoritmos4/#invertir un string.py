#invertir un string
#hola-->aloh
def invetir(s):
    if len(s)<= 1:
       return s
    return invetir(s{1:}) + s[0]

"hola"
"ola" "h"
"la"  "o"
"a"   "l"
"a"
#verificador si una palabra es palindormo
 palabra= input("ingrese la palabra")

 def verrificacion_palindromo(palabra)
     if len(palabra)<= 1:
       return palabra
     return verrificacion_palindromo(palabra{1:}) + s[0]
 palabra2= verrificacion_palindromo
 if palabra==palabra2:
   print("es palindromo")
 else
   print("no es palindromo")

   return 0
#contar cuantas veces se repite un caracter en un texto
def contar(s, c):
    if len(s) == 0:
        return 0
    if s[0] == c:
        return 1 + contar(s[1:], c)
    return contar(s[1:], c)
print(contar("holaa","a"))
#
class node:
   def __init__(self,dato):
      self.dato = dato
      self.siguiente = None
class lista:
   def __init__(self):
      self.cabeza =None
   def agregar(dato):
      node=node(dato)
      if self.cabeza==None
         self.cabeza= node
      else:
         actual =self.cabeza
         while actual = actual.siguiente:
            actual=actual.siguiente
          actual.siguiente= node

        # Si no se pasa nodo, empezamos desde la cabeza
        # Caso base: si el nodo es None, no hay más elementos
        # Caso recursivo: 1 (el nodo actual) + contar el resto

   def contar(self, node=None):
    if node == None:
        node = self.cabeza
    if node == None:
        return 0
    else:
        return 1 + self.contar(node=.siguiente)
