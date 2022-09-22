# -*- encoding=utf8 -*-

import abc

import uiautomator2 as u2


class AndroidInfo:

    def __init__(self, device_):
        self.device = u2.connect(device_)
        device_info: dict = self.device.info
        # 当前包名
        self.currentPackageName = device_info["currentPackageName"]
        # 屏幕方向（横屏、竖屏），如果横屏的高度和宽度是相反的
        self.displayRotation = device_info["displayRotation"]
        # 高度
        self.displayHeight = device_info["displayHeight"]
        # 宽度
        self.displayWidth = device_info["displayWidth"]
        # 屏幕x坐标
        self.displaySizeDpX = device_info["displaySizeDpX"]
        # 屏幕y坐标
        self.displaySizeDpY = device_info["displaySizeDpY"]
        # 屏幕是否开启
        self.screenOn = device_info["screenOn"]
        # ...
        self.naturalOrientation = device_info["naturalOrientation"]


class Steps(metaclass=abc.ABCMeta):

    def __init__(self,  speed: int):
        self.speed = speed
        pass

    @abc.abstractmethod
    def begin_fight(self):
        """
        首页开战
        """
        pass

    @abc.abstractmethod
    def start_fight(self):
        """
        进入战斗
        """
        pass

    @abc.abstractmethod
    def next_fight(self):
        """
        下一关战斗
        """
        pass

    @abc.abstractmethod
    def choose_buff(self):
        """
        选择buff
        """
        pass

    @abc.abstractmethod
    def resurgence(self):
        """
        复活
        """
        pass

    @abc.abstractmethod
    def try_fight_again(self):
        """
        再次挑战
        """
        pass

    @abc.abstractmethod
    def hero_tab(self):
        """
        英雄tab页面
        """
        pass

    @abc.abstractmethod
    def choose_hero(self, name):
        """
        根据名称选择英雄

        :param name: 英雄名称
        """
        pass

    @abc.abstractmethod
    def choose_solider(self, name):
        """
        根据名称选择士兵

        :param name: 士兵名称
        """
        pass

    @abc.abstractmethod
    def lv_upgrade(self, **kwargs):
        """
        升级

        :param kwargs: 可选参数 duration 按住升级按钮的持续时间（长按）
        """
        pass

    @abc.abstractmethod
    def star_up(self):
        """
        升星按钮
        """
        pass

    @abc.abstractmethod
    def go_star_up_btn(self):
        """
        去升星按钮
        """
        pass

    @abc.abstractmethod
    def suit_up(self):
        """
        一键穿戴
        """

    @abc.abstractmethod
    def take_off(self):
        """
        卸下
        """

    @abc.abstractmethod
    def gift_tab(self):
        """
        天赋tab页面
        """

    @abc.abstractmethod
    def train(self, **kwargs):
        """
        培养

        :param kwargs: 可选参数 duration 按住升级按钮的持续时间（长按）
        """

    @abc.abstractmethod
    def fast_buy_toggle(self):
        """
        快捷购买开关，勾选时使用这个方法会取消勾选，反之亦然
        """

    @abc.abstractmethod
    def main_tab(self):
        """
        回到首页（只能当前不在首页的时候使用）
        """

    @abc.abstractmethod
    def back_btn(self):
        """
        返回按钮（许多场景通用）
        """

    @abc.abstractmethod
    def get_reward(self):
        """
        领取奖励
        """

    @abc.abstractmethod
    def manor_tab(self):
        """
        领地tab
        """
        pass

    @abc.abstractmethod
    def recruit(self, is_manor_btn=True, recruit_times=1, is_skip_animate=True):
        """
        招募功能，点击领地tab页面进入招募，或者进行单抽还是十连抽

        :param is_manor_btn: 是否点击的是领地tab里面的招募按钮，默认True
        :param recruit_times: 单抽还是十连抽，默认单抽，或者新手引导里面免费抽奖
        :param is_skip_animate: 是否跳过动画，默认跳过
        """
        pass

    @abc.abstractmethod
    def one_key_add_piece(self):
        """
        一键添加
        """
        pass

    @abc.abstractmethod
    def confirm(self):
        """
        确认
        """
        pass

    @abc.abstractmethod
    def click_close(self):
        """
        点击空白处关闭
        """
        pass

    @abc.abstractmethod
    def go_break(self):
        """
        去突破
        """
        pass

    @abc.abstractmethod
    def break_(self):
        """
        突破
        """
        pass

    @abc.abstractmethod
    def close(self):
        """
        关闭面板
        """
        pass

    @abc.abstractmethod
    def go_break2(self):
        """
        去突破2
        """
        pass

    @abc.abstractmethod
    def hero_task(self):
        """
        英雄任务按钮
        """
        pass

    @abc.abstractmethod
    def get_task_reward(self):
        """
        领取按钮（英雄任务）
        """
        pass

    @abc.abstractmethod
    def choose_equip(self, index):
        """
        选择装备

        :param index: 第几个装备，横着数，1、2、3、4
        """
        pass

    @abc.abstractmethod
    def one_key_add_equip_piece(self):
        """
        一键添加装备碎片
        """
        pass

    @abc.abstractmethod
    def equip_lv_up(self):
        """
        装备升级
        """
        pass

    @abc.abstractmethod
    def go_equip_upgrade(self):
        """
        去装备升级页面
        """
        pass

    @abc.abstractmethod
    def go_equip_star_up(self):
        """
        去装备升星
        """
        pass

    @abc.abstractmethod
    def equip_star_up(self):
        """
        装备升星
        """

    @abc.abstractmethod
    def fetter_btn(self):
        """
        羁绊按钮
        """

    def choose_fetter(self, name):
        """
        选择羁绊

        :param name: 羁绊名称
        """

    def army_btn(self):
        """
        军团按钮
        """

    def hero_buff_btn(self):
        """
        英雄加成按钮
        """

    def fetter_upgrade_btn(self):
        """
        羁绊升级按钮
        """

    def risk_btn(self):
        """
        冒险tab
        """

    def mhy_entry(self):
        """
        魔幻域入口
        """

    def mhy_tips(self):
        """
        魔幻域tips
        """

    def mhy_challenge_btn(self):
        """
        魔幻域挑战按钮
        """

    def mhy_fight_result_get_btn(self):
        """
        魔幻域战斗结束领取按钮
        """
