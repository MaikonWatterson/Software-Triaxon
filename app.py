from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastrar_paciente', methods=['GET', 'POST'])
def cadastrar_paciente():
    if request.method == 'POST':
        return redirect(url_for('index'))
    return render_template('paciente_cadastro.html')

@app.route('/cadastrar_medico', methods=['GET', 'POST'])
def cadastrar_medico():
    if request.method == 'POST':
        return redirect(url_for('index'))
    return render_template('medico_cadastro.html')

@app.route('/pesquisar_paciente', methods=['GET', 'POST'])
def pesquisar_paciente():
    if request.method == 'POST':
        return render_template('resultado.html')
    return render_template('pesquisa_paciente.html')

@app.route('/pesquisar_medico', methods=['GET', 'POST'])
def pesquisar_medico():
    if request.method == 'POST':
        return render_template('resultado.html')
    return render_template('pesquisa_medico.html')

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)