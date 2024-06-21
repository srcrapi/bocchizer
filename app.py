import threading

import tkinter as tk
import pandas as pd
from pandas.io.parsers import TextFileReader
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions 
from tkinter import filedialog
from flask import Flask, render_template, jsonify
from markupsafe import escape
from werkzeug.serving import make_server
# import webview


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


"""
def html_interface():
    window = webview.create_window("Imagizer", url="127.0.0.1:5000", width=1580, height=760, resizable=False)
    webview.start()
"""


def select_file():
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename(initialdir="~", title="Select a file")

    return file_path


def check_driver():
    firefox_found = False
    chrome_found = False

    try:
        ChromeDriverManager().install()
        chrome_found = True
    except:
        pass


    try:
        GeckoDriverManager().install()
        firefox_found = True
    except:
        pass


    if firefox_found and chrome_found:
        return "firefox"
    
    if firefox_found:
        return "firefox"

    if chrome_found:
        return "chrome"

def web_search(search_term: str, num_images: int = 6) -> list:
    """
    Pesquisa o item no google images e retorna a sua url

    :param search_term: Termo que vai ser usado na pesquisa
    :return: Retorna a url da imagem
    """

    driver_to_use = check_driver()

    chrome_options = Options()
    chrome_options.add_argument("--headless")

    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

    try:
        driver.get("https://www.google.com/imghp")

        search_box = WebDriverWait(drive, 10).until(
            EC.presence_of_element_located((By.NAME, "q"))
        )
        search_box.send_keys(search_term)
        search_box.send_keys(Keys.RETURN)

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'img.rg_i'))
        )

        drive.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'img.rg_i'))
        )

        images = driver.find_element_by_css_selector("img.rg_i")

        url = [img.get_attribute("src") for img in imagens[:num_images]]

        return url
    finally:
        driver.quit()


@app.route("/dados")
def get_data():
    try:
        csv_file_path = select_file()

        df: TextFileReader = pd.read_csv(csv_file_path, delimiter=";")
    
        marcas: list[str] = df["Marca"].tolist()
        referencia: list[str] = df["Ref"].tolist()
    
        data: list[dict] = df.to_dict(orient="records")
        
        urls = []

        for item in data:
            url_images: list = web_search(f"{item['Marca']} {item['Ref']}")
            print(url_images)
            urls.append({item["Ref"]: url_images})

        return jsonify(urls)

    except Exception as e:
        print(f"Error: {e}")

    
def run_flask_app():
    server = make_server("localhost", "5555", app)
    server.serve_forever()


if __name__ == "__main__":

    flask_theread = threading.Thread(target=run_flask_app)
    flask_theread.start()

    #html_interface()
