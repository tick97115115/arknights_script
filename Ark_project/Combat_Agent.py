#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from Utility import *
from Image_load import *
import cv2 as cv
import numpy as np
from mss.windows import MSS as mss
import time

ProcessControl = []
####经验本####
Exp = [Combat,Section_of_Materials_collection,Into_Page_of_Exp_Collection,Exprience_Five]
Money = [Combat,Section_of_Materials_collection,Into_Page_of_Money_Collection,Money_Five]
compound_jade = [Combat,Page_of_KILL_THEM_ALL,Outer_Ring_of_LongMen]
def Operation_LS(loop_count,number):
    loop_count = eval(loop_count)
    num = 0
    Back_To_Home()
    Out_of_Home()
    if loop_count is not Page_of_KILL_THEM_ALL:
        Match_And_Click(loop_count[1],tms=3)
        Match_And_Click(loop_count[2],tms=3)
    else:
        Match_And_Click(loop_count[1],tms=3)
    while num < number:
        num += 1
        Match_And_Click(loop_count[-1],tms=2)
        if num == 1:
            Match_And_Click(Combat_Get_Ready,tms=3,wrong="已确认代理模式")
        Match_And_Click(Combat_Get_Start,tms=3)
        Match_And_Click(Ensure_Company,tms=3)
        Data_Switching_delay()
        while True:
            if Match_And_Click(Keep_Fighting,wrong="第%d轮完成。" % num,tms=7) is not False:
                time.sleep(3)
            else:
                while Match_Only(Banner_Buttom,tms=3) is False:
                    mouse.click()
                    time.sleep(3)
                    mouse.click()
                    time.sleep(3)
                break
    Back_To_Home()


##########