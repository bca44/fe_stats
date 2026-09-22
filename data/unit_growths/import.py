import pandas as pd
import requests as r
from io import StringIO

binding_unit_growths_r = r.get('https://serenesforest.net/binding-blade/characters/growth-rates/')
binding_unit_growths = pd.read_html(StringIO(binding_unit_growths_r.text))
binding_unit_growths = pd.DataFrame(binding_unit_growths[0])
binding_unit_growths.to_csv('data/unit_growths/binding_unit_growths.csv')

blazing_unit_growths_r = r.get('https://serenesforest.net/blazing-sword/characters/growth-rates/')
blazing_unit_growths = pd.read_html(StringIO(blazing_unit_growths_r.text))
blazing_unit_growths = pd.DataFrame(blazing_unit_growths[0])
blazing_unit_growths.to_csv('data/unit_growths/blazing_unit_growths.csv')

sacred_unit_growths_r = r.get('https://serenesforest.net/the-sacred-stones/characters/growth-rates/')
sacred_unit_growths = pd.read_html(StringIO(sacred_unit_growths_r.text))
sacred_unit_growths = pd.DataFrame(sacred_unit_growths[0])
sacred_unit_growths.to_csv('data/unit_growths/sacred_unit_growths.csv')
