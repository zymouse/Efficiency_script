#!/usr/bin/env python  
# -*- coding:utf-8 -*-

import MyConfig as MyConfig

""" 
输入：文件夹路径列表和对于文件夹下的文件列表
输出：读取的文件内容值
"""

if __name__ == '__main__':
    for i in MyConfig.fileSortAbsMap.file_absPathSortMap.values():
        print(i)
