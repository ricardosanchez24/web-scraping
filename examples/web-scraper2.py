import requests
from bs4 import BeautifulSoup

def web_scraper():
    # guardamos la url a extraer los datos para hacer las peticiones
    url = 'https://listado.mercadolibre.com.ve/ford-fiesta#D[A:ford%20fiesta]'
    
    #creamos una identificacion para pasarla con la peticion para que la web me deje pasar
    headers = {
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36'
    }
    
    #enviamos una peticion get a la url y le pasamos la identificacion
    respuesta = requests.get(url,headers=headers)

    #imprimimos el codigo de respuesta 
    print(respuesta.status_code)
    
    # le pasamos la respuesta al metodo de bs4 para que parsee el html
    soup = BeautifulSoup(respuesta.text,'html.parser')
    print(soup.prettify())

    # obtenemos una lista con todas las etiquetas que queremos (y con esa clase)
    etiqueta = soup.find_all('div', class_='poly-card__content')
    print(etiqueta)

    #iteramos sobre la lista e imprimimos su titulo
    for titulo in etiqueta:
        print(titulo.text[500])

if __name__ == '__main__':
    web_scraper()