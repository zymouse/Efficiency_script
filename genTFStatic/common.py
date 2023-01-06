#!/usr/bin/env python  
# -*- coding:utf-8 -*-
import rospy
# from geometry_msgs.msg import Transform
import tf2_ros

def getTransformationRelation(frame_id, child_frame_id):

    rospy.init_node('tf_echo')
    rate = rospy.Rate(10.0)

    tfbuffer = tf2_ros.Buffer()
    listener = tf2_ros.TransformListener(tfbuffer)
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
    Quaternion = (qx, qy, qz, qw)
    return x, y, z, Quaternion