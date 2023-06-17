#!/usr/bin/python3
# -*- coding: utf-8 -*-

########################################################################
####          Copyright 2020 GuYueHome (www.guyuehome.com).          ###
########################################################################

# 该例程将订阅/person_info话题，自定义消息类型learning_topic::Person

import rospy
from yuntai_pkg.msg import yuntai_setspeed_msg,yuntai_setpose_msg,yuntai_setback_msg,yuntai_getpose_msg
import sensor_msgs
from time import sleep
from yuntai import setpose,setback,setspeed,getpose, TTL


def setspeedInfoCallback(msg):
    rospy.loginfo("yuntai speed: xside:%0.2f,y:%0.2f",msg.xside,msg.yside)
    setspeed(TTL, msg.xside,msg.yside)

def setposeInfoCallback(msg):
    rospy.loginfo("yuntai setpose: x:%0.2f,y:%0.2f",msg.yaw,msg.pitch)
    setpose(TTL, msg.yaw, msg.pitch)

def setbackInfoCallback(msg):
    rospy.loginfo("yuntai setback is running")
    setback(TTL)

def getposeInfoCallback(msg):
    rospy.loginfo("yuntai getpose is running")
    getpose(TTL)
    
    
    
    
    
def yuntai_subscriber():
	# ROS节点初始化
    rospy.init_node('yuntai_setspeed_subscriber', anonymous=True)

	# 创建一个Subscriber，订阅名为___的topic，注册回调函数
    rospy.Subscriber("/yuntai_setspeed_info", yuntai_setspeed_msg, setspeedInfoCallback)


	
    rospy.Subscriber("/yuntai_setpose_info", yuntai_setpose_msg, setposeInfoCallback)



	
    rospy.Subscriber("/yuntai_setpose_info", yuntai_setback_msg, setposeInfoCallback)


	
    rospy.Subscriber("/yuntai_getpose_info", yuntai_getpose_msg, getposeInfoCallback)

    

	# 循环等待回调函数
    rospy.spin()
if __name__ == '__main__':
    yuntai_subscriber()
    # while rospy.is_shutdown():
    #     sleep(0.2)
    # print(rospy.is_shutdown())
    # TTL.close()

