# Problema de Ordenamiento (Selection Sort)

# [25.4, 12.8, 35.1, 4.2, 18.5]

# Módulo principal

def principal():
    lista_original = [45.5, 12.3, 89.1, 3.4, 27.8]

    print("Lista original (inmutable):", lista_original)

    lista_ordenada = ordenar_por_seleccion(lista_original)

    print("Resultado del ordenamiento:", lista_ordenada)


# Módulo de ordenamiento

def ordenar_por_seleccion(lista_entrada):
        lista_copia = copiar_arreglo(lista_entrada) 
        n = len(lista_copia)

        for i in range(n - 1):
            indice_minimo = i
            for j in range(i + 1, n):
                
                if lista_copia[j] < lista_copia[indice_minimo]:
                    indice_minimo = j

        if indice_minimo != i:
            temporal = lista_copia[i]
            lista_copia[i] = lista_copia[indice_minimo]
            lista_copia[indice_minimo] = temporal
            
        return lista_copia


# Módulo Auxiliar

def copiar_arreglo(original):
    copia = []

    for k in range(len(original)):
        copia.append(original[k])

    return copia


# Ejecución del programa principal
if __name__ == "__main__":
    principal()
