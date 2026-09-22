from unit_class import UnitClass

class Hero:
    def __init__(self, name, base_class, base_lvl, base_hp, base_s_or_m, base_skl, base_spd, base_lck, base_def, base_res, base_con, base_mov, game,
                 hp_growth, s_or_m_growth, skl_growth, spd_growth, lck_growth, def_growth, res_growth, total_base, total_growths):

        ### TODO - would this be better as a DataClass

        self.name = name
        self.current_class = base_class
        self.current_lvl = base_lvl
        self.base_hp = base_hp
        self.base_s_or_m = base_s_or_m
        self.base_skl = base_skl
        self.base_spd = base_spd
        self.base_lck = base_lck
        self.base_def = base_def
        self.base_res = base_res
        self.base_con = base_con
        self.base_mov = base_mov
        self.total_base = total_base

        self.game = game
        self.hp_growth = hp_growth
        self.s_or_m_growth = s_or_m_growth
        self.skl_growth = skl_growth
        self.spd_growth = spd_growth
        self.lck_growth = lck_growth
        self.def_growth = def_growth
        self.res_growth = res_growth
        self.total_growths = total_growths

        self.max_hp = base_hp
        self.s_or_m = base_s_or_m
        self.skl = base_skl
        self.spd = base_spd
        self.lck = base_lck
        self._def = base_def
        self.res = base_res
        self.con = base_con
        self.mov = base_mov

        ### LATER - EXP attr for encounter sim

    def __repr__(self):
        return f'{self.name} (lvl {self.current_lvl} {self.current_class})'

### TODO - add lvl_up & change_class methods
    ### change_class will need can_promote_to check live first
### lvl_up - (unit_growths + class_growths)/100 prob -> relevant_stat ++
### change_class - relevant_stat += promotional_gains

### NOTE there is no luck gain for any class/game combo - didn't know that
