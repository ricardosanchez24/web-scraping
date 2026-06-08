from scrapers.mercadolibre import scrapear_ml_bs4


def mostrar_resultados(productos: list[dict]) -> None:
    if not productos:
        print("No se encontraron productos.")
        return

    for p in productos:
        print(f"Producto: {p['titulo']} - Precio: {p['precio']}")


def main() -> None:
    productos = scrapear_ml_bs4()
    mostrar_resultados(productos)


if __name__ == '__main__':
    main()