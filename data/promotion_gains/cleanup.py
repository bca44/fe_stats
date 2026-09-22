import pandas as pd

binding_promotion_gains = pd.read_csv('data/promotion_gains/binding_promotion_gains.csv')

blazing_promotion_gains = pd.read_csv('data/promotion_gains/blazing_promotion_gains.csv')
blazing_class_promotions = pd.read_csv('data/promotion_gains/blazing_class_promotionsFINAL_HAND_EDITED.csv')
blazing_promotion_gains.rename(columns={'Class': 'Promotion'}, inplace=True)
blazing_promotion_gains = pd.merge(blazing_promotion_gains, blazing_class_promotions, how='left', left_on='Promotion', right_on='Promotes to')

sacred_promotion_gains = pd.read_csv('data/promotion_gains/sacred_promotion_gains.csv')

binding_promotion_gains.drop(columns=['Unnamed: 0', 'Weapon ranks'], inplace=True)
blazing_promotion_gains.drop(columns=['Unnamed: 0_x', 'Promotes to', 'Unnamed: 0_y', 'Icon', 'Weapon EXP', 'Weapons', 'Notes'], inplace=True)
sacred_promotion_gains.drop(columns=['Unnamed: 0', 'Weapon Ranks'], inplace=True)

df_list = [binding_promotion_gains, blazing_promotion_gains, sacred_promotion_gains]
for df in df_list:
    df.drop(df[df['Class'] == 'Class'].index, inplace=True)
    df.drop(df[df['Class'] == 'Name'].index, inplace=True)
    df.rename(columns={'Class': 'base_class',
                                   'Promotion': 'promoted_class',
                                   'HP': 'hp_gain',
                                   'S/M': 's_or_m_gain',
                                   'Skl': 'skl_gain',
                                   'Spd': 'spd_gain',
                                   'Lck': 'lck_gain',
                                   'Def': 'def_gain',
                                   'Res': 'res_gain',
                                   'Con': 'con_gain',
                                   'Mov': 'mov_gain'}, inplace=True)
    int_columns = [col for col in df.columns if col not in ['base_class', 'promoted_class', 'game']]
    df[int_columns] = df[int_columns].astype(int)

    df['total_gains'] = df[['hp_gain', 's_or_m_gain',
                            'skl_gain', 'spd_gain', 'def_gain',
                            'res_gain', 'con_gain', 'mov_gain']].sum(axis=1)

blazing_promotion_gains = blazing_promotion_gains[['base_class', 'promoted_class', 'hp_gain', 's_or_m_gain', 'skl_gain', 'spd_gain', 'def_gain', 'res_gain', 'con_gain', 'mov_gain', 'total_gains']]

# [print(df.head()) for df in df_list]

binding_promotion_gains.to_csv('data/promotion_gains/binding_promotion_gains.csv')
blazing_promotion_gains.to_csv('data/promotion_gains/blazing_promotion_gains.csv')
sacred_promotion_gains.to_csv('data/promotion_gains/sacred_promotion_gains.csv')
