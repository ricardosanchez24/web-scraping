import requests
from bs4 import BeautifulSoup



def primer_scraper():
    url = 'https://medium.com/@joerosborne/web-scraping-with-puppeteer-extra-typescript-aws-lambda-bf4f49d49806'
    respuesta = requests.get(url,verify=False)
    soup = BeautifulSoup(respuesta.text,'html.parser')
    #print(soup)

    titulo = soup.select_one('h1').text
    parrafo = soup.select_one('p').text
    enlace = soup.select_one('a').get('href')

    print(titulo)
    print(parrafo)
    print(enlace)

if __name__ == '__main__':
    primer_scraper()