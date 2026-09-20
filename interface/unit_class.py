from cleanup import *

class UnitClass:
    def __init__(self, class_name, hp_growth, s_or_m_growth, skl_growth, spd_growth, def_growth, res_growth, lck_growth, game, total_growths, hp_gain=0, s_or_m_gain=0, skl_gain=0, spd_gain=0, def_gain=0, res_gain=0, con_gain=0, mov_gain=0, total_gains=0):
        ### TODO - would this be better as a DataClass

        self.class_name = class_name
        self.hp_growth = hp_growth
        self.s_or_m_growth = s_or_m_growth
        self.skl_growth = skl_growth
        self.spd_growth = spd_growth
        self.def_growth = def_growth
        self.res_growth = res_growth
        self.lck_growth = lck_growth
        self.game = game
        self.total_growths = total_growths
        self.hp_gain = hp_gain
        self.s_or_m_gain = s_or_m_gain
        self.skl_gain = skl_gain
        self.spd_gain = spd_gain
        self.def_gain = def_gain
        self.res_gain = res_gain
        self.con_gain = con_gain
        self.mov_gain = mov_gain
        self.total_gains = total_gains

    def __repr__(self):
        return self.class_name

