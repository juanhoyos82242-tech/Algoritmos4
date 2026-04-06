import re
canciones_juan={
    "bohemian rhapsody","shape of you","blinding lighth"
    "despacito", "hotel california"
}
canciones_cristian={
    "bohemian rhapsody", "despacito","wathermelon sugar","californication"

}

playlist_comun= canciones_juan & canciones_cristian
playlist_recomendacion= canciones_cristian - canciones_juan
catalogo= canciones_cristian|canciones_juan
a={canciones_juan<=canciones_cristian}#para saber si es un subconjunto
exclusivas= canciones_cristian ^ canciones_juan

print("============================================================================================================================================")


algoritmos={
    "ana", "carlos", "diana", "esudardo", "fernanda",
    "gabriel", "helena", "ivan"
} 
bases_datos={
    "carlos", "diana", "juan", "karen",
    "gabriel", "luis", "maria"
}
redes={
    "diana", "eduardo", "gabriel", "karen",
    "natalia", "oscar","ivan"
}

Todos_estudiantes= bases_datos | algoritmos | redes
solo_bases= bases_datos-algoritmos-redes
solo_algoritmos= algoritmos-redes - bases_datos
solo_redes=redes- bases_datos - algoritmos
estudian_una= solo_algoritmos |solo_bases | solo_redes
print(len(estudian_una))
print(Todos_estudiantes)
materias={
    "algoritmos":algoritmos,
    "bases_datos":bases_datos,
    "redes":redes,
}

for estudiante in Todos_estudiantes:
    conjuntos_donde_esta = [nombre for nombre, grupo in materias.items() if estudiante in grupo]
    print(f"{estudiante} está en: {conjuntos_donde_esta}")

print("======================================================================================================================================================")

catalogo = {
    "Inception": {"ciencia ficción", "acción", "thriller", "drama"},
    "The Matrix": {"ciencia ficción", "acción", "thriller"},
    "Titanic": {"romance", "drama", "histórica"},
    "The Notebook": {"romance", "drama"},
    "Avengers": {"acción", "ciencia ficción", "aventura"},
    "John Wick": {"acción", "thriller", "crimen"},
    "Interstellar": {"ciencia ficción", "drama", "aventura"},
    "The Godfather": {"crimen", "drama", "thriller"},
    "Toy Story": {"animación", "comedia", "aventura"},
    "Shrek": {"animación", "comedia", "aventura"}
}
def comparar_peliculas(catalogo):
    resultado = []
    peliculas = list(catalogo.keys())
    
    for i in range(len(peliculas)):
        for j in range(i+1, len(peliculas)):
            peli1, peli2 = peliculas[i], peliculas[j]
            comunes = catalogo[peli1] & catalogo[peli2]  
            if len(comunes) >= 2:
                resultado.append((peli1, peli2, comunes))
    return resultado

pares = comparar_peliculas(catalogo)

for peli1, peli2, comunes in pares:
    print(f"{peli1} y {peli2} comparten {len(comunes)} géneros: {comunes}")

print("===================================================================================================================================================================")

favoritos_mios = {"acción", "thriller", "aventura"}

def recomendar(catalogo, favoritos):
    recomendaciones = {}
    for pelicula, generos in catalogo.items():
        comunes = generos & favoritos
        if comunes:  # si hay al menos un género en común
            porcentaje = (len(comunes) / len(favoritos)) * 100
            recomendaciones[pelicula] = (porcentaje, comunes)
    return recomendaciones

recs = recomendar(catalogo, favoritos_mios)

for peli, (porcentaje, comunes) in recs.items():
    print(f"{peli}: {porcentaje:.0f}% recomendable (géneros en común: {comunes})")

