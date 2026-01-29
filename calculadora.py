from precios import comparar_pieza_coche

def ejecutar_comparador():
    print("\nSIMULADOR DE MERCADO DE PIEZAS\n")
# Solicita los datos al usuario
    coche = input("Introduce el nombre del coche: ")
    pieza = input("Introduce la pieza: ")
    ofertas = input("Número de ofertas a comparar (por defecto 5): ")
  # Si el usuario no introduce nada, se usan 5 ofertas por defecto

    if ofertas.strip() == "":
        ofertas = 5
    else:
        ofertas = int(ofertas)

    resultado = comparar_pieza_coche(coche, pieza, ofertas)

    if not resultado:
        return

    precios, mejor_precio = resultado
  # Muestra las ofertas encontradas
    print(f"\nOfertas encontradas para {pieza} ({coche}):")
    contador = 1
    for precio in precios:
        print(f"Vendedor {contador}: {precio} €")
        contador += 1
# Muestra el mejor precio
    print(f"\nMEJOR PRECIO: {mejor_precio} €")


if __name__ == "__main__":
    ejecutar_comparador()
