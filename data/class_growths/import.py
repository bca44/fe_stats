import pandas as pd
import requests as r
from io import StringIO

binding_class_growths_r = r.get('https://serenesforest.net/binding-blade/classes/growth-rates/')
binding_class_growths = pd.read_html(StringIO(binding_class_growths_r.text))
binding_class_growths = pd.DataFrame(binding_class_growths[0])
binding_class_growths.to_csv('data/class_growths/binding_class_growths.csv')

blazing_class_growths_r = r.get('https://serenesforest.net/blazing-sword/classes/growth-rates/')
blazing_class_growths = pd.read_html(StringIO(blazing_class_growths_r.text))
blazing_class_growths = pd.DataFrame(blazing_class_growths[0])
blazing_class_growths.to_csv('data/class_growths/blazing_class_growths.csv')

sacred_class_growths_r = r.get('https://serenesforest.net/the-sacred-stones/classes/growth-rates/')
sacred_class_growths = pd.read_html(StringIO(sacred_class_growths_r.text))
sacred_class_growths = pd.DataFrame(sacred_class_growths[0])
sacred_class_growths.to_csv('data/class_growths/sacred_class_growths.csv')
