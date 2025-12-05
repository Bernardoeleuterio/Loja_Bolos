from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

pedidos = []

@app.route("/")
def index():
    return render_template("index.html", pedidos=pedidos)

@app.route("/adicionar", methods=["POST"])
def adicionar():
    bolo = request.form.get("bolo")
    if bolo:
        pedidos.append({"bolo": bolo, "concluido": False})
    return redirect(url_for("index"))

@app.route("/concluir/<int:indice>")
def concluir(indice):
    if 0 <= indice < len(pedidos):
        pedidos[indice]["concluido"] = True
    return redirect(url_for("index"))

@app.route("/remover/<int:indice>")
def remover(indice):
    if 0 <= indice < len(pedidos):
        pedidos.pop(indice)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
