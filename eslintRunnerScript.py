import subprocess
import os
import glob
import shlex
import os

def runLinter():
    
    path = '/home/ingridmoreira/Documentos/Teste_Final'      # Mudar caminho do diretório conforme necessidade!

    os.chdir(path)
    fileList = glob.glob('*.html')
    fileList = listSplit(fileList, 20)
    reportNumber = 0
    ArgsList = []
    """ 
    for p, _, files in os.walk(os.path.abspath(path)):
        for file in files:
            print(os.path.join(p, file))
            print(os.path.splitext(file)[0])
 """

    # Listar arquivos para multiplos diretórios
    # Path recursivo + arquivo
    for p, _, files in os.walk(os.path.abspath(path)):
        for file in files:
            args = shlex.split('pa11y --reporter csv {} >  {}.csv'.format(os.path.join(p, file), os.path.splitext(file)[0]))   # Incrementa no '{}' cada caminho do arquivo no diretório
            reportNumber += 1
            filename = os.path.basename(path)
            ArgsList.append(" ".join(args))
            print("args", " ".join(args))
    processList = [subprocess.Popen(argsToRun, shell=True) for argsToRun in ArgsList]

    print("arglist", ArgsList)
    print("process ", processList)

    for proc in processList:
        proc.wait()
        print('proc:', proc.wait())


def listSplit(listToSplit: list, countSplit: int):
    length = len(listToSplit)
    print('tamanho: ',length)
    splitlist = []
    for x in range(countSplit):
        splitlist.append(
            listToSplit[length * x // countSplit: (x + 1) * length // countSplit])
    return splitlist


if __name__ == "__main__":
    runLinter()
