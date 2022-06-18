from flask import Flask, render_template, request
import logica
import ConexionBD

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/result', methods = ['POST', "GET"])
def result():
    indice = logica.Indice()
    output = request.form.to_dict()
    texto = output["Criterio"]
    if texto != '':
        listaIndice = indice.indexar(texto)
        documentos = ConexionBD.buscar(listaIndice)
        print(listaIndice)
        print(documentos)
        return render_template('IndexData.html', datos = [documentos])
    else:
        return render_template('index.html', datos = [])

if __name__ == '__main__':
    app.run(debug=True)