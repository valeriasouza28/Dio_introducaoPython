import shutil
def escrever_arquivo(texto):

    #vamos usar open para abrir um arquivo que já existe
    #Ou para criar um arquivo que ainda não existe
    # Para fazer a leitura utilizamos o nome do arquivo e um modo
    #um modo pode ser para leitura, escrita, salvar enfim.
    #com o modo 'w' ele vai sobrepor o que jáexiste
    # Para fazer uma actualization sem sobrepor 'a'
    diretorio = '/home/oem/introducao_Python_DIO/Aula9/teste.txt'
    arquivo = open(diretorio, 'w')

    #E utilizamos arquivo.write, onde arquivo é a variável que recebeu o arquivo teste.txt
    # e utilizamos o write para escrever dentro desse arquivo teste,txt.
    #arquivo.write('Minha primeira escrita')
    #Para escrever na segunda linha do arquivo utilizamos \n para passar para a pŕoxima  linha em seguida escrevemos o contéúdo da segunda linha
    arquivo.write(texto)
    #arquivo.close é para fechar o arquivo
    arquivo.close()

def atualizar_arquivo(nome_arquivo, texto):
    arquivo = open(nome_arquivo, 'a')
    arquivo.write(texto)
    arquivo.close()

def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)

def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    aluno_nota = arquivo.read()
    #print(aluno_nota)
    aluno_nota = aluno_nota.split('\n')
    lista_media = []
    #print(aluno_nota)
    for x in aluno_nota:
        lista_notas = x.split(',')
        aluno = lista_notas[0]
        lista_notas.pop(0)
        print(aluno)
        print(lista_notas)
        media = lambda notas: sum([int(i) for i in notas]) /4
        print(media(lista_notas))
        lista_media.append({aluno:media(lista_notas)})
    return lista_media
        #print(sum(lista_notas))

def copia_arquivo (nome_arquivo):

    shutil.copy(nome_arquivo, 'home/oem/introducao_Python_DIO/notas.txt')

def move_arquivo (nome_arquivo):
    shutil.move(nome_arquivo, '/home/oem/introducao_Python_DIO/notas_aluno.txt')

if __name__ == '__main__':
    #move_arquivo('notas.txt')
    #copia_arquivo('notas.txt')
    #lista_media = media_notas('notas.txt')
    #print(lista_media)
    #escrever_arquivo('Primeira linha.\n')
    aluno = ' Cesar, 7, 9, 3, 8\n'
    atualizar_arquivo('notas.txt', aluno)
    #ler_arquivo('teste.txt')