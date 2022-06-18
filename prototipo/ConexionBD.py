from collections import OrderedDict

dicIndices = {  'mund': ['volcanes.pdf', 'naturaleza.pdf'], 
                'verd': ['pintura_organica.pdf', 'naturaleza.pdf'], 
                'tecnolog': ['Oracle.pdf', 'CSS.pdf', 'SQL.pdf', 'Estructuras de datos.pdf'], 
                'requer': ['Oracle.pdf', 'clean_Code.pdf'],
                'tierr': ['mundo.pdf', 'volcanes.pdf'],
                'salt': ['100cm.pdf', 'Dejate caer.pdf'],
                'vaci': ['Espacio.pdf', 'NASA.pdf']}

def buscar(listaIndices):
    dicSalida = {}
    for indice in listaIndices:
        if indice in dicIndices:
            for documento in dicIndices[indice]:
                if documento in dicSalida:
                    dicSalida[documento] += 1
                else:
                    dicSalida.update({documento : 1})

    return OrderedDict(sorted(dicSalida.items()))


def main():
    valor = buscar(['requer', 'tecnologi'])
    for n in valor.values():
        print(n)

if __name__ == "__main__":
    main()