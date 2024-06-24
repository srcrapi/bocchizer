import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.firefox import GeckoDriverManager



class WebSearcher:
    def __init__(self):
        self.options = FirefoxOptions()
        self.options.add_argument("--headless")

    def search(self, search_term: str, num_images: int = 6) -> list:
        """
        Pesquisa o item no google images e retorna a sua url

        :param search_term: Termo que vai ser usado na pesquisa
        :return: Retorna a url da imagem
        """
        
        driver = webdriver.Firefox(options=self.options)
    
        try:
            url = f"https://www.google.co.in/search?q={search_term.replace(' ', '+')}&source=lnms&tbm=isch"
            driver.get(url)

            time.sleep(2) 
            
            images = driver.find_elements(By.CLASS_NAME, "YQ4gaf")

            url_images = [img.get_attribute("src") for img in images[:num_images] if img.get_attribute("src")]

            return url_images
        finally:
            driver.quit()


if __name__ == "__main__":
    searcher = WebSearcher()
    print(searcher.search("Dell 725y7", num_images=5))