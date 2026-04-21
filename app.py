from flask import Flask, request, render_template , redirect

app = Flask(__name__)
estoque = {} # dicionario pra guardar produtos

@app.route('/')
def index():
    return  render_template("index.html", produtos = estoque)

@app.route("/adicionar" , methods=["POST"])
def adicionar():
    nome = request.form["nome"]
    qtd = int(request.form["quantidade"])
    estoque[nome] = estoque.get(nome, 0) + qtd
    return redirect("/")
@app.route("/remover" , methods=["POST"])
def remover():
    nome = request.form["nome"]
    qtd = int(request.form["quantidade"])
    if nome in estoque and estoque[nome] >= qtd:
        estoque[nome] -= qtd
        if estoque[nome] == 0:
            del estoque[nome]
    return redirect("/")
@app.route("/apagar" , methods=["POST"])
def apagar():
    nome = request.form["nome"]
    if nome in estoque:
        del estoque[nome]
    return redirect("/")
@app.route("/editar" , methods=["POST"])
def editar():
    nome = request.form["nome"]
    addQtd = int(request.form["quantidade"])
    if nome in estoque:
        estoque[nome] = addQtd
    return redirect("/")

@app.route("/consultar/<nome>")
def consultar(nome):
    qtd = estoque.get(nome, 0)
    return  f":{nome}:  , {qtd} unidades"