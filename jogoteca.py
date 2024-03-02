from flask import Flask, render_template

app = Flask(__name__)

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

@app.route('/inicio')
def ola():
    jogo1 = Jogo('COD', 'Fps', 'CONSOLE')
    jogo2 = Jogo('Free Fire', 'Fps', 'MOBILE')
    jogo3 = Jogo('Fifa 24', 'Futebol', 'Console')

    lista_jogos = [jogo1, jogo2, jogo3]
    return render_template('lista.html', titulo='Jogos', jogos=lista_jogos)

app.run(debug=True)