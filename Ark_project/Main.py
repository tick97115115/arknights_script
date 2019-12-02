#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import Essentrial_facility
import Utility
import Image_load
import Combat_Agent


if __name__ == "__main__":
    goal = input('''请问要进行什么操作？请输入下方目标代码：
    Exp = 经验副本
    Money = 龙门币副本
    compound_jade = 合成玉副本

    Notice:区分大小写
    ''')
    number = input('请输入挂机次数:\n')
    number = int(number)
    Combat_Agent.Operation_LS(goal,number)