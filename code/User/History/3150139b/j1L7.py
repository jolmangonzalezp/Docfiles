from flask import Flask, send_from_directory

app = Flask(__name__, static_folder="static", static_url_path="/")

# Ruta para servir Vue (index.html)
@app.route("/")
def index():
    return send_from_directory(app.static_folder, "index.html")

# Rutas API (ejemplo)
@app.route("/api/saludo")
def saludo():
    return {"mensaje": "Hola desde Flask"}

if __name__ == "__main__":
    app.run(debug=True)
