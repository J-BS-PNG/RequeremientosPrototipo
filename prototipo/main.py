from flask import Flask, render_template, request
import logica

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', datos = listaIndice )

@app.route('/About')
def about():
    return render_template('about.html')

@app.route('/result', methods = ['POST', "GET"])
def result():
    indice = logica.Indice()
    output = request.form.to_dict()
    texto = output["Criterio"]
    listaIndice = indice.indexar(texto)
    print(listaIndice)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)