#/usr/bin/python
#coding=utf-8
import os


dirs = os.listdir(".")
for d in dirs:
    os.chdir(d)
    dirs_l2 = os.listdir(".")
    for dl2 in dirs_l2:
        os.chdir(dl2)
        os.system("enca -L zh_CN -x UTF8 *.txt")
        os.chdir("..")
    os.chdir("..")

