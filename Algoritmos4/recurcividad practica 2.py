#1 a*a*a
def potencia(a,b)
    if b== 0:
        return 1
    else
        return a*potencia(a,b-1)

def potencia_optimizada(a,b)
    if b==0:
        return 1
    if b % 2 == 0:
        mitad=potencia_optimizada(a,b//2)
        return mitad*mitad
    else:
        return a* potencia_optimizada(a,b-1)
    
#sumar digitos
def sumar_digitos(n):
    n = abs(n)  
    if n < 10:
        return n
    return sumar_digitos(n // 10) + n % 10
