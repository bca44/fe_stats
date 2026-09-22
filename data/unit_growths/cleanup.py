import pandas as pd

binding_unit_growths = pd.read_csv('data/unit_growths/binding_unit_growths.csv')

blazing_unit_growths = pd.read_csv('data/unit_growths/blazing_unit_growths.csv')

sacred_unit_growths = pd.read_csv('data/unit_growths/sacred_unit_growths.csv')

# DROP unneeded cols & header rows
for df in [binding_unit_growths, blazing_unit_growths, sacred_unit_growths]:

    df.drop(columns=['Unnamed: 0'], inplace=True)
    df.drop(df[df['Name'] == 'Character'].index, inplace=True)
    df.drop(df[df['Name'] == 'Name'].index, inplace=True)

df_list = [binding_unit_growths, blazing_unit_growths, sacred_unit_growths]

for df in df_list:
    df.rename(columns={'Name': 'name',
                           'HP':'hp_growth',
                           'S/M':'s_or_m_growth',
                           'Skl':'skl_growth',
                           'Spd':'spd_growth',
                           'Lck':'lck_growth',
                           'Def':'def_growth',
                           'Res':'res_growth'}, inplace=True)

for df in df_list:
    int_columns = [col for col in df.columns if col not in ['name', 'base_class', 'game']]
    df[int_columns] = df[int_columns].astype(int)

    df['total_growths'] = df[['hp_growth', 's_or_m_growth', 'skl_growth',
                            'spd_growth', 'lck_growth', 'def_growth',
                            'res_growth']].sum(axis=1)

# [print(df.head()) for df in df_list]

binding_unit_growths.to_csv('data/unit_growths/binding_unit_growths.csv')

blazing_unit_growths.to_csv('data/unit_growths/blazing_unit_growths.csv')

sacred_unit_growths.to_csv('data/unit_growths/sacred_unit_growths.csv')