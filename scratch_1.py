import subprocess
import os
import glob, shlex

os.chdir("./files")
ArgsList = []
args = shlex.split('npx eslint 65083754.js -f json -o report1.json')
ArgsList.append(args)
processList = [subprocess.Popen(argsToRun, shell=True) for argsToRun in ArgsList]
for proc in processList:
    proc.wait()