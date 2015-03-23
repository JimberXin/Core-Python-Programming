__author__ = 'JimberXin'

import csv
from os import listdir


def findIndex(targetName):
    dirList = listdir('samples')
    m = len(dirList)
    for i in range(m):
        dirNameStr = dirList[i]  # current directory name
        fileNameStr = listdir('samples/'+dirNameStr)

        # find the index of the file
        index = 0
        for j in range(len(fileNameStr)):
            if fileNameStr[j].find(targetName) != -1:
                index = j
                break
        print dirNameStr
        fileName = fileNameStr[index]
        print fileName
        return dirNameStr, fileName

