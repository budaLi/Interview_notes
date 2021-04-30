# coding=utf-8
# Copyright (c) 2020 ichinae.com, Inc. All Rights Reserved
"""
参考： https://zhuanlan.zhihu.com/p/67930839
Authors: 15735656005@163.com
"""

import numpy as np
import datetime

from utils import _get_current_screen_shoot
from utils import _get_poi_number
from utils import _Matchimage
from utils import _getText
from utils import get_current_time
from utils import get_average_speed

# 图像中 Guiding information (GI)box 和Arrival information box 的像素取值
BOX_low_hsv = np.array([0, 0, 0])  # 这里要根据HSV表对应
BOX_high_hsv = np.array([0, 100, 0])  # 这里填入三个max值

def main():
    """
    到达信息框中显示的预期到达时间应该始终基于到达目的地之前的预期平均速度
    """
    img = _get_current_screen_shoot()
    # 每个区域获取对应的POI数量个数
    _,img_boxs = _get_poi_number(img,BOX_low_hsv,BOX_high_hsv,style= "hls")

    # 判断哪个是Arrival information box
    for box in img_boxs:
        x, y, w, h = box
        x_end = x+w
        y_end = y+h
        if _Matchimage(x,y,x_end,y_end,"Arrival information box"):
            # 获取内容
            text = _getText(x,y,x_end,y_end)
            km_info = float(text.split(",")[0].split(":")[1])
            arring_info = ":".join(text.split(",")[1].split(":")[1:])
            print("Arrival information box:{}".format(km_info,arring_info))

            # 获取当前系统时间及平均速度 用里程数除以平均速度获取到达时间
            current_time = get_current_time()
            average_speed = get_average_speed()
            average_speed = float(average_speed.replace("km/h",""))
            cost_time = datetime.timedelta(minutes = km_info/average_speed)

            print("current time:{}, cost time:{},arring_info_time:{}".format(current_time,cost_time,arring_info))
            break

if __name__ == '__main__':
    main()
