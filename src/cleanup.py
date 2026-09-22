import pandas as pd

# READ IN data
binding_base = pd.read_csv('data/unit_base/binding_base.csv').drop(columns=['Affin', 'Weapon ranks'])
binding_unit_growths = pd.read_csv('data/unit_growths/binding_unit_growths.csv')
binding_class_growths = pd.read_csv('data/class_growths/binding_class_growths.csv')
binding_promotion_gains = pd.read_csv('data/promotion_gains/binding_promotion_gains.csv')

blazing_base = pd.read_csv('data/unit_base/blazing_base.csv').drop(columns=['Affin', 'Weapon ranks'])
blazing_unit_growths = pd.read_csv('data/unit_growths/blazing_unit_growths.csv')
blazing_class_growths = pd.read_csv('data/class_growths/blazing_class_growths.csv')
blazing_class_growths.rename(columns={'Name': 'Class'}, inplace=True)
blazing_promotion_gains = pd.read_csv('data/promotion_gains/blazing_promotion_gains.csv')

sacred_base = pd.read_csv('data/unit_base/sacred_base.csv').drop(columns=['Affin', 'Weapon Rank'])
sacred_unit_growths = pd.read_csv('data/unit_growths/sacred_unit_growths.csv')
sacred_class_growths = pd.read_csv('data/class_growths/sacred_class_growths.csv')
sacred_promotion_gains = pd.read_csv('data/promotion_gains/sacred_promotion_gains.csv')

# DROP unneeded cols & header rows
for df in [binding_base, binding_unit_growths,
           blazing_base, blazing_unit_growths,
           sacred_base, sacred_unit_growths]:

    df.drop(columns=['Unnamed: 0'], inplace=True)
    df.drop(df[df['Name'] == 'Character'].index, inplace=True)
    df.drop(df[df['Name'] == 'Name'].index, inplace=True)

for df in [binding_class_growths, blazing_class_growths, sacred_class_growths]:

    df.drop(columns=['Unnamed: 0'], inplace=True)
    df.drop(df[df['Class'] == 'Class'].index, inplace=True)
    df.drop(df[df['Class'] == 'Name'].index, inplace=True)

binding_promotion_gains.drop(columns=['Unnamed: 0', 'Weapon ranks'], inplace=True)
blazing_promotion_gains.drop(columns=['Unnamed: 0', 'Weapon EXP'], inplace=True)
sacred_promotion_gains.drop(columns=['Unnamed: 0', 'Weapon Ranks'], inplace=True)

for df in [binding_promotion_gains, blazing_promotion_gains, sacred_promotion_gains]:

    df.drop(df[df['Class'] == 'Class'].index, inplace=True)
    df.drop(df[df['Class'] == 'Name'].index, inplace=True)

# SET game col
for df in [binding_base, binding_unit_growths, binding_class_growths, binding_promotion_gains]:
    df['game'] = 'binding blade'

for df in [blazing_base, blazing_unit_growths, blazing_class_growths, blazing_promotion_gains]:
    df['game'] = 'blazing blade'

sacred_base.rename(columns={'Str': 'S/M'}, inplace=True)
for df in [sacred_base, sacred_unit_growths, sacred_class_growths, sacred_promotion_gains]:
    df['game'] = 'sacred stones'

# RENAME cols
base_df = pd.concat([binding_base, blazing_base, sacred_base]).drop('Weapon Ranks', axis=1)
base_df.rename(columns={'Name':'name',
                        'Class':'base_class',
                        'Lv':'base_lvl',
                        'HP':'base_hp',
                        'S/M':'base_s_or_m',
                        'Skl':'base_skl',
                        'Spd':'base_spd',
                        'Lck':'base_lck',
                        'Def':'base_def',
                        'Res':'base_res',
                        'Con':'base_con',
                        'Mov':'base_mov',
                        'Game':'base_game'}, inplace=True)

unit_growths_df = pd.concat([binding_unit_growths, blazing_unit_growths, sacred_unit_growths])
unit_growths_df.rename(columns={'Name': 'name',
                           'HP':'hp_growth',
                           'S/M':'s_or_m_growth',
                           'Skl':'skl_growth',
                           'Spd':'spd_growth',
                           'Lck':'lck_growth',
                           'Def':'def_growth',
                           'Res':'res_growth'}, inplace=True)

class_growths_df = pd.concat([binding_class_growths, blazing_class_growths, sacred_class_growths])
class_growths_df.rename(columns={'Class': 'class_name',
                           'HP':'hp_growth',
                           'S/M':'s_or_m_growth',
                           'Skl':'skl_growth',
                           'Spd':'spd_growth',
                           'Lck':'lck_growth',
                           'Def':'def_growth',
                           'Res':'res_growth'}, inplace=True)

promotion_gains_df = pd.concat([binding_promotion_gains, blazing_promotion_gains])
promotion_gains_df.rename(columns={'Class': 'base_class',
                                   'Promotion': 'promoted_class',
                                   'HP': 'hp_gain',
                                   'S/M': 's_or_m_gain',
                                   'Skl': 'skl_gain',
                                   'Spd': 'spd_gain',
                                   'Lck': 'lck_gain',
                                   'Def': 'def_gain',
                                   'Res': 'res_gain',
                                   'Con': 'con_gain',
                                   'Mov': 'mov_gain'}, inplace=True
                          )

hero_df = pd.merge(base_df, unit_growths_df, on=['name', 'game'])

# CHANGE col types
int_columns = [col for col in hero_df.columns if col not in ['name', 'base_class', 'game']]
hero_df[int_columns] = hero_df[int_columns].astype(int)

int_columns = [col for col in class_growths_df.columns if col not in ['class_name', 'game']]
class_growths_df[int_columns] = class_growths_df[int_columns].astype(int)

int_columns = [col for col in promotion_gains_df.columns if col not in ['base_class', 'promoted_class', 'game']]
promotion_gains_df[int_columns] = promotion_gains_df[int_columns].astype(int)

# ADD calculated cols
hero_df['total_base'] = hero_df[['base_hp', 'base_s_or_m', 'base_skl',
                           'base_spd', 'base_lck', 'base_def',
                           'base_res', 'base_con']].sum(axis=1)

hero_df['total_growths'] = hero_df[['hp_growth', 's_or_m_growth', 'skl_growth',
                            'spd_growth', 'lck_growth', 'def_growth',
                            'res_growth']].sum(axis=1)

class_growths_df['total_growths'] = class_growths_df[['hp_growth', 's_or_m_growth',
                            'skl_growth', 'spd_growth', 'lck_growth',
                            'def_growth', 'res_growth']].sum(axis=1)

promotion_gains_df['total_gains'] = promotion_gains_df[['hp_gain', 's_or_m_gain',
                            'skl_gain', 'spd_gain', 'def_gain',
                            'res_gain', 'con_gain', 'mov_gain']].sum(axis=1)

hero_df.to_csv("hero_df.csv")
class_growths_df.to_csv("class_growths_df.csv")
promotion_gains_df.to_csv("promotion_gains_df.csv")


if __name__ == '__main__':
    print("HERO")
    print(hero_df.head())
    print(hero_df.columns)

    print("CLASS GROWTHS")
    print(class_growths_df.head())
    print(class_growths_df.columns)

    print("PROMOTION GAINS")
    print(promotion_gains_df.head())
    print(promotion_gains_df.columns)
