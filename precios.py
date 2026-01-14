import random
from datos import coches

def generar_precios_mercado(precio_base, numero_ofertas=5, variacion=0.10):
    precios = []
    for _ in range(numero_ofertas):
        factor = random.uniform(1 - variacion, 1 + variacion)
        precio = round(precio_base * factor, 2)
        precios.append(precio)
    return precios

def comparar_pieza_coche(nombre_coche, nombre_pieza, numero_ofertas=5):

    if nombre_coche not in coches:
        print("Error: el coche no existe")
        return

    if nombre_pieza not in coches[nombre_coche]:
        print("Error: la pieza no existe para ese coche")
        return

    precio_base = coches[nombre_coche][nombre_pieza]
    precios_mercado = generar_precios_mercado(precio_base, numero_ofertas)
    mejor_precio = min(precios_mercado)

   
    return precios_mercado, mejor_precio

