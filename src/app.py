import threading
import json

import tkinter as tk
import pandas as pd
import chardet
from tkinter import filedialog
from flask import Flask, render_template, jsonify
from werkzeug.serving import make_server
import webview

from components.web_searcher import ImageDownloader


app = Flask(__name__)
image_downloader = ImageDownloader()

@app.route("/")
def index():
    return render_template("index.html")


def html_interface():
    webview.create_window("Bocchizer", url="http://localhost:5000", width=1280, height=760, resizable=True)
    webview.start()


def select_csv_file():
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename(initialdir="~", title="Select a file", filetypes=[("CSV files", "*.csv")])

    return file_path


def save_data(data, filename: str) -> None:
    with open(filename, "w") as json_file:
        json.dump(data, json_file)


def load_data(filename: str):
    with open(filename, "r") as json_file:
        return json.load(json_file)


def detect_enconding(file_path: str):
    with open(file_path, "rb") as file:
        result = chardet.detect(file.read())

    return result["encoding"]



@app.route("/data")
def get_data():
    try:
        csv_file_path = select_csv_file()
        enconding = detect_enconding(csv_file_path)

        df = pd.read_csv(csv_file_path, delimiter=";", encoding=enconding)

        data = df.to_dict(orient="records")

        save_data(data, "data.json")

        for item in data:
            result, program_path = image_downloader.create_folder(
                {item['Ref']: f"{item['Marca']} {item['Ref']}"},
                num_image=6
            )

        return jsonify({"result": result, "program_path": program_path}), 200

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
    server = make_server("localhost", 5000, app)
    server.serve_forever()


if __name__ == "__main__":
    flask_theread = threading.Thread(target=run_flask_app)
    flask_theread.start()

    html_interface()
