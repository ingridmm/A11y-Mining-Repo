import csv
import itertools

"""
Initial Function to start reading the CSV file with all the codes.
"""
def replaceNewLine(row):
    if '&#xD;&#xA;' in row:
        rowReplaced = row.replace('&#xD;&#xA;','\n')
        return rowReplaced

def openFileAndCreateDictionary(fileName):
    codeList = {}
    with open(fileName, newline='',encoding="utf8") as csvFile:
        csvFile.readline()
        codeList = readCSVFile(codeList,csvFile)
    return codeList



def readCSVFile(codeList, csvFile):
    rowReader = csv.reader(csvFile, delimiter=',')

    for row in rowReader:
        print(row)
        codeList[row[0]] = [row[1]]

    return codeList
def writeCodeFiles(codeList):
    for keys in codeList:
        for content in codeList[keys]:
           # print(content)
            with open("files/" + keys+".html","a",encoding="utf8") as codeFile:
               # print(content)
                codeFile.write(content)

codelist = openFileAndCreateDictionary('html.csv')

writeCodeFiles(codelist)