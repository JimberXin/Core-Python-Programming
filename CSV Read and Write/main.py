#coding=utf-8

import csv
import getFileList


def Channel_Matching():
    target = 'Channel Matching at 1 kHz'
    name, fileList = getFileList.findIndex(target)
    saveFile = open(target+'.csv', 'wb')        # 文件写入file中
    writer = csv.writer(saveFile, dialect="excel")
    writer.writerow(name)  # 第一行写入各个文件夹的名字
    fileNum = len(fileList)  # 文件总个数
    lineNum = len(fileList[0])  # 每个文件的行数
    line = []

    # 对于channel只有一个数据需要提取，所以遍历每个文件就行了
    for eachCsv in range(fileNum):
        '''
        所有需要改动的代码几乎都在这里，根据每个文件你需要提取的不同的列数，在这里添加代码
        比如对于Level Smoothed,这里是提取从第四行开始到最后一行的第2列（下标为1）和第4列（下标为3）
        '''
        line.append(fileList[eachCsv][3][1])

    writer.writerow(line)
    saveFile.close()


# 从第4行开始，提取第2列和第4列
def Level_Smoothed():
    target = 'Level Smoothed at 1 kHz'
    nameList, fileList = getFileList.findIndex(target)
    saveFile = open(target+'.csv', 'wb')        # 文件写入file中
    name = []
    for i in range(len(nameList)):
        name.append(nameList[i])
        name.append(' ')  # 此个文件下，第一行是每隔一个名字有个空格

    writer = csv.writer(saveFile, dialect="excel")
    writer.writerow(name)  # 第一行写入各个文件夹的名字
    fileNum = len(fileList) # 文件总个数
    lineNum = len(fileList[0])  # 每个文件的行数
    for i in range(4, lineNum):
        line = []
        for eachCsv in range(fileNum):
            '''
            所有需要改动的代码几乎都在这里，根据每个文件你需要提取的不同的列数，在这里添加代码
            比如对于Level Smoothed,这里是提取从第四行开始到最后一行的第2列（下标为1）和第4列（下标为3）
            '''
            line.append(fileList[eachCsv][i][1])
            line.append(fileList[eachCsv][i][3])
        writer.writerow(line)

    saveFile.close()


# 从第4行开始，提取第2列和第4列
def Normalized_Level():
    target = 'Normalized Level at 1 kHz'
    nameList, fileList = getFileList.findIndex(target)
    saveFile = open(target+'.csv', 'wb')        # 文件写入file中
    name = []
    for i in range(len(nameList)):
        name.append(nameList[i])
        name.append(' ')  # 此个文件下，第一行是每隔一个名字有个空格

    writer = csv.writer(saveFile, dialect="excel")
    writer.writerow(name)  # 第一行写入各个文件夹的名字
    fileNum = len(fileList) # 文件总个数
    lineNum = len(fileList[0])  # 每个文件的行数
    for i in range(4, lineNum):
        line = []
        for eachCsv in range(fileNum):
            '''
            所有需要改动的代码几乎都在这里，根据每个文件你需要提取的不同的列数，在这里添加代码
            比如对于Level Smoothed,这里是提取从第四行开始到最后一行的第2列（下标为1）和第4列（下标为3）
            '''
            line.append(fileList[eachCsv][i][1])
            line.append(fileList[eachCsv][i][3])
        writer.writerow(line)

    saveFile.close()


def main():
    Channel_Matching()
    Level_Smoothed()


if __name__ == '__main__':
    main()

