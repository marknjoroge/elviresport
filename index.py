from flask import Flask, render_template

app = Flask(__name__)

products = {
    "resistance-band": [
        "../static/images/logo.png",
        "../static/images/logo.png",
        "../static/images/logo.png",
        "../static/images/logo.png",
        "../static/images/logo.png",
        "../static/images/logo.png",
        "../static/images/logo.png",
        "../static/images/logo.png",
    ],
    "foam-roller-set": [
        "../static/images/logo.png",
        "../static/images/foamrollerset.webp",
        "../static/images/foamrollerset.webp",
        "../static/images/foamrollerset.webp",
        "../static/images/foamrollerset.webp",
        "../static/images/foamrollerset.webp",
        "../static/images/foamrollerset.webp",
        "../static/images/logo.png",
    ],
}


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/<product>")
def product(product):
    for key, value in products.items():
        if key == product:
            return render_template("buy.html", product=product, images=value)
    return render_template("notfound.html")


if __name__ == "__main__":
    app.run(host="localhost", port=8000, debug=True)
