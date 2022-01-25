import subprocess
import os
import glob
import shlex


def runLinter():
    #mudar caminho dir
    path = "/home/ingridmoreira/Documentos/TCC/git-tcc/projeto_tcc/files"

    os.chdir(path)
    fileList = glob.glob('*.html')
    fileList = listSplit(fileList, 20)
    reportNumber = 0
    ArgsList = []
    # print(fileList)
    # arg_list = [['./node_modules/eslint/bin/eslint.js'+fileName+'-f json -o report.json'] for fileName  in fileList]
    
    #leitura das files com o linter 'pa11y'
    #necessário instalar pa11y
    for x in fileList:
        args = shlex.split('pa11y --reporter csv {}{} >  report{}.csv'.format(path, "".join(x), reportNumber))
        reportNumber += 1
        ArgsList.append(" ".join(args))
    print("args", " ".join(args))
    processList = [subprocess.Popen(argsToRun, shell=True)
                   for argsToRun in ArgsList]

    print("arglist", ArgsList)
    print("process ", processList)

    for proc in processList:
        proc.wait()
        print('proc:', proc.wait())


def listSplit(listToSplit: list, countSplit: int):
    length = len(listToSplit)
    print(length)
    splitlist = []
    for x in range(countSplit):
        splitlist.append(
            listToSplit[length * x // countSplit: (x + 1) * length // countSplit])
    return splitlist


if __name__ == "__main__":
    runLinter()
