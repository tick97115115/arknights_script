#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import cv2 as cv
import numpy as np
import mouse
from mss.windows import MSS as mss
from Image_load import *
import time


def Match_And_Click(template,tms=0,meth=0,wrong=None):
    time.sleep(tms)
    img = cv.imread(Take_a_screenshot(),0)
    tpl = cv.imread(template,0)
    h,w = tpl.shape
    if meth == 0:
        method = 'cv.TM_SQDIFF_NORMED'

    res = cv.matchTemplate(img,tpl,eval(method))
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)

    if meth == 0 and min_val < 0.1:
        x,y = min_loc[0] + w/2, min_loc[1] + h/2
        mouse.move(x,y)
        mouse.click()
    else:
        if wrong == None:
            pass
        else:
            print(wrong)#需要学习try-except-finally语句控制，来达成正式的错误反馈
        return False

def Match_Only(template,tms=0,wrong=None):
    time.sleep(tms)
    img = cv.imread(Take_a_screenshot(),0)
    tpl = cv.imread(template,0)
    h,w = tpl.shape
    res = cv.matchTemplate(img,tpl,cv.TM_SQDIFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
    if min_val < 0.1:
        return True
    else:
        return False
        print(wrong)


def Take_a_screenshot():
    with mss() as sct:
        return sct.shot()


####Location_Management####

Previous_Location = None
Current_Location = None

def Banner_Into_Any_Location(Destination):
    if Destination is not HomeFaceID:
        if Match_And_Click(HomeFaceID) is False:
            Match_And_Click(Banner_Buttom,tms=2)
            Match_And_Click(Destination,tms=2)
        else:
            print("Now you are on Home Page,we can't change page via ClickBanner.Please out of HomePage. eg:into combat page.")


def Back_To_Home():
    HiddenMouse()
    if Match_And_Click(HomeFaceID) is not False:
        print('您已在主界面')
    else:
        Match_And_Click(Banner_Buttom,tms=3)
        Match_And_Click(HomeBanner_HomePage,tms=3)

def Out_of_Home():
    if Match_And_Click(HomeFaceID,tms=3) is False:
        print('Now, you are already out of HomePage.')
    else:
        Match_And_Click(Into_Combat,tms=3)

##########################

def Data_Switching_delay():#避免与服务器数据交换过程中由于网络延迟产生的错误操作
    time.sleep(10)


def HiddenMouse():
    mouse.move(1920,1080)
