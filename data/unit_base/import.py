import pandas as pd
import requests as r
from io import StringIO


binding_base_r = r.get('https://serenesforest.net/binding-blade/characters/base-stats/')
binding_base = pd.read_html(StringIO(binding_base_r.text))
binding_base = pd.DataFrame(binding_base[0])
binding_base.to_csv('data/unit_base/binding_base.csv')



blazing_base_r = r.get('https://serenesforest.net/blazing-sword/characters/base-stats/')
blazing_base = pd.read_html(StringIO(blazing_base_r.text))
blazing_base_0 = pd.DataFrame(blazing_base[0]) #lyn prologue in separate table
blazing_base_1 = pd.DataFrame(blazing_base[1])
blazing_base = pd.concat([blazing_base_0, blazing_base_1])
blazing_base.to_csv('data/unit_base/blazing_base.csv')


sacred_base_r = r.get('https://serenesforest.net/the-sacred-stones/characters/base-stats/')
sacred_base = pd.read_html(StringIO(sacred_base_r.text))
sacred_base = pd.DataFrame(sacred_base[0])
sacred_base.to_csv('data/unit_base/sacred_base.csv')