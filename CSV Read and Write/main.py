#coding=utf-8

'''
安装完python，在shell下或者编译器（强烈推荐PyCharm)下跑main.py就行了。
main.py调用了getFileList，注意如果是mac下，系统会在sample下自动生成.DS_Store，
需要把该文件删掉，如果不想每次改动编译文件都生成此文件，可以百度下方法
=====================================================================================

源文件：

1: main.py
主要包括5个需要生成的文件的函数，每个函数都调用了fileList,传入文件名字，返回所有文件的列表以及文件名
读完文件后，需要将这些文件内容进行合并，所有函数的差别也都只在这一项，主要改写的是，
从文件的哪一行开始读取，读取哪一列，然后写入文件


2: getFileList.py
# @input: 一个需要保存的目标文件，如Level Smoothed at 1 kHZ
# @output: 返回文件名字，以及一个列表，里面每一项都是文件内容

'''
import csv
import getFileList


# 读取文件的第4行第2列
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


# 从第5行开始，提取第2列和第4列
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


# 从第5行开始，提取第2列和第4列
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


# 提取第4和第5行的第2列和第4列
def Sensitivity():
    target = 'Sensitivity at 1 kHz'
    nameList, fileList = getFileList.findIndex(target)
    saveFile = open(target+'.csv', 'wb')        # 文件写入file中
    name = []

    '''
    for i in range(len(nameList)):
        name.append(nameList[i])
        name.append(' ')  # 此个文件下，第一行是每隔一个名字有个空格
    '''

    writer = csv.writer(saveFile, dialect="excel")
    writer.writerow(nameList)  # 第一行写入各个文件夹的名字
    fileNum = len(fileList) # 文件总个数
    lineNum = len(fileList[0])  # 每个文件的行数
    for i in range(3, lineNum):
        line = []
        for eachCsv in range(fileNum):
            '''
            所有需要改动的代码几乎都在这里，根据每个文件你需要提取的不同的列数，在这里添加代码
            比如对于Level Smoothed,这里是提取从第四行开始到最后一行的第2列（下标为1）和第4列（下标为3）
            '''
            line.append(fileList[eachCsv][i][1])
        writer.writerow(line)

    saveFile.close()


# 从第5行开始，第2列和第4列
def THD_Ratio():
    target = 'THD Ratio 200 Points'
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


# 分别调用这5个函数
def main():
    Channel_Matching()
    Level_Smoothed()
    Normalized_Level()
    Sensitivity()
    THD_Ratio()


if __name__ == '__main__':
    main()

