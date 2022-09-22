# -*- encoding=utf8 -*-

import random
import Basic
import Case
import Const

from threading import Thread
from airtest.core.api import *
from poco.drivers.unity3d import UnityPoco
from poco.exceptions import PocoTargetTimeout, PocoNoSuchNodeException


class PocoTest(Basic.Steps, Case.Flow):

    def __init__(self, device_, speed=1):
        super().__init__(speed)
        self.poco = UnityPoco()
        auto_setup(__file__, devices=[f"Android://127.0.0.1:5037/{device_}?cap_method=JAVACAP&&ori_method=MINICAPORI&&touch_method=MAXTOUCH"], logdir=Const.LOG_DIR)

    def resource_exist(self, res_name, timeout=120):
        """
        判断资源是否出现

        :param res_name: 资源名称
        :param timeout: 寻找资源时的超时时间
        :return: bool
        """
        try:
            self.poco(res_name).wait_for_appearance(timeout=timeout)
            return True
        except PocoTargetTimeout:
            return False

    def easy_touch(self, name):
        try:
            self.poco(name).click()
        except PocoNoSuchNodeException:
            raise PocoNoSuchNodeException
        finally:
            sleep(self.speed)

    def begin_fight(self):
        self.easy_touch("btnTeam")

    def start_fight(self):
        self.easy_touch("btnFight")

    def next_fight(self):
        self.easy_touch("BtnGet")

    def choose_buff(self):
        if self.resource_exist("FightInspireWindow(Clone)"):
            num = random.randint(1, 4)
            if num == 4:
                print("buff全选")
                self.poco("BtnDiamonGetAll").click()
            else:
                print(f"选择第{num}个buff")
                self.poco(f"BtnSkill{num}").click()

    def resurgence(self):
        """
        复活面板
        """
        def listener():
            while 1:
                try:
                    print("异步等待复活面板")
                    self.poco("FightAgainWindow(Clone)").wait_for_appearance(timeout=120)
                    self.poco("BtnGet").click()
                except PocoTargetTimeout:
                    pass
        rt = Thread(target=listener)
        rt.start()

    def try_fight_again(self):
        self.easy_touch("BtnGet")

    def hero_tab(self):
        self.easy_touch("ImgArmy")

    def choose_hero(self, name):
        if self.resource_exist("ArmyWindow(Clone)"):
            hero_list = self.poco("ArmyBookWindow(Clone)").child("Center").child("bookPanel").offspring("generalExistPanel").children()
            for hero in hero_list:
                hero_name = hero.offspring("Text_Name").get_text()
                print(hero_name)
                if hero_name == name:
                    hero_icon = hero.offspring("icon")
                    hero_icon.click()
                    break
        sleep(self.speed)

    def choose_solider(self, name):
        if self.resource_exist("ArmyWindow(Clone)"):
            solider_list = self.poco("ArmyBookWindow(Clone)").child("Center").child("bookPanel").child("soldierPanel").children()
            for solider in solider_list:
                solider_name = solider.offspring("topText").get_text()
                if solider_name == name:
                    solider_icon = solider.offspring("iconFrame")
                    solider_icon.click()
                    break
        sleep(self.speed)

    def lv_upgrade(self, duration=0.01):
        if self.resource_exist("ArmyEnhanceGeneralWindow(Clone)"):
            self.poco("BtnLevelUp").long_click(duration=duration)
        sleep(self.speed)

    def star_up(self):
        self.easy_touch("BtnStarUp")

    def suit_up(self):
        self.easy_touch("BtnPutOn")

    def take_off(self):
        self.easy_touch("BtnPutOff")

    def gift_tab(self):
        self.easy_touch("tab2")

    def train(self, **kwargs):
        self.easy_touch("BtnWeaponUp")

    def fast_buy_toggle(self):
        self.easy_touch("fastbuyBtn")

    def main_tab(self):
        self.easy_touch("btnHome")

    def back_btn(self):
        self.easy_touch("BtnBack")

    def get_reward(self):
        self.easy_touch("BtnGet")

    def manor_tab(self):
        self.easy_touch("btnShop")

    def recruit(self, is_manor_btn=True, recruit_times=1, is_skip_animate=True):
        if is_manor_btn:
            if self.resource_exist(Const.OFFICE_MAIN_WINDOW):
                self.poco("Recruit").child("area").click()
        if recruit_times == 1:
            if self.resource_exist(Const.RECRUIT_WINDOW):
                self.poco("receiveOne").click()
            else:
                self.poco("receiveFive").click()
        if is_skip_animate:
            self.poco("skipAnimBtn").click()
        sleep(self.speed)

    def one_key_add_piece(self):
        self.easy_touch("btnAdd")

    def confirm(self):
        self.easy_touch("btnOk")

    def click_close(self):
        pass

    def go_break(self):
        self.easy_touch("BtnGotoBreach")

    def break_(self):
        self.easy_touch("btn_breach")

    def close(self):
        self.easy_touch("BtnClose")

    def go_break2(self):
        self.easy_touch("BtnOk")

    def hero_task(self):
        self.easy_touch("bg")

    def get_task_reward(self):
        self.easy_touch("Img_lingqu")

    def equip1(self):
        self.easy_touch("LeftItem1")

    def equip2(self):
        self.easy_touch("RightItem1")

    def equip3(self):
        self.easy_touch("LeftItem2")

    def equip4(self):
        self.easy_touch("RightItem2")

    def newbie_guide(self):

        def buy_soldier_btn():
            if self.resource_exist(Const.FIGHT_TEAM_WINDOW):
                self.poco("btnBuySoldier").click()
                sleep(self.speed)

        def get_():
            if self.resource_exist("UnlockHeroWindow(Clone)"):
                self.poco("BtnGet").click()
            sleep(self.speed)

        def buy_bow_soldier():
            self.poco("soldierPanel").child("container").child("slot1 (1)").child("heroInfo").child(
                "iconContainer").child("icon").click()
            sleep(self.speed)

        def release_skill():
            self.poco("ActionSkill").child("1").click()
            sleep(self.speed)

        buy_soldier_btn()
        self.start_fight()
        self.get_reward()
        # 拖动合成
        self.poco("Pos7").child("showMesh").drag_to(self.poco("Pos8").child("showMesh"), duration=1)
        sleep(self.speed)
        buy_soldier_btn()
        self.start_fight()
        self.next_fight()
        get_()
        self.poco("btnSoldier").click()
        sleep(self.speed)
        # 购买弓兵
        buy_bow_soldier()
        buy_bow_soldier()
        self.start_fight()
        self.next_fight()
        self.start_fight()
        self.next_fight()
        self.start_fight()
        self.get_reward()
        get_()
        self.hero_tab()
        self.lv_upgrade(duration=3)
        self.back_btn()
        self.back_btn()
        self.main_tab()
        self.begin_fight()
        self.start_fight()
        sleep(10)
        release_skill()
        sleep(10)
        release_skill()
        self.next_fight()
        self.start_fight()
        self.next_fight()
        self.start_fight()
        self.next_fight()
        self.start_fight()
        self.next_fight()
        self.start_fight()
        self.next_fight()
        self.get_reward()
        self.manor_tab()
        self.recruit()
        pass

    def upgrade(self, names, get_task_reward=False):
        self.hero_tab()
        for name in names:
            self.choose_hero(name)
            self.lv_upgrade(duration=5)
        pass

    def equip_upgrade(self, name, equip_index, one_key_max=True, current_level=1, level=1, suit_up=True):
        pass

    def fetter_upgrade(self, name):
        pass

    def mhy(self, times):
        pass

    def fetter_btn(self):
        pass

    def go_star_up_btn(self):
        self.easy_touch("BtnOk")

    def choose_equip(self, index):
        if index == 1:
            self.easy_touch("LeftItem1")
        if index == 2:
            self.easy_touch("RightItem1")
        if index == 3:
            self.easy_touch("LeftItem2")
        if index == 4:
            self.easy_touch("RightItem2")

    def one_key_add_equip_piece(self):
        self.easy_touch("btnFill")

    def equip_lv_up(self):
        self.easy_touch("btnLvUp")

    def go_equip_upgrade(self):
        self.easy_touch("btnLevelUp")

    def go_equip_star_up(self):
        self.easy_touch("btnStarUp")

    def equip_star_up(self):
        self.easy_touch("btnStarUp")

    def infinity_war(self, current_floor, fight_times):
        g_str = self.poco("tipGuanqi").get_text()
        floor = int(g_str[1:len(g_str) - 1])
        self.begin_fight()
        while fight_times:
            self.poco(Const.FIGHT_TEAM_WINDOW).wait_for_appearance(timeout=240)
            self.start_fight()
            if floor % 5 == 0:
                self.choose_buff()
            self.poco("BtnGet").wait_for_appearance(timeout=240)
            self.poco("BtnGet").click()
            sleep(5)
            floor += 1
            fight_times -= 1
