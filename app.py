import threading
import json

import tkinter as tk
import pandas as pd
from pandas.io.parsers import TextFileReader
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions 
from tkinter import filedialog
from flask import Flask, render_template, jsonify
from markupsafe import escape
from werkzeug.serving import make_server
import webview


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


def html_interface():
    window = webview.create_window("Imagizer", url="http://localhost:5000", width=1280, height=760, resizable=True)
    webview.start()


def select_csv_file():
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename(initialdir="~", title="Select a file")

    return file_path


"""
def web_search(search_term: str, num_images: int = 6) -> list:
    Pesquisa o item no google images e retorna a sua url

    :param search_term: Termo que vai ser usado na pesquisa
    :return: Retorna a url da imagem

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
"""


def save_data(data, filename: str) -> None:
    with open(filename, "w") as json_file:
        json.dump(data, json_file)


def load_data(filename: str):
    with open(filename, "r") as json_file:
        return json.load(json_file)


@app.route("/data")
def get_data():
    try:
        csv_file_path = select_csv_file()

        df: TextFileReader = pd.read_csv(csv_file_path, delimiter=";")
    
        marcas = df["Marca"].tolist()
        referencia = df["Ref"].tolist()
        
        data = df.to_dict(orient="records")

        save_data(data, "data.json")
        """
        urls = []

        for item in data:
            url_images: list = web_search(f"{item['Marca']} {item['Ref']}")
            print(url_images)
            urls.append({item["Ref"]: url_images})
        """

        return render_template("index.html", data=data)

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": str(e)}), 500



@app.route("/table")
def show_table():
    try: 
        data = load_data("data.json")

        return render_template("table.html", data=data)
    except Exception as e:
        print(f"Error: {e}")

        return jsonify({"error": str(e)}), 500

    
def run_flask_app():
    server = make_server("localhost", "5000", app)
    server.serve_forever()


if __name__ == "__main__":

    flask_theread = threading.Thread(target=run_flask_app)
    flask_theread.start()

    html_interface()
