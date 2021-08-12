#!/usr/bin/env python
# coding: utf-8
"""
1.0 自动固定ousetr_ip脚本

"""
import os
import re
import requests

# os.system(cmd) -- 在终端执行指令，但是交互式指令
# os.system("ls")
# def list_transform_string():

def get_ouster_ipv4():
    """
    # 获取ouster雷达现在的IP
    return：ouster雷达的默认IPv4的ip
    """
    os.system("avahi-browse -ltr _roger._tcp")  # 第一次获取雷达原始ip
    return_raw_list = os.popen("avahi-browse -ltr _roger._tcp").readlines()
    # print(return_raw_list)
    return_raw_string  = "".join(return_raw_list)
    return_ipv4 = re.search("address = \[[0-9\.]{13,15}",return_raw_string).group().split("[", 1)
    # print(return_ipv4[1])
    return return_ipv4[1]


def revise_ouster_ipv4(old_ip, new_ip="192.168.1.120"):
    """
    修改ouster雷达的IP
    para: 
        new_ip  雷达的新ip   默认"192.168.1.120"
        old_ip  雷达的旧ip
    return: 修改成功返回True，修改失败返回False
    """
    # 修改ip--192.168.1.117
    # old_ip = get_default_ipv4()  # 雷达当前ip

    put_response = requests.put('http://{}/api/v1/system/network/ipv4/override'.format(old_ip),headers={'Content-Type': 'application/json'},json='{}/24'.format(new_ip))
    return put_response.status_code

if __name__=="__main__":
    print("start....")
    # 获取雷达ip
    old_ip = get_ouster_ipv4()
    # print(old_ip)
    status = revise_ouster_ipv4(old_ip, "192.168.1.116")
    print(status)



