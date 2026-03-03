from selenium import webdriver
from selenium.webdriver.common.by import By

def web_scraper_selenium():

    driver = webdriver.Chrome()

    url = 'https://listado.mercadolibre.com.ve/ford-fiesta#D[A:ford%20fiesta]'

    try:
        driver.get(url)

        driver.implicitly_wait(2)
    except Exception as e:
        print(f"Error!!!, el error que ocurrio fue {e}")

    lista_publicaciones = driver.find_elements(by=By.CSS_SELECTOR, value="li.ui-search-layout__item")

    if not lista_publicaciones:
        return "lista vacia, no hay elementos disponibles"

    for publicacion in lista_publicaciones:

        titulo = publicacion.find_element(by=By.CSS_SELECTOR, value="h3.poly-component__title-wrapper").text
        precio = publicacion.find_element(by=By.CSS_SELECTOR, value="div.poly-component__price").text
        kilometraje_año = publicacion.find_element(by=By.CSS_SELECTOR, value="div.poly-component__attributes-list").text
        ubicacion = publicacion.find_element(by=By.CSS_SELECTOR, value="span.poly-component__location").text

        print(f"Carro: {titulo}")
        print(f"Precio: {precio}")
        print(f"Año y kilometraje: {kilometraje_año}")
        print(f"Ubicacion: {ubicacion}\n")


    driver.quit()

if __name__ == "__main__":
    web_scraper_selenium()    