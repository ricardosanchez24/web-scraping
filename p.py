import requests
from bs4 import BeautifulSoup

def web_scraper():
    url = 'https://listado.mercadolibre.com.ve/ford-fiesta'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36'
    }
    
    try:
        respuesta = requests.get(url, headers=headers)
        if respuesta.status_code == 200:
            soup = BeautifulSoup(respuesta.text, 'html.parser')
            
            # Intentamos buscar los elementos individuales de cada producto
            productos = soup.find_all('div', class_='poly-card__content')
            
            if not productos:
                print("No se encontraron productos. Es posible que la estructura haya cambiado o te detectaron como bot.")
                return

            for item in productos:
                # Dentro de cada item, buscamos el título
                titulo = item.find('h3', class_='poly-content__title-wrapper')
                precio = item.find('div', class_='poly-content__price')
                
                if titulo:
                    print(f"Producto: {titulo.text} - Precio: {precio.text if precio else 'N/A'}")
        else:
            print(f"Error de conexión: {respuesta.status_code}")
            
    except Exception as e:
        print(f"Ocurrió un error: {e}")

if __name__ == '__main__':
    web_scraper()