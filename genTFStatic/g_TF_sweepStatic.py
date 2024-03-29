#!/usr/bin/env python  
# -*- coding:utf-8 -*-
import rospy
import tf2_ros
import io
import ConfigParser
from time import gmtime, strftime
from string import Template
import PyKDL
from math import pi
import getpass
import os
import shutil

import common

def iniFileParser(data):
    config = ConfigParser.RawConfigParser()
    config.read(data)
    return config


baseTF= Template("""${FrameID_F}2$FrameID_S:
    x:$x
    y:$y
    z:$z
    roll:$roll
    pitch:$pitch
    yaw:$yaw
    """)


def replace_calibration_file():
    # 替换文件
    sweep_calibration_path = "/home/%s/pixautowarearchitectureproposal/install/vehicle_launch/share/vehicle_launch/config/default/sweeper_sensor_kit/"
    sweep_calibration_flie = "sensors_calibration.yaml"
    sweep_calibration_path = sweep_calibration_path%getpass.getuser()
    
    file_exists = os.path.exists("./output/sensors_calibration.yaml")
    if(not file_exists):
        print("./output/sensors_calibration.yaml文件不存在")
        exit()
        
    while(True):
        print("文件路径:%s+%s}\n"%(sweep_calibration_path, sweep_calibration_flie))
        instr = raw_input("是否替换sensors_calibration.yaml文件(yes/no):")
        print(instr)

        if(instr!="yes" and instr!="no"):
            print("请输入yes或者no")
            continue


        if(instr=="yes"):  # 备份原来的文件，并拷贝
            print("完成替换，并备份原文件")
            if(os.path.exists(sweep_calibration_path+sweep_calibration_flie)):
                name_Suffix = strftime("%M%S", gmtime())
                os.rename(sweep_calibration_path+sweep_calibration_flie, sweep_calibration_path+sweep_calibration_flie+".%s"%name_Suffix)
            else:
                if(not os.path.exists(sweep_calibration_path)):
                    os.makedirs(sweep_calibration_path)

            shutil.copy("output/sensors_calibration.yaml", sweep_calibration_path+sweep_calibration_flie)
            break

        else:
            print("取消替换文件")
            break


if __name__ == '__main__':

    config = iniFileParser("input/test.ini")
    sensingTF = list()
    print(config.sections())
    for name_node in  config.sections():
        frame_id = config.get(name_node, "frame_id")
        child_frame_id = config.get(name_node, "child_frame_id")
        trans_set = common.getTransformationRelation(frame_id, child_frame_id)
        # print(trans_set[3])
        rot = PyKDL.Rotation.Quaternion(x=trans_set[3][0], y=trans_set[3][1], z=trans_set[3][2], w=trans_set[3][3])
        YPR_radian = rot.GetEulerZYX()
        # print(YPR_radian)
        TF_value = baseTF.substitute(FrameID_F=frame_id, FrameID_S=child_frame_id, \
                            x=trans_set[0], y=trans_set[1], z=trans_set[2],\
                            roll=YPR_radian[2], pitch=YPR_radian[1], yaw=YPR_radian[0])
        # print baseTF 
        sensingTF.append(TF_value)


    # print sensingTF[0]
    # print node_xmls
    sensingTFs = "\n".join(sensingTF)+"\n"
    # launch_file = launch_file.substitute(node_xml=node_xmls)


    # print launch_file
    # name_Suffix = strftime("%M%S", gmtime())
    with io.open(r"output/sensors_calibration.yaml", 'w', encoding="utf-8") as fp:
        fp.write(sensingTFs.decode("utf-8"))
    #     pass
    
    replace_calibration_file()


        
        

    
    

