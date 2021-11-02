# coding: utf-8
import json
import csv
import glob
import os
import pandas


class Parser:
    postId = ''

    def __init__(self):
        self.jdic = {}

    def parse_json(self, path):
        with open(path, 'r', encoding='utf-8') as file:
            return json.loads(file.read())

    def parse_errors_with_Filepath(self, l):
        for dic in l:
            for k, v in dic.items():
                if k == "filePath":
                    self.postId = self.getPostId(v)
                if k == 'ruleId':
                    self.jdic[self.postId][v] = 1 if v not in self.jdic[self.postId] else self.jdic[self.postId][v] + 1
                if isinstance(v, list):
                    self.parse_errors_with_Filepath(v)

    def parse_errors(self, l):
        for dic in l:
            for k, v in dic.items():
                if k == 'ruleId':
                    self.jdic[v] = 1 if v not in self.jdic else self.jdic[v] + 1
                if isinstance(v, list):
                    self.parse_errors(v)

    def initializeDict(self, dict):
        print("Initializing csv dict")
        for subDict in dict:
            for k, v in subDict.items():
                if k == "filePath":
                    v = self.getPostId(v)
                    self.jdic[v] = {}

    def getPostId(self, filepath: str):
        filepath = filepath.split("/").pop().split(".").pop(0)
        return filepath

    def out_to_csv_single_line(self, dic, filename, openType, headers=[]):
        with open(filename, openType, newline='') as file:
            writer = csv.DictWriter(file, dic.keys())
            writer.writeheader()
            writer.writerow(dic)

    def out_to_csv_filePath(self, dic, filename, openType, headers=[]):
        self.ExtractRules(dic, headers)
        with open(filename, openType, newline='') as file:
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writeheader()
            for x in dic:
                writer.writerow(self.createCsvDict(x, dic[x], headers))

    def ExtractRules(self, dic, headers):
        for x in dic:
            for y in dic[x]:
                if y not in headers:
                    headers.append(y)

    def createCsvDict(self, key, dic, headers):
        csvDict = {}
        for x in headers:
            csvDict[x] = ''
        csvDict['Post Id'] = key
        for keys, values in dic.items():
            csvDict[keys] = values
        return csvDict


def createRuleDict():
    csvRules = {"Best Practices": [], "ECMAScript 6": [], "Node.js and CommonJS": [], "Possible Errors": [],
                "Stylistic Issues": [], "Variables": []}
    with open("RegrasLinter.csv", "r") as csvFile:
        csvReader = csv.DictReader(csvFile)
        for row in csvReader:
            csvRules[row["Rule Classification"]].append(row["Rules"])

        return csvRules
    return {}


def aggregateRules():
    ruleDict = createRuleDict()
    aggregateRules = {"Best Practices": 0, "ECMAScript 6": 0, "Node.js and CommonJS": 0, "Possible Errors": 0,
                      "Stylistic Issues": 0, "Variables": 0}
    with open("allrules.csv", "r") as csvFile:
        reader = csv.reader(csvFile)
        FieldNames = []
        values = []
        for index, row in enumerate(reader):
            if index == 0:
                FieldNames = row
            else:
                values = row
        for y in ruleDict:
            for x in zip(FieldNames, values):
                if x[0] in ruleDict[y]:
                    aggregateRules[y] += int(x[1])
    with open("aggregatedRules.csv", "w") as csvFile:
        writer = csv.DictWriter(csvFile, aggregateRules)
        writer.writeheader()
        writer.writerow(aggregateRules)


def mostCommonErrorsPerCategory():
    ruleDict = createRuleDict()
    rules = {"Best Practices": [], "ECMAScript 6": [], "Node.js and CommonJS": [], "Possible Errors": [],
             "Stylistic Issues": [], "Variables": []}
    with open("allrules.csv", "r") as csvFile:
        reader = csv.reader(csvFile)
        FieldNames = []
        values = []
        for index, row in enumerate(reader):
            if index == 0:
                FieldNames = row
            else:
                values = [int(x) for x in row]
        for y in ruleDict:
            for x in zip(FieldNames, values):
                if x[0] in ruleDict[y]:
                    rules[y].append(x)
        for y in ruleDict:
            rules[y].sort(key=lambda tup: tup[1], reverse=True)
        print(rules.keys())
    with open("MostCommonRule.csv", "w") as csvFile:
        writer = csv.DictWriter(csvFile, rules.keys())
        writer.writeheader()
        writer.writerow(rules)


def getPossibleErrorsIDs():
    ruleDict = createRuleDict()
    ruleIDs = {"PostID": []}
    with open("PersonalizedIndividualReportFixed.csv", "r") as csvFile:
        reader = csv.DictReader(csvFile)
        for index, row in enumerate(reader):
            for x in ruleDict["Possible Errors"]:
                if row[x] != '':
                    ruleIDs["PostID"].append(row["Post Id"])
                    break
    with open("possibleErrorsID.csv", 'w') as errorsFile:
        writer = csv.DictWriter(errorsFile, ruleIDs.keys())
        writer.writeheader()
        idList = ruleIDs["PostID"]
        print(idList)
        for x in idList:
            print(x)
            writeDict = {"PostID": x}
            writer.writerow(writeDict)


def parseErrorsSingle(jsonFiles):
    parser = Parser()
    for x in jsonFiles:
        parser.parse_errors(x)
    parser.out_to_csv_single_line(parser.jdic, "singleLineRuleViolations.csv", "w")


def parseFilePathRules(jsonfiles):
    parser = Parser()
    for idx, x in enumerate(jsonfiles):
        print("parsing snippet{}".format(idx))
        parser.initializeDict(x)
        parser.parse_errors_with_Filepath(x)
    parser.out_to_csv_filePath(parser.jdic, 'PersonalizedIndividualReportFixed.csv', 'w', ["Post Id"])


parser = Parser()
l = []
os.chdir("./files")
fileDir = glob.glob('report*.json')
z = 0
menu = True
getPossibleErrorsIDs()

while(menu):
    print("Menu")
    print("Do you want to load the reports ?")
    userInput = input("yes/no")
    if userInput.lower().lstrip().rstrip()=="yes":
        for idx, x in enumerate(fileDir):
            print("Reading json Reports{}...".format(idx))
            l.append(parser.parse_json(x))
        print("Parse Errors json with rule count in one line : 1")
        print("Parse Errors json with filepath count:2")
        userInput = input("Select an option")
    elif userInput.lower().lstrip().rstrip()=="no":
        print("Aggregate rules:1")
        print("Most Common Errors :2")
        print("Exit : 3")
        userInput=input("Select an option")
        if userInput =="1":
            aggregateRules()
        if userInput =="2":
            mostCommonErrorsPerCategory()
        if userInput=="3":
            exit(0)
        if userInput=="4":
            getPossibleErrorsIDs()