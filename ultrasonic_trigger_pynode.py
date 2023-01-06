#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
用于超声波雷达，通过发送接收can报文起到：
1.0 触发超声波雷达
2.0 查看超声波雷达状态
"""
# -------------------- import -------------------
import can
can.rc["interface"] = "socketcan_native"
# can.rc["channel"] = "can1"
can.rc["bitrate"] = 500000
from can.interface import Bus
from can import Message
import rospy


# -------------------- global -------------------
# global execute
rospy.init_node("ultrasonic_trigger_pynode", anonymous=True)


# -------------------- class -------------------
class ZyCan(object):
    """
    发送和接收can消息
    """
    def __init__(self,channel):
        self.bus = Bus(channel=channel)
        # make can msgs --
        self.can_byte_data = [0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0] 
        self.__can_msgs = Message(data = self.can_byte_data, is_extended_id=False, arbitration_id=0x231)
    

    def can_send(self, rate = 5):
        """can msgs  send to 0x231
        parameter:
            rate -- send rate 5HZ
        return:
            None
        """
        send_rate = rospy.Rate(rate)
        while not rospy.is_shutdown():
            self.bus.send(self.__can_msgs)
            send_rate.sleep()


# -------------------- function --------------------
# -------------------- main_func -------------------
def main():
    print("program start....")
    can_send = ZyCan("can1")
    can_send.can_send()
 
 
# -------------------- demo_test -------------------
if __name__ == "__main__":
    main()
 
