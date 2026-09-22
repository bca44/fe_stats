class PCClass:
    def __init__(self, class_growth_row, promotion_gain_row=None):
        ### TODO - would this be better as a DataClass

        self.class_name = class_growth_row['class_name'].item()
        self.hp_growth = class_growth_row['hp_growth'].item()
        self.s_or_m_growth = class_growth_row['s_or_m_growth'].item()
        self.skl_growth = class_growth_row['skl_growth'].item()
        self.spd_growth = class_growth_row['spd_growth'].item()
        self.def_growth = class_growth_row['def_growth'].item()
        self.res_growth = class_growth_row['res_growth'].item()
        self.lck_growth = class_growth_row['lck_growth'].item()
        self.game = class_growth_row['game'].item()
        self.total_growths = class_growth_row['total_growths'].item()

        # promotion_gain_row should be passed only if this is a promoted class
        # the gains will be stored with the promoted class, then a later promote() method will into account
        # the gains of the destination PCClass
        # TODO - promote method
        if promotion_gain_row is not None:
            self.add_promotion_gains(promotion_gain_row)

    def __repr__(self):
        return f'{self.class_name} (Total Growths: {self.total_growths})'

    def add_promotion_gains(self, promotion_gain_row):
        self.hp_gain = promotion_gain_row['hp_gain'].item()
        self.s_or_m_gain = promotion_gain_row['s_or_m_gain'].item()
        self.skl_gain = promotion_gain_row['skl_gain'].item()
        self.spd_gain = promotion_gain_row['spd_gain'].item()
        self.def_gain = promotion_gain_row['def_gain'].item()
        self.res_gain = promotion_gain_row['res_gain'].item()
        self.con_gain = promotion_gain_row['con_gain'].item()
        self.mov_gain = promotion_gain_row['mov_gain'].item()
        self.total_gains = promotion_gain_row['total_gains'].item()

