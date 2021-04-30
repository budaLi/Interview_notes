# coding=utf-8
# Copyright (c) 2020 ichinae.com, Inc. All Rights Reserved
"""
Module Summary Here.
Authors: 15735656005@163.com
"""

import cv2
import numpy as np

#当前系统时间
def get_current_time():
    Current_system_time = "13:30:59"
    return Current_system_time
c
# 预期平均车速
def get_average_speed():
    Expected_average_speed_until_destination = "80km/h"
    return Expected_average_speed_until_destination


# 当前地理坐标
Current_geographic_coordinates = "32.715°N, 117.163°W"
# 距下一指示牌距离
Distance_to_next_guiding_event = "300m"
#下一指示牌信息
Type_of_next_guiding_event = "Right Turn"


def _getColor(x,y):
    """
    Returns the color value of a single pixel.
    返回单个像素的颜色值KM left:84Arrival:12:01010
    """
    ...

def _getText(x_start,y_start,x_end,y_end):
    """
    Returns the text inside a rectangle defined via x and y coordinates.
    返回由x和y坐标定义的文本内容
    """
    return "KM lEFT:84,Arrival:12:01"

def _Matchimage(x_start,y_start,x_end,y_end,img_src):
    """
    Returns true if the rectangle defined via x and y coordinates matches the image file set in img_src,otherwise return false.
    如通过x和y坐标定义的矩形与img_src中的图像文件集匹配，则返回false
    """
    return True


def _get_current_screen_shoot():
    """
    获取导航系统的当前界面截图
    """
    img = cv2.imread("screenshots.jpg")
    img = cv2.resize(img, (1080, 490))
    return img


def _get_poi_number(img,low_,high_,style="hsv"):
    """
    style 表示用哪种方式提取颜色  主要用到HLS和HSV 参考：https://blog.csdn.net/weixin_43584807/article/details/106386711
    获取符合low_hsv,high_hsv的图片中的矩形框个数及其对应box 坐标
    """
    cv2.namedWindow("input", cv2.WINDOW_AUTOSIZE)
    cv2.imshow("input", img)
    if style=="hls":
        src = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)  # BGR转HSV
    else:
        src = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  # BGR转HSV

    mask = cv2.inRange(src, lowerb=low_, upperb=high_)  # 提取掩膜
    # 二值化操作
    ret, binary = cv2.threshold(mask, 0, 255, cv2.THRESH_BINARY)
    # 膨胀操作，因为是对线条进行提取定位，所以腐蚀可能会造成更大间隔的断点，将线条切断，因此仅做膨胀操作
    kernel = np.ones((5, 5), np.uint8)
    dilation = cv2.dilate(binary, kernel, iterations=1)
    # 获取图像轮廓坐标，其中contours为坐标值，此处只检测外形轮廓
    contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    new_box_res= []
    if len(contours) > 0:
        # cv2.boundingRect()返回轮廓矩阵的坐标值，四个值为x, y, w, h， 其中x, y为左上角坐标，w,h为矩阵的宽和高
        boxes = [cv2.boundingRect(c) for c in contours]
        for box in boxes:
            x, y, w, h = box
            # 过滤太小的区域  文档中指出 最小为 100x30  故大小最小设置为3000
            if w*h<3000:
                continue
            new_box_res.append(box)
            # 绘制矩形框对轮廓进行定位
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 4)
        # 将绘制的图像保存并展示
        # cv2.imwrite("./masked_poi_for_four_part_img/xxx.jpg", img)
        cv2.imshow('image', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    return len(new_box_res),new_box_res