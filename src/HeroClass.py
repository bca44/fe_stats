# from PCClass import PCClass

class Hero:
        ### LATER - EXP attr for encounter sim

    def __init__(self, hero_row):
        self.name = hero_row['name']
        self.current_class = hero_row['base_class']
        self.current_lvl = hero_row['base_lvl']
        self.base_hp = hero_row['base_hp']
        self.base_s_or_m = hero_row['base_s_or_m']
        self.base_skl = hero_row['base_skl']
        self.base_spd = hero_row['base_spd']
        self.base_lck = hero_row['base_lck']
        self.base_def = hero_row['base_def']
        self.base_res = hero_row['base_res']
        self.base_con = hero_row['base_con']
        self.base_mov = hero_row['base_mov']
        self.total_base = hero_row['total_base']
        self.hp_growth = hero_row['hp_growth']
        self.s_or_m_growth = hero_row['s_or_m_growth']
        self.skl_growth = hero_row['skl_growth']
        self.spd_growth = hero_row['spd_growth']
        self.lck_growth = hero_row['lck_growth']
        self.def_growth = hero_row['def_growth']
        self.res_growth = hero_row['res_growth']
        self.total_growths = hero_row['total_growths']
        
    def __repr__(self):
        return f'{self.name} (LVL {self.current_lvl} {self.current_class})'

### TODO - add lvl_up & change_class methods
    ### change_class will need can_promote_to check live first
### lvl_up - (unit_growths + class_growths)/100 prob -> relevant_stat ++
### change_class - relevant_stat += promotional_gains

### there is no luck gain for any class/game combo - didn't know that
