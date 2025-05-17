import os
from flask import Flask, request, redirect, render_template
import pandas as pd

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Crie a pasta uploads se não existir
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def home():
    return render_template("upload.html")

@app.route("/upload", methods=["POST"])
def upload_file():
    if 'arquivo_excel' not in request.files:
        return "Nenhum arquivo enviado", 400
    
    file = request.files['arquivo_excel']
    
    if file.filename == "":
        return "Nome de arquivo inválido", 400

    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)

    # 🧠 Aqui você pode processar o Excel com pandas
    df = pd.read_excel(filepath)
    media_idade = df["Idade"].mean()
    return f"Média de idade: {media_idade:.2f}"

if __name__ == "__main__":
    app.run(debug=True)
