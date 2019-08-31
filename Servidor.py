from flask import Flask, render_template, request
from Biblioteca import Cliente
app = Flask(__name__, static_url_path='', static_folder='templates')
app.config['SECRET_KEY'] = '43r78934yt6y5907'

ListaClientes = [
    Cliente("Lonteiro Mobato", "lonteiro123@gmail.com", "(51) 99322-1242", "Aluno")
]

@app.route("/")
def Home():
    return render_template("Main.html")

@app.route("/CadastroCliente")
def CadastroCliente():
    return render_template("CadastroCliente.html", lista = ListaClientes)

@app.route("/AdicionarCliente", methods=['POST'])
def AdicionarCliente():
    nome = request.form["Nome"]
    email = request.form["Email"]
    tel = request.form["Telefone"]
    tipo = request.form["Tipo"]
    ClienteNovo = Cliente(nome, email, tel, tipo)
    ListaClientes.append(ClienteNovo)
    return render_template("Sucesso.html", mensagem="Cliente Salvo!")

@app.route("/CadastroLivro")
def CadastroLivro():
    return render_template("CadastroLivro.html")

@app.route("/Emprestimo")
def Emprestimo():
    return render_template("Emprestimo.html")

@app.route("/Sucesso")
def Sucesso():
    return render_template("Sucesso.html")

@app.route("/Erro")
def Erro():
    return render_template("Erro.html")
    
app.run(host="0.0.0.0")
app.run(debug=True)
