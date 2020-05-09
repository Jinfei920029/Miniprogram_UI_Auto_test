# -*- coding:utf-8 -*-
# Author:Jin Fei
import os
import time

now = str(time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime()))
print (now)
filename1 = 'tokens_test'+now+'.txt'
filename2 = 'cloc'+now+'.txt'
reportpath1 = 'c:\\Users\\A633335\\Desktop\\report\\' + filename1
reportpath2 = 'c:\\Users\\A633335\\Desktop\\report\\' + filename2
user_path3 = "C:/Users/A633335/Desktop/pmd-bin-6.20.0/bin" #执行命令的路径
def cmd1():
    try:
        cmd1 = 'cd '+ user_path3
        cmd2 = 'cpd.bat --minimum-tokens 6 --files c:\\Users\\A633335\\Desktop\\bsh_hcwxapp_api >' + reportpath1
        cmd = cmd1 + '&&' + cmd2
        os.popen(cmd)
    except Exception as e:
        print("cpd.bat tool fail:" + str(e))

def cmd2():
    try:
        cmd1 = 'cd '+ user_path3
        cmd2 = 'cloc-1.64.exe C:\\Users\\A681549\\Desktop\\bsh_hcwxapp_api\\src\\main\\java\\com\\zencloud\\bsh >' + reportpath2
        cmd = cmd1 + '&&' + cmd2
        os.popen(cmd)
    except Exception as e:
        print("cloc tool fail:" + str(e))

cmd1()