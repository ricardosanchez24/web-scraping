from typing import Optional

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import WebDriverException, NoSuchElementException

from scrapers.base import HEADERS
from scrapers.mercadolibre import URL_ML
from scrapers.utils import limpiar_texto, limpiar_precio

URL_SELENIUM = URL_ML + '#D[A:ford%20fiesta]'
SELECTORES = {
    'contenedor': 'li.ui-search-layout__item',
    'titulo': 'h3.poly-component__title-wrapper',
    'precio': 'div.poly-component__price',
    'atributos': 'div.poly-component__attributes-list',
    'ubicacion': 'span.poly-component__location',
}
IMPLICIT_WAIT: int = 2


def extraer_dato(elemento: WebElement, selector: str, por: str = 'css selector') -> Optional[str]:
    try:
        return elemento.find_element(by=By.CSS_SELECTOR, value=selector).text
    except NoSuchElementException:
        return None


def extraer_publicaciones(driver: webdriver.Chrome) -> list[dict]:
    contenedores = driver.find_elements(
        by=By.CSS_SELECTOR,
        value=SELECTORES['contenedor'],
    )
    publicaciones: list[dict] = []

    for c in contenedores:
        titulo = extraer_dato(c, SELECTORES['titulo'])
        if not titulo:
            continue

        publicaciones.append({
            'titulo': limpiar_texto(titulo),
            'precio': limpiar_precio(extraer_dato(c, SELECTORES['precio'])),
            'atributos': limpiar_texto(extraer_dato(c, SELECTORES['atributos'])),
            'ubicacion': limpiar_texto(extraer_dato(c, SELECTORES['ubicacion'])),
        })

    return publicaciones


def mostrar_publicaciones(publicaciones: list[dict]) -> None:
    if not publicaciones:
        print("No se encontraron publicaciones.")
        return

    for p in publicaciones:
        print(f"Carro: {p['titulo']}")
        print(f"Precio: {p['precio']}")
        print(f"Año y kilometraje: {p['atributos']}")
        print(f"Ubicación: {p['ubicacion']}\n")


def web_scraper_selenium() -> None:
    driver = webdriver.Chrome()

    try:
        driver.get(URL_SELENIUM)
        driver.implicitly_wait(IMPLICIT_WAIT)

        publicaciones = extraer_publicaciones(driver)
        mostrar_publicaciones(publicaciones)

    except WebDriverException as e:
        print(f"Error del navegador: {e}")
    finally:
        driver.quit()


if __name__ == "__main__":
    web_scraper_selenium()    