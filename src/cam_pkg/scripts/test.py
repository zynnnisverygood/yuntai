#!/usr/bin/python3
# -*- coding: utf-8 -*-
#引入库
cap = cv2.VideoCapture('rtsp://192.168.144:8554/main.264')
#cap = cv2.VideoCapture(0)
while True:
    try:
        ret, frame = cap.read()
        if ret:
            cv2.imshow("Video", frame)
        #读取内容
            if cv2.waitKey(10) == ord("q"):
                break
        else:
            print('no frame', end='\r')
    except:
        cap.release()
        cv2.destroyAllWindows()
        break
        
#随时准备按q退出
cap.release()
cv2.destroyAllWindows()
#停止调用，关闭窗口

