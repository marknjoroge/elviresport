from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/<product>")
def product(product):
    return f"this product"

if __name__ == "__main__":
    app.run()