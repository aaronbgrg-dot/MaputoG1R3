from precios import comparar_pieza_coche

def ejecutar_comparador():
    print("\nSIMULADOR DE MERCADO DE PIEZAS\n")

    coche = input("Introduce el nombre del coche: ")
    pieza = input("Introduce la pieza: ")
    ofertas = input("Número de ofertas a comparar (por defecto 5): ")

    if ofertas.strip() == "":
        ofertas = 5
    else:
        ofertas = int(ofertas)

    resultado = comparar_pieza_coche(coche, pieza, ofertas)

    if not resultado:
        return

    precios, mejor_precio = resultado

    print(f"\nOfertas encontradas para {pieza} ({coche}):")
    contador = 1
    for precio in precios:
        print(f"Vendedor {contador}: {precio} €")
        contador += 1

    print(f"\nMEJOR PRECIO: {mejor_precio} €")


if __name__ == "__main__":
    ejecutar_comparador()
