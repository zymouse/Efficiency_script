#!/usr/bin/env python  
# -*- coding:utf-8 -*-
import os
import re

class readFileABSPathList:
    # 获取一个有序的文件绝对路径列表--有序根据文件前缀数字
    def __init__(self):
        self.file_absPath = list()
        self.scanfile(self.read_file_path("input/flm_sweeping_scripts-master"))
        self.file_absPathSortMap={}
        self.readFilePrefixNumber()
        # self.SortFilePathList = [filePath for filePath in self.file_absPathSortMap]

    @staticmethod
    def read_file_path(relative_path):
        # 读取当前文件夹路径并去除文件路径的文件名
        current_path = os.path.dirname(os.path.abspath(__file__))
        # 链接文件
        return os.path.join(current_path, relative_path)

    # 递归读取所有文件绝对路径
    def scanfile(self, path):
        for filename in os.listdir(path):
            filepath = os.path.join(path, filename)
            if os.path.isdir(filepath):
                self.scanfile(filepath)

            if not os.path.isdir(filepath):
                self.file_absPath.append(filepath) 

    # 根据绝对路径的中的文件名称前缀路径的数字--有序列表
    def readFilePrefixNumber(self):
        for i in self.file_absPath:
            res = re.sub('\D.*', '', os.path.basename(i))
            self.file_absPathSortMap[int(res)] = i
        # for i in range(len(self.file_absPathSortMap))
        


fileSortAbsMap =  readFileABSPathList()

if __name__ == '__main__':
    
    # for i in fileSortAbsMap.file_absPathSortMap.values():
    #     print(i)
    print(type(fileSortAbsMap.file_absPathSortMap))
