import Stemmer
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
import string

class Indice:

    def __init__(self):
        self.stopWords = set(stopwords.words('spanish'))
        self.stemmer = SnowballStemmer("spanish")
    
    # Funcion que recibe un criterio de busqueda creando el
    # indice 
    def indexar(self, criterioDeBusqueda):
        textoTokemizado = word_tokenize(criterioDeBusqueda.lower())
        filtrandoPalabras = [palabra for palabra in textoTokemizado if not palabra in string.punctuation]
        filtrandoPalabras = [palabra for palabra in filtrandoPalabras if not palabra in self.stopWords] 
        return [self.stemmer.stem(palabra) for palabra in filtrandoPalabras]

def main():
    crearIndice = Indice()
    listaIndices = crearIndice.indexar("Hola mundo, comiendo para comer")
    #Buscar()
    print(listaIndices, )

if __name__ == "__main__":
    main()
