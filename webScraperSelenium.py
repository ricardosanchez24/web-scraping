from selenium import webdriver
from selenium.webdriver.common.by import By

def web_scraper():
    # 1-iniciar sesion
    driver = webdriver.Chrome()
    # 2-realizar acciones en el navegador (como entrar en un pagina)
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")

    # 3-solicitar info del navegador
    title = driver.title
    print(title)

    # 4- establecer una estrategia de espera
    driver.implicitly_wait(2)

    # 5- encontrar elementos
    text_box = driver.find_element(by=By.NAME, value="my-text")
    submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

    # 6- puedes realizar acciones con esos elementos (escribir, hacer click,etc)
    text_box.send_keys("Selenium")
    submit_button.click()

    # 7- solicitar informacion de los elementos
    message = driver.find_element(by=By.ID, value="message")
    text = message.text

    print(text)

    # finalizar la sesion
    driver.quit()

if __name__ == '__main__':
    web_scraper()

'''
    wait = WebDriverWait(driver, timeout=2)
    wait.until(lambda _ : revealed.is_displayed())
'''    