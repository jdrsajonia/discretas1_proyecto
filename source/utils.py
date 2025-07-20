import matplotlib.pyplot as plt

def graficar_diccionario_barras(titulo:str, nombre_eje_x:str, nombre_eje_y:str, diccionario:dict):
    '''
    Imprime las claves y valores de un diccionario en formato de grados por IP.
    Útil para ver los grados de los nodos.
    '''
    # Ordenar por clave para mantener consistencia en eje X
    claves = list(diccionario.keys())
    valores = list(diccionario.values())

    # Convertir claves complejas (como tuplas) a strings para mostrar
    etiquetas = [str(k) for k in claves]

    # Normalizar valores para mapa de color (entre 0 y 1)
    max_valor = max(valores) if valores else 1
    colores_normalizados = [v / max_valor for v in valores]
    
    # Crear colores entre azul y rojo
    colormap = plt.colormaps.get_cmap('coolwarm')  # azul -> rojo
    colores = [colormap(c) for c in colores_normalizados]

    # Crear gráfica
    fig, ax = plt.subplots(figsize=(12, 6))
    barras = ax.bar(etiquetas, valores, color=colores)

    # Títulos
    ax.set_title(titulo)
    ax.set_xlabel(nombre_eje_x)
    ax.set_ylabel(nombre_eje_y)

    # Rotar etiquetas si son largas
    plt.xticks(rotation=90, ha='right')
    plt.tight_layout()
    plt.show()


def obtener_max_conexiones_multiple(diccionario: dict):
    """
    Retorna una lista con todas las claves que tienen el valor máximo en el diccionario,
    junto con dicho valor.

    Parámetros:
    - diccionario (dict): Diccionario donde las claves son nodos o tuplas (usuario-servidor)
                          y los valores representan el grado de conexión.

    Retorna:
    - (lista_claves_max, valor_max): Tupla donde el primer elemento es una lista con las claves
      que tienen el valor máximo, y el segundo es el valor en sí.
    """

    valor_max = max(diccionario.values())
    claves_max = [clave for clave, valor in diccionario.items() if valor == valor_max]
    return claves_max, valor_max