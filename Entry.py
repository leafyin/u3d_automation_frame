# -*- encoding=utf8 -*-
import sys

from AirTest import AirTest
from PocoTest import PocoTest
from airtest.report.report import LogToHtml, simple_report
from DingDingRobot import *

import Const


def menu(device_):
    obj = AirTest(device_)
    while 1:
        print("1.新手引导")
        print("2.英雄升级")
        print("3.装备升级")
        print("4.羁绊升级")
        print("5.无限战斗")
        arg = input()
        arg = int(arg)
        if arg == 1:
            make_call(obj.newbie_guide)
        if arg == 2:
            print("输入英雄名称，需升级多个英雄请用|隔开")
            hero_str = input()
            hero = []
            for h in hero_str.split("|"):
                hero.append(h)
            make_call(obj.upgrade, names=hero)
        if arg == 3:
            print("输入英雄名称")
            name = input()
            make_call(obj.equip_upgrade, name=name)
        if arg == 4:
            print("输入想要升级的羁绊（确保你的羁绊已经激活）")
            name = input()
            make_call(obj.fetter_upgrade, name=name)
        if arg == 5:
            print("这个case是用来测试战斗中是否有一些异常，参数1：当前关卡的尾数，参数2：需要战斗多少关，用|隔开，eg：23|100")
            param = input()
            param = param.split("|")
            make_call(obj.infinity_war, current_floor=int(param[0]), fight_times=int(param[1]))


def make_call(func, **kwargs):
    try:
        func.__call__(**kwargs)
    finally:
        now = time.strftime("%Y%m%d%H%M%S", time.localtime())
        # access_path = f"D:\\nginx-1.22.0\\html\\{now}"
        # doc = str(func.__doc__).replace(" ", "").replace("\n", "")
        # logfile = "E:\\mini_army_autotest\\Main\\log\\log.txt"
        # file_name = str(__file__).split("/")[len(str(__file__).split("/")) - 1].split(".")[0]
        # msg = f"UI自动化测试报告-{doc}\n"
        # url = f"{msg}http://172.18.11.106/{now}/{file_name}.log/log.html"
        # send_msg(url)
        simple_report(__file__, logpath="E:\\log", output=f"E:\\{now}.html")


if __name__ == '__main__':
    menu("00000af7ad0617a0")
    # poco_ = PocoTest("00000af7ad0617a0")
    # poco_.infinity_war(0, 10)
