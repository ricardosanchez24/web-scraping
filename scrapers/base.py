from typing import Optional

import requests
from bs4 import BeautifulSoup
from requests import RequestException

HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36',
}
TIMEOUT: int = 15


def obtener_html(url: str, headers: Optional[dict] = None) -> Optional[str]:
    headers = headers or HEADERS
    try:
        respuesta = requests.get(url, headers=headers, timeout=TIMEOUT)
        respuesta.raise_for_status()
        return respuesta.text
    except RequestException as e:
        print(f"Error de conexión: {e}")
        return None


def crear_soup(html: str) -> BeautifulSoup:
    return BeautifulSoup(html, 'html.parser')
