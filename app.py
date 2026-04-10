from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/productos")
def productos():
    return render_template("productos.html")

@app.route("/nosotros")
def nosotros():
    return render_template("nosotros.html")

@app.route("/detalles")
def detalles():
    return render_template("detalles.html")


if __name__ == "__main__":
    app.run(debug=True)
