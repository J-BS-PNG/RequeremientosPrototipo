from collections import OrderedDict

dicIndices = {  'mund': ['volcanes.pdf', 'naturaleza.pdf'], 
                'verd': ['pintura_organica.pdf', 'naturaleza.pdf'], 
                'tecnolog': ['Oracle.pdf', 'CSS.pdf'], 
                'requer': ['Oracle.pdf', 'clean_Code.pdf']}

def buscar(listaIndices):
    file = open('datos.txt')
    dicSalida = {}
    for indice in listaIndices:
        if indice in dicIndices:
            for documento in dicIndices[indice]:
                if documento in dicSalida:
                    dicSalida[documento] += 1
                else:
                    dicSalida.update({documento : 1})

    return sorted(dicSalida.items())


def main():
    valor = buscar(['requer', 'tecnologi'])
    print(valor)

if __name__ == "__main__":
    main()