# from PCClass import PCClass

class Hero:
        ### LATER - EXP attr for encounter sim

    def __init__(self, hero_row):
        self.name = hero_row['name'].item()
        self.current_class = hero_row['base_class'].item()
        self.current_lvl = hero_row['base_lvl'].item()
        self.base_hp = hero_row['base_hp'].item()
        self.base_s_or_m = hero_row['base_s_or_m'].item()
        self.base_skl = hero_row['base_skl'].item()
        self.base_spd = hero_row['base_spd'].item()
        self.base_lck = hero_row['base_lck'].item()
        self.base_def = hero_row['base_def'].item()
        self.base_res = hero_row['base_res'].item()
        self.base_con = hero_row['base_con'].item()
        self.base_mov = hero_row['base_mov'].item()
        self.total_base = hero_row['total_base'].item()

        self.game = hero_row['game'].item()
        self.hp_growth = hero_row['hp_growth'].item()
        self.s_or_m_growth = hero_row['s_or_m_growth'].item()
        self.skl_growth = hero_row['skl_growth'].item()
        self.spd_growth = hero_row['spd_growth'].item()
        self.lck_growth = hero_row['lck_growth'].item()
        self.def_growth = hero_row['def_growth'].item()
        self.res_growth = hero_row['res_growth'].item()
        self.total_growths = hero_row['total_growths'].item()
        
    def __repr__(self):
        return f'{self.name} (LVL {self.current_lvl} {self.current_class})'

### TODO - add lvl_up & change_class methods
    ### change_class will need can_promote_to check live first
### lvl_up - (unit_growths + class_growths)/100 prob -> relevant_stat ++
### change_class - relevant_stat += promotional_gains

### NOTE there is no luck gain for any class/game combo - didn't know that
