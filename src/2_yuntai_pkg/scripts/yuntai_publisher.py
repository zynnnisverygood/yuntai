#!/usr/bin/python3
# -*- coding: utf-8 -*-

########################################################################
####          Copyright 2020 GuYueHome (www.guyuehome.com).          ###
########################################################################

# 该例程将发布turtle1/cmd_vel话题，消息类型geometry_msgs::Twist

import rospy
from yuntai_pkg.msg import pub_setspeed

def yuntai_publisher():
	# ROS节点初始化
    rospy.init_node('yuntai_publisher', anonymous=True)

	# 创建一个Publisher，发布名为/turtle1/cmd_vel的topic，消息类型为geometry_msgs::Twist，队列长度10
    yuntai_speed_pub = rospy.Publisher('yuntai_setspeed_info', pub_setspeed, queue_size=10)

	#设置循环的频率
    rate = rospy.Rate(10) 

    while not rospy.is_shutdown():
		# 初始化geometry_msgs::Twist类型的消息
        speed_msg = pub_setspeed()
        speed_msg.xside = 20
        speed_msg.yside = 20

		# 发布消息
        yuntai_speed_pub.publish(speed_msg)
        rospy.loginfo("yuntai_speed[%0.2f , %0.2f]", speed_msg.xside, speed_msg.yside)

		# 按照循环频率延时
        rate.sleep()

if __name__ == '__main__':
    try:
        yuntai_publisher()
    except rospy.ROSInterruptException:
        pass
