# -*- encoding=utf8 -*-

import abc


class Flow(metaclass=abc.ABCMeta):

    def __init__(self):
        pass

    @abc.abstractmethod
    def newbie_guide(self):
        """
        新手引导
        """
        pass

    @abc.abstractmethod
    def upgrade(self, names, get_task_reward=False):
        """
        英雄升级，可以领取升级任务奖励

        :param names: 英雄名称
        :param get_task_reward: 是否需要领取英雄升级任务奖励
        """
        pass

    @abc.abstractmethod
    def equip_upgrade(self, name, equip_index, one_key_max=True, current_level=1, level=1, suit_up=True):
        """
        装备升级

        :param name: 英雄名称--
        :param equip_index: 升级某个装备或者全部升级，单个装备升级传入1-4，全部升级请传入0
        :param one_key_max: 一键把装备升满级
        :param current_level: 装备当前等级，这个参数能极大提升运行效率
        :param level: 对指定装备提升多少等级
        :param suit_up: 是否需要一键穿戴装备，默认会一键点击穿戴装备
        """

    @abc.abstractmethod
    def fetter_upgrade(self, name):
        """
        羁绊激活升级，需要先激活当前羁绊，如条件不满足时会将所对应的羁绊的英雄升到顶级

        :param name: 羁绊名称
        """

    @abc.abstractmethod
    def mhy(self, times):
        """
        魔幻域

        :param times: 挑战魔幻域的次数
        """

    @abc.abstractmethod
    def infinity_war(self, current_floor, fight_times):
        """
        无限战斗

        :param current_floor: 当前关卡的尾数，主要为了判断是否需要选择buff
        :param fight_times: 想要战斗的次数
        """
