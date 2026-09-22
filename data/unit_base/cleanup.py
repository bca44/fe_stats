import pandas as pd


binding_base = pd.read_csv('data/unit_base/binding_base.csv').drop(columns=['Affin', 'Weapon ranks'])

blazing_base = pd.read_csv('data/unit_base/blazing_base.csv').drop(columns=['Affin', 'Weapon ranks'])

sacred_base = pd.read_csv('data/unit_base/sacred_base.csv').drop(columns=['Affin', 'Weapon Rank'])
sacred_base.rename(columns={'Str': 'S/M'}, inplace=True)

df_list = [binding_base, blazing_base, sacred_base]
# DROP unneeded cols & header rows
blazing_base.drop(columns=['Weapon Ranks'], inplace=True)
blazing_base.drop(blazing_base[blazing_base['Name'] == "Nils"].index, inplace = True)
for df in df_list:

    df.drop(columns=['Unnamed: 0'], inplace=True)
    df.drop(df[df['Name'] == 'Character'].index, inplace=True)
    df.drop(df[df['Name'] == 'Name'].index, inplace=True)

for df in df_list:

    df.rename(columns={'Name':'name',
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

    int_columns = [col for col in df.columns if col not in ['name', 'base_class', 'game']]
    df[int_columns] = df[int_columns].astype(int)

    df['total_base'] = df[['base_hp', 'base_s_or_m', 'base_skl',
                           'base_spd', 'base_lck', 'base_def',
                           'base_res', 'base_con']].sum(axis=1)

# [print(df.head()) for df in df_list]

binding_base.to_csv('data/unit_base/binding_base.csv')
blazing_base.to_csv('data/unit_base/blazing_base.csv')
sacred_base.to_csv('data/unit_base/sacred_base.csv')
