from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from time import sleep
from chrome_options import get_chrome_options


class ZType:

    def __init__(self):
        options = get_chrome_options()
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=options)
        self.start()

    def start(self):
        self.driver.get("https://zty.pe/")
        self.driver.maximize_window()

        for i in range(3):
            sleep(1)
            print(f"Starting in {3- i} seconds...")

        # Enviar la tecla "Enter" directamente al cuerpo de la página
        body = self.driver.find_element(By.TAG_NAME, "body")
        body.send_keys(Keys.ENTER)
        sleep(1)

        self.simulate_press_alphabet()

    def simulate_press_words_of_the_game(self):
        body = self.driver.find_element(By.TAG_NAME, "body")

        while True:
            for key, value in words.items():
                for word in value:
                    body.send_keys(word)
                    sleep(0.03)
            sleep(0.03)

    def simulate_press_alphabet(self):
        body = self.driver.find_element(By.TAG_NAME, "body")

        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        big_alphabet_string = alphabet * 5
        while True:
            body.send_keys(big_alphabet_string)
            sleep(0.03)


if __name__ == "__main__":
    ztype = ZType()
