from app import app
from flask import render_template, url_for

@app.route("/")
def homepage():
    usuario = 'Camp Code'
    idade = 34

    context = {
        'usuario': usuario,
        'idade': idade
    }
    return render_template('index.html', **context)

@app.route("/contato")
def nova():
    return "nova"