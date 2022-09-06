from aula7_parte2 import Televisao
from Aula7_parte1 import Calculadora
from Aula8_contador_letras import contador_letras, teste

#com esta linha nós interagimos com arquivo Aula7_parte2.py
#importando apenas do arquivo Aula7_parte2.py a classe Televisao
# para fazer o import sem traceback colocar o nome doa arquivo sem .py no final
# no import contador_letras utilizamos a ',' para importar mais de uma função
# e fizemos o mesmo com a Aula7_parte1.py importando a classe Calculadora


if __name__ == '__main__':
    #utilizando a classe Televisao do arquivo Aula7_partte2.py
    televisao = Televisao()
    print(televisao.ligada)
    televisao.power()
    print(televisao.ligada)

    #utilizando a classe Calculadora do arquivo Aula7_partte2.py
    calculadora = Calculadora ()
    print(calculadora.soma(10, 2) )

    #utilizando a função do arquivo aula8_contador_letras
    lista = ['cachorro', 'gato', 'elefante']
    total_letras = contador_letras(lista)
    print('Total de letras por palavras da lista: {}'.format(total_letras))

    #utilizando a função teste do arquivo Aula8_contador_letras
    print(teste())