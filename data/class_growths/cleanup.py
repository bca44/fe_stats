import pandas as pd

binding_class_growths = pd.read_csv('data/class_growths/binding_class_growths.csv')

blazing_class_growths = pd.read_csv('data/class_growths/blazing_class_growths.csv')
blazing_class_growths.rename(columns={'Name': 'Class'}, inplace=True)

sacred_class_growths = pd.read_csv('data/class_growths/sacred_class_growths.csv')

for df in [binding_class_growths, blazing_class_growths, sacred_class_growths]:

    df.drop(columns=['Unnamed: 0'], inplace=True)
    df.drop(df[df['Class'] == 'Class'].index, inplace=True)
    df.drop(df[df['Class'] == 'Name'].index, inplace=True)

df_list = [binding_class_growths, blazing_class_growths, sacred_class_growths]

for df in df_list:
    df.rename(columns={'Class': 'class_name',
                           'HP':'hp_growth',
                           'S/M':'s_or_m_growth',
                           'Skl':'skl_growth',
                           'Spd':'spd_growth',
                           'Lck':'lck_growth',
                           'Def':'def_growth',
                           'Res':'res_growth'}, inplace=True)
    
    int_columns = [col for col in df.columns if col not in ['class_name', 'game']]
    df[int_columns] = df[int_columns].astype(int)

    df['total_growths'] = df[['hp_growth', 's_or_m_growth',
                            'skl_growth', 'spd_growth', 'lck_growth',
                            'def_growth', 'res_growth']].sum(axis=1)

binding_class_growths = binding_class_growths[['class_name', 'hp_growth', 's_or_m_growth', 'skl_growth', 'spd_growth', 'lck_growth', 'def_growth', 'res_growth', 'total_growths']]

# [print(df.head()) for df in df_list]

binding_class_growths.to_csv('data/class_growths/binding_class_growths.csv')
blazing_class_growths.to_csv('data/class_growths/blazing_class_growths.csv')
sacred_class_growths.to_csv('data/class_growths/sacred_class_growths.csv')
