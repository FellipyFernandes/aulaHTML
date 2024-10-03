from flask import (Flask, request) 

app = Flask(__name__)

@app.route("/", methods=('GET',))
def index():
    nome = request.args.get('nome')
    return f"""<h1>Página inicial</h1> <p>Eu sou o Pajé</p>
        <p>Olá {nome}, que nome bonito!
    """
@app.route("/galeria", methods=('GET',))
def galeria():
    return "<h1>Galeria</h1>"

@app.route("/contato", methods=('GET',))
def contato():
    return "<h1>Contato (17) 99222-3333</h1>"

@app.route("/sobre", methods=('GET',))
def sobre():
    return "<h1>Sobre...</h1>"
    