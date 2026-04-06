import re


def validar_telefono(numero):
   
    telefono_valido= re.match(r"^3\d{2}[-/s]?\d{3}[-/s]?\d{2}[-/s]?\d{2}$",numero)
   
    return bool(telefono_valido)

print(validar_telefono("3053468688"))




def validar_fecha(fecha):
    fecha_validar= re.match(r"^(0[1-9]|[12]\d|3[01])[-/](0[1-9]|1[0-2])[-/](10|20)\d{2}$",fecha)
    return bool (fecha_validar)

print(validar_fecha("01/05/2026"))



def validar_contraseña(contraseña):#verificar que contenga minimo 8 caracteres y que tenga minimo una Mayuscula
    # Mínimo 8 caracteres
    if len(contraseña) >= 8:
        # Al menos una mayúscula
        if re.search(r'[A-Z]', contraseña):
            # Al menos una minúscula
            if re.search(r'[a-z]', contraseña):
                # Al menos un carácter especial
                if re.search (r'[!@#$%^&*]', contraseña):

                    if re.search (r'\d', contraseña):
                        return True
                    
    return False
print(validar_contraseña("Marinilla2064*"))
