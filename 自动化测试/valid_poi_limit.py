# coding=utf-8
# Copyright (c) 2020 ichinae.com, Inc. All Rights Reserved
"""
参考：
https://blog.csdn.net/qq_43670549/article/details/108242679

Authors: 15735656005@163.com
"""

import cv2
import numpy as np
from utils import _get_current_screen_shoot
from utils import _get_poi_number


# 图像中POI label区域对应的像素取值  参考HSV.jpg
POI_label_low_hsv = np.array([11, 43, 46])  # 这里要根据HSV表对应
POI_label_high_hsv = np.array([25, 255, 255])  # 这里填入三个max值

def main():
    """
    地图中每四分之一的部分中poi_number个POI标识
    """
    img = _get_current_screen_shoot()
    # 四等分图片
    h,w,c = img.shape
    middle_x = w//2
    middle_y = h//2
    first_part_img =  img[0:middle_y,0:middle_x]
    second_part_img = img[0:middle_y,middle_x:w]
    third_part_img = img[middle_y:h,0:middle_x]
    four_part_img = img[middle_y:h,middle_x:w]

    cv2.imwrite("./four_part_img/first_part_img.jpg",first_part_img)
    cv2.imwrite("./four_part_img/second_part_img.jpg",second_part_img)
    cv2.imwrite("./four_part_img/third_part_img.jpg",third_part_img)
    cv2.imwrite("./four_part_img/four_part_img.jpg",four_part_img)

    # 每个区域获取对应的POI数量个数
    first_part_poi_numer,first_part_poi_box = _get_poi_number(first_part_img,POI_label_low_hsv,POI_label_high_hsv)
    second_part_numer,second_part_poi_box = _get_poi_number(second_part_img,POI_label_low_hsv,POI_label_high_hsv)
    third_part_img_poi_numer,third_part_poi_box = _get_poi_number(third_part_img,POI_label_low_hsv,POI_label_high_hsv)
    four_part_poi_numer,four_part_poi_box = _get_poi_number(four_part_img,POI_label_low_hsv,POI_label_high_hsv)

    print("first part poi number:{},box:{}".format(first_part_poi_numer,first_part_poi_box))
    print("second part poi number:{},box:{}".format(second_part_numer,second_part_poi_box))
    print("third part poi number:{},box:{}".format(third_part_img_poi_numer,third_part_poi_box))
    print("four part poi number:{},box:{}".format(four_part_poi_numer,four_part_poi_box))



if __name__ == '__main__':
    main()