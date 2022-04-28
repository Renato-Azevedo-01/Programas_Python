from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")                                           #route Decorator
def homepage():                                           #Function
    return render_template("homepage.html")

@app.route("/empresa")
def empresa():
    return render_template("empresa.html")

@app.route("/contatos")
def contatos():
    return render_template("contatos.html")

@app.route("/<nome_usuario>")
def usuarios(nome_usuario):
    return render_template("usuarios.html" , nome_usuario = nome_usuario)

#Colocando o site no ar
if __name__ == "__main__" :
    app.run(debug=True)

