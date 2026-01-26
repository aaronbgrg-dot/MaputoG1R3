from precios import comparar_pieza_coche
from os import system
def ejecutar_comparador():
    system('cls')
    
    print(f"{"\nSIMULADOR DE MERCADO DE PIEZAS\n":^104}")

    coche = input(f"{"Introduce el nombre del coche: ":>51} ")
    pieza = input(f"{"Introduce la pieza: ":>51}")
    ofertas = input(f"{"Numero de ofertas a comparar (por defecto 5): " :>51}")

    if ofertas.strip() == "":
        ofertas = 5
    else:
        ofertas = int(ofertas)

    resultado = comparar_pieza_coche(coche, pieza, ofertas)

    if not resultado:
        return

    precios, mejor_precio = resultado

    print(f"{"\nOfertas encontradas para " + str(pieza) + " (" + str(coche) + "):":^104}")
    contador = 1
    for precio in precios:
        print(f"{"Vendedor " + str(contador) + ":" + str(precio) + "€":^104}")
        contador += 1

    print(f"{"\nMEJOR PRECIO: " + str(mejor_precio) + "€":^104}")


if __name__ == "__main__":
    ejecutar_comparador()
