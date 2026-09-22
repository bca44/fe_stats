class PCClass:
    def __init__(self, class_growth_row, promotion_gain_row=None):
        ### TODO - would this be better as a DataClass

        self.class_name = class_growth_row['class_name']
        self.hp_growth = class_growth_row['hp_growth']
        self.s_or_m_growth = class_growth_row['s_or_m_growth']
        self.skl_growth = class_growth_row['skl_growth']
        self.spd_growth = class_growth_row['spd_growth']
        self.def_growth = class_growth_row['def_growth']
        self.res_growth = class_growth_row['res_growth']
        self.lck_growth = class_growth_row['lck_growth']
        self.total_growths = class_growth_row['total_growths']
        self.is_promoted_class = False
        if promotion_gain_row is not None:
            self.add_promotion_gains(promotion_gain_row)
        # promotion_gain_row should be passed only if this is a promoted class
        # the gains will be stored with the promoted class, then a later promote() method will into account
        # the gains of the destination PCClass
        # TODO - promote method

    def __repr__(self):
        return f'{self.class_name} {{Promoted Class: {self.is_promoted_class}, Total Growths: {self.total_growths}}}'
        # TODO - add divergent repr methods for base or promoted class - with promotes_to and promotes_from vals respectively

    def add_promotion_gains(self, promotion_gain_row):
        self.is_promoted_class = True
        self.hp_gain = promotion_gain_row['hp_gain']
        self.s_or_m_gain = promotion_gain_row['s_or_m_gain']
        self.skl_gain = promotion_gain_row['skl_gain']
        self.spd_gain = promotion_gain_row['spd_gain']
        self.def_gain = promotion_gain_row['def_gain']
        self.res_gain = promotion_gain_row['res_gain']
        self.con_gain = promotion_gain_row['con_gain']
        self.mov_gain = promotion_gain_row['mov_gain']
        self.total_gains = promotion_gain_row['total_gains']

