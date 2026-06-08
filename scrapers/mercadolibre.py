from typing import Optional

from scrapers.base import obtener_html, crear_soup
from scrapers.utils import limpiar_precio, limpiar_texto

URL_ML = 'https://listado.mercadolibre.com.ve/ford-fiesta'

SELECTORES = {
    'contenedor': 'div.poly-card__content',
    'titulo': 'h3.poly-content__title-wrapper',
    'precio': 'div.poly-content__price',
    'contenedor_selenium': 'li.ui-search-layout__item',
    'titulo_selenium': 'h3.poly-component__title-wrapper',
    'precio_selenium': 'div.poly-component__price',
    'atributos': 'div.poly-component__attributes-list',
    'ubicacion': 'span.poly-component__location',
}


def extraer_productos_bs4(html: str) -> list[dict]:
    soup = crear_soup(html)
    items = soup.find_all('div', class_='poly-card__content')
    productos: list[dict] = []

    for item in items:
        titulo = item.find('h3', class_='poly-content__title-wrapper')
        precio = item.find('div', class_='poly-content__price')

        if titulo:
            productos.append({
                'titulo': limpiar_texto(titulo.text),
                'precio': limpiar_precio(precio.text if precio else None),
            })

    return productos


def scrapear_ml_bs4() -> list[dict]:
    html = obtener_html(URL_ML)
    if html is None:
        return []
    return extraer_productos_bs4(html)
