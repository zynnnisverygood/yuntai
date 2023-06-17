#!/usr/bin/python3
#!coding=utf-8



import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge 
import cv2

def yuntaicamcallback(msg):  
    #图像转化
    bridge = CvBridge()
    img = bridge.imgmsg_to_cv2(msg,desired_encoding="bgr8")
    cv2.imshow('win',img)
    cv2.waitKey(1)

def yuntai_sub():
	# ROS节点初始化
    rospy.init_node('yuntai_cam_sub', anonymous=True)
    img_sub = rospy.Subscriber("/cam/image_raw",Image,yuntaicamcallback)
    


	#设置循环的频率
    rospy.spin()

yuntai_sub()
