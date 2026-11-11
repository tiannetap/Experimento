# Módulo principal

def principal():
    datos_entrada = [12.5, -999, 15.0, None, 18.2, 20.1, -5, 14.8]

    resultado_estadistico = calcular_estadisticas_descriptivas(datos_entrada)

    if resultado_estadistico is None:
        print("No hay datos válidos para procesar.")
    else:
        print("Resultado Estadístico:")
        print(f"Media: {resultado_estadistico['media']:.2f}")
        print(f"Varianza: {resultado_estadistico['varianza']:.2f}")
        print(f"Desviación estándar: {resultado_estadistico['desviacion_estandar']:.2f}")


# Módulo de coordinación

def calcular_estadisticas_descriptivas(datos):

    datos_limpios = filtrar_datos_validos(datos)

    if len(datos_limpios) == 0:
        return None

    media = calcular_media(datos_limpios)
    varianza = calcular_varianza(datos_limpios, media)
    desviacion = calcular_desviacion_estandar(varianza)

    return {
        "media": media,
        "varianza": varianza,
        "desviacion_estandar": desviacion
    }


# Módulos de Soporte

def filtrar_datos_validos(datos):
    resultado = []

    for elemento in datos:
        
        if elemento is not None and elemento >= 0:
            resultado.append(float(elemento))

    return resultado


def calcular_media(datos):
    suma_total = sum(datos)
    total_elementos = len(datos)

    return suma_total / total_elementos


def calcular_varianza(datos, media):
    suma_cuadrados = 0.0
    total_elementos = len(datos)

    for x in datos:
        suma_cuadrados += (x - media) ** 2

    return suma_cuadrados / total_elementos


def calcular_desviacion_estandar(varianza):
    return varianza ** 0.5

# Ejecución

if __name__ == "__main__":
    principal()
