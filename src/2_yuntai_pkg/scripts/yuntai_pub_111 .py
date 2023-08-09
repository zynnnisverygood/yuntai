#!/usr/bin/python3
# -*- coding: utf-8 -*-

########################################################################
####          Copyright 2020 GuYueHome (www.guyuehome.com).          ###
########################################################################

# 该例程将发布turtle1/cmd_vel话题，消息类型geometry_msgs::Twist

import rospy
from yuntai_pkg.msg import pub_setspeed
import sensor_msgs
from time import sleep
from yuntai import getpose, TTL 

def yuntai_publisher(msg):
	# ROS节点初始化
    rospy.init_node('yuntai_publisher', anonymous=True)
	# 初始化geometry_msgs::Twist类型的消息
    speed_msg = pub_setspeed()
    speed_msg.xside = 20
    speed_msg.yside = 20
    
	# 创建一个Publisher，发布名为yuntai_setspeed_info的topic，消息类型为 parameter，队列长度10
    yuntai_speed_pub = rospy.Publisher('yuntai_setspeed_info', parameter, queue_size=10)

	#设置循环的频率
    rate = rospy.Rate(10) 

    while not rospy.is_shutdown():
		# 发布消息
        yuntai_speed_pub.publish(parameter_msg)
        rospy.loginfo("yuntai_speed[%0.2f , %0.2f]", speed_msg.xside, speed_msg.yside)

		# 按照循环频率延时
        rate.sleep()
        
        rospy.Subscriber("/yuntai_getpose_info", yuntai_getpose_msg)
        
        rospy.loginfo("yuntai getpose is running")
        get = getpose(TTL)
        parameter_msg = parameter()
    	parameter_msg.yaw=get[0]   
    	parameter_msg.pitch=get[1]  
    	parameter_msg.roll=get[2]  
    	parameter_msg.yaw_velocity= get[3]    
    	parameter_msg.pitch_velocity=get[4]  
    	parameter_msg.roll_velocity=get[5]  
    	parameter.publish(parameter_msg)

if __name__ == '__main__':  
    yuntai_publisher()
   
