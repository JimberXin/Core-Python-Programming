#coding=utf-8

import csv

from os import listdir


# @input: 一个需要保存的目标文件，如Level Smoothed at 1 kHZ
# @output: 返回一个列表，里面每一项都是文件内容

def findIndex(targetName):
    dirList = listdir('samples')  # 列出sample下所有文件夹的名字
    m = len(dirList)  # 统计有多少个文件夹(目前为3个)

    # 找出文件在当前文件夹下的索引（第几个），用index表示
    fileNameStr = listdir('samples/' + dirList[0])
    index = 0
    for j in range(len(fileNameStr)):
            if fileNameStr[j].find(targetName) != -1:
                index = j
                break

    name = []
    fileList = []   # 将所有文件保存成一个文件列表

    # 遍历每一个文件夹，将每个文件的所有内容都保存在列表fileList中，避免重复读取
    for eachCsv in range(m):
        dirNameStr = dirList[eachCsv]
        # 对于该文件夹，第index 个文件为所需要处理读写的文件
        fileName = listdir('samples/' + dirNameStr)[index]

        # 读入源文件
        csvFile = open('samples/'+dirNameStr+'/'+fileName, 'rU')
        reader = csv.reader(csvFile)
        name.append(dirNameStr)
        fileList.append(list(reader))
        csvFile.close()
    return name, fileList












