from typing import Optional

import requests
from bs4 import BeautifulSoup
from requests import RequestException

URL = 'https://listado.mercadolibre.com.ve/ford-fiesta'
HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36',
}


def obtener_html(url: str, headers: dict) -> Optional[str]:
    try:
        respuesta = requests.get(url, headers=headers, timeout=15)
        respuesta.raise_for_status()
        return respuesta.text
    except RequestException as e:
        print(f"Error de conexión: {e}")
        return None


def extraer_productos(html: str) -> list[dict]:
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='poly-card__content')
    productos: list[dict] = []

    for item in items:
        titulo = item.find('h3', class_='poly-content__title-wrapper')
        precio = item.find('div', class_='poly-content__price')

        if titulo:
            productos.append({
                'titulo': titulo.text.strip(),
                'precio': precio.text.strip() if precio else 'N/A',
            })

    return productos


def mostrar_resultados(productos: list[dict]) -> None:
    if not productos:
        print("No se encontraron productos.")
        return

    for p in productos:
        print(f"Producto: {p['titulo']} - Precio: {p['precio']}")


def main() -> None:
    html = obtener_html(URL, HEADERS)
    if html is None:
        return

    productos = extraer_productos(html)
    mostrar_resultados(productos)


if __name__ == '__main__':
    main()