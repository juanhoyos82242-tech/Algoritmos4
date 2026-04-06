import re

texto= ""
resultado= re.findall( r"\w+{\@ ", texto) 

print(resultado)