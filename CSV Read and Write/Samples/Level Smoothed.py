#coding=utf-8

import csv

from os import listdir


def findIndex(targetName):
    dirList = listdir('samples')  # 列出sample下所有文件夹的名字
    target = 'Channel Matching at 1kHz'
    m = len(dirList)  # 统计有多少个文件夹
    saveFile = file('Channel Matching at 1kHz.csv', 'wb')

    # 遍历每一个文件夹
    for i in range(m):
        dirNameStr = dirList[i]
        # 对于每个文件夹，列出所有文件的名字
        fileNameStr = listdir('samples/' + dirNameStr)

        # index 为找到每个文件夹中，想找的文件的索引
        index = 0
        for j in range(len(fileNameStr)):
            if fileNameStr[j].find(targetName) != -1:
                index = j
                break

        fileName = fileNameStr[index]
        print fileName

        writer = csv.writer(saveFile)
        writer.join(fileName)
        writer.





