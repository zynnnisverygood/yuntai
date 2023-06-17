#!/usr/bin/python3

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge,CvBridgeError
import cv2

def yuntaicamSub():
    #初始化节点
    rospy.init_node("yuntai_cam_pub",anonymous=True)
    #创建订阅者

def cam():
    video = cv2.VideoCapture('rtsp://192.168.144.25:8554/main.264')
    # width = 640
    # heigth = 480
    # video.set(cv2.CAP_PROP_FRAME_WIDTH,width)
    # video.set(cv2.CAP_PROP_FRAME_HEIGHT,heigth)

    while not rospy.is_shutdown():
        ret, img = video.read()
        if ret:
            bridge = CvBridge()
            msg = bridge.cv2_to_imgmsg(img,encoding="bgr8")
            rospy.loginfo("yuntai_cam:%0.2f,%0.2f",msg.height,msg.width)
            rospy.Publisher("cam/image_raw",Image,queue_size=1).publish(msg)
            # cv2.imshow('img' ,img)
            if ord('b') == cv2.waitKey(10):
                break
    video.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    yuntaicamSub()
    cam()    
    
    


