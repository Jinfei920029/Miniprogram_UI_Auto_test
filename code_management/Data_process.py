# -*- coding:utf-8 -*-
# Author:Jin Fei
import os
import time
import re
report1_psth = "C:\\Users\\A633335\\Desktop\\report\\code_20200327.txt.txt"
report2_path = "C:\\Users\\A633335\\Desktop\\report\\total_code_line.txt"
fileName1 = report1_psth
fileName2 = report2_path
#读取 fileName3 自己得文件路径

def loadData1(fileName):
    key = "Found"
    with open(fileName, encoding='gb18030') as txtData:
        lines=txtData.readlines()
        num = 0
        for line in lines:
            if key in line:
                line=line.strip()#去除空行
                list = re.findall(r'\b\d+\b' , line)#取出数字
                #print(list)
                #print(list[0])
                num = num + int(list[0])
    return num

def get_codeline(fileName):
    key = "Java"
    list_end = []
    with open(fileName, encoding='gb18030') as txtData:
        lines=txtData.readlines()
        for line in lines:
            if key in line:
                line=line.strip()#去除空行
                list = re.findall(r'\b\d+\b' , line)#取出数字
                list_end.append(list[-1])
    return list_end[-1]

line1 = loadData1(fileName1)
line2 = get_codeline(fileName2)
code_repetion_rate = int(line1)/int(line2)
print('Code_repetion_rate:'+ str(code_repetion_rate)+'\n','Data1:'+ str(loadData1(fileName1))+'\n','Data2:'+ str(get_codeline(fileName2)))
