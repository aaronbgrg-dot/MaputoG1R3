import random
from datos import coches

def generar_precios_mercado(precio_base, numero_ofertas=5, variacion=0.10):
    # Lista donde se guardarán los precios generados
    precios = []

    # Genera tantos precios como ofertas haya
    for _ in range(numero_ofertas):
        # Factor aleatorio de variación (±10%) (IA)
        factor = random.uniform(1 - variacion, 1 + variacion)

        # Calcula el precio final aplicando la variación
        precio = round(precio_base * factor, 2)

        
        precios.append(precio)

    # Devuelve la lista de precios 
    return precios


def comparar_pieza_coche(nombre_coche, nombre_pieza, numero_ofertas=5):

    # Comprueba si el coche existe en los datos
    if nombre_coche not in coches:
        print("Error: el coche no existe")
        return

    # Comprueba si la pieza existe para ese coche
    if nombre_pieza not in coches[nombre_coche]:
        print("Error: la pieza no existe para ese coche")
        return

    # Obtiene el precio base de la pieza
    precio_base = coches[nombre_coche][nombre_pieza]

     # Genera los precios para el mercado
    precios_mercado = generar_precios_mercado(precio_base, numero_ofertas)

 # Obtiene el mejor precio
    mejor_precio = min(precios_mercado)

    # Devuelve los precios y el mejor precio
    return precios_mercado, mejor_precio


