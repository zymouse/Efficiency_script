#!/usr/bin/env python  
# -*- coding:utf-8 -*-
import rospy
# from geometry_msgs.msg import Transform
import tf2_ros
import io
import tf
import ConfigParser
from time import gmtime, strftime
from string import Template

def iniFileParser(data):
    config = ConfigParser.RawConfigParser()
    config.read(data)
    return config

def getTransformationRelation(frame_id, child_frame_id):
    global tfbuffer
    global rate
    while not rospy.is_shutdown():
        try:
            trans = tfbuffer.lookup_transform(frame_id, child_frame_id, rospy.Time())
            break
        except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException) as e:
            print "Fail", e
        rate.sleep()
        
    trans = trans.transform
    x = trans.translation.x
    y = trans.translation.y
    z = trans.translation.z
    qx = trans.rotation.x
    qy = trans.rotation.y
    qz = trans.rotation.z
    qw = trans.rotation.w

    return x, y, z, qx, qy, qz, qw

launch_file = Template("""<launch>
$node_xml</launch>""")

node_xml =  Template("""<node pkg="tf" type="static_transform_publisher" name="$node_name" args="$transform_arg" />""")

if __name__ == '__main__':
    rospy.init_node('tf_echo')
    tfbuffer = tf2_ros.Buffer()
    listener = tf2_ros.TransformListener(tfbuffer)
    rate = rospy.Rate(10.0)
    config = iniFileParser("input/test.ini")
    node_xmls = list()
    for name_node in  config.sections():
        frame_id = config.get(name_node, "frame_id")
        child_frame_id = config.get(name_node, "child_frame_id")
        trans_t = getTransformationRelation(frame_id, child_frame_id)
        trans_t = ("%f"%i for i in trans_t)
        transform_arg = " ".join(trans_t)
        transform_arg  += " "+ " ".join((frame_id, child_frame_id, "100"))
        node_xmls.append(node_xml.substitute(node_name=name_node,transform_arg=transform_arg))

    # print node_xmls
    node_xmls = "\t" + "\n\t".join(node_xmls)+"\n"
    launch_file = launch_file.substitute(node_xml=node_xmls)
    # print launch_file
    name_Suffix = strftime("%M%S", gmtime())
    with io.open(r"output/tf_Static_{}.launch".format(name_Suffix), 'w', encoding="utf-8") as fp:
        fp.write(launch_file.decode("utf-8"))
        pass

        
        

    
    

