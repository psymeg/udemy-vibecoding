from flask import Flask, render_template, request
import os
import threading
import pyautogui
from deepface import DeepFace

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <html>
    <head>
        <title>Script Launcher</title>
        <style>
            body { background-color: orange; text-align: center; font-family: Arial; }
            button { font-size: 20px; margin: 10px; padding: 10px; }
        </style>
    </head>
    <body>
        <h1>Script Launcher</h1>
        <form action="/jiggle" method="post"><button type="submit">Start Mouse Jiggler</button></form>
        <form action="/scan" method="post"><button type="submit">Scan Photos</button></form>
    </body>
    </html>
    '''

def is_man(image_path):
    try:
        analysis = DeepFace.analyze(image_path, actions=["gender"], enforce_detection=False)
        return analysis[0]['dominant_gender'] == "Man"
    except Exception as e:
        print(f"Error analyzing {image_path}: {e}")
        return False

@app.route('/scan', methods=['POST'])
def scan_images():
    directory = "/share/photos"
    if not os.path.exists(directory):
        return "Directory not found."
    
    results = []
    for root, _, files in os.walk(directory):
        for filename in files:
            if filename.lower().endswith((".jpg", ".png", ".jpeg")):
                image_path = os.path.join(root, filename)
                result = f"{image_path}: {'Man detected' if is_man(image_path) else 'Not a man'}"
                results.append(result)
    
    return "<br>".join(results)

@app.route('/jiggle', methods=['POST'])
def start_jiggler():
    def jiggle_mouse():
        while True:
            pyautogui.moveRel(5, 0, duration=0.2)
            pyautogui.moveRel(-5, 0, duration=0.2)
    
    threading.Thread(target=jiggle_mouse, daemon=True).start()
    return "Mouse jiggler started!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

