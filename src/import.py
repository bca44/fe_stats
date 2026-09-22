import pandas as pd
import requests as r
from io import StringIO

binding_base_r = r.get('https://serenesforest.net/binding-blade/characters/base-stats/')
binding_base = pd.read_html(StringIO(binding_base_r.text))
binding_base = pd.DataFrame(binding_base[0])
binding_base.to_csv('data/unit_base/binding_base.csv')

binding_unit_growths_r = r.get('https://serenesforest.net/binding-blade/characters/growth-rates/')
binding_unit_growths = pd.read_html(StringIO(binding_unit_growths_r.text))
binding_unit_growths = pd.DataFrame(binding_unit_growths[0])
binding_unit_growths.to_csv('data/unit_growths/binding_unit_growths.csv')

binding_class_growths_r = r.get('https://serenesforest.net/binding-blade/classes/growth-rates/')
binding_class_growths = pd.read_html(StringIO(binding_class_growths_r.text))
binding_class_growths = pd.DataFrame(binding_class_growths[0])
binding_class_growths.to_csv('data/class_growths/binding_class_growths.csv')

binding_promotion_gains_r = r.get('https://serenesforest.net/binding-blade/classes/promotion-gains/')
binding_promotion_gains = pd.read_html(StringIO(binding_promotion_gains_r.text))
binding_promotion_gains = pd.DataFrame(binding_promotion_gains[0])
binding_promotion_gains.to_csv('data/promotion_gains/binding_promotion_gains.csv')


blazing_base_r = r.get('https://serenesforest.net/blazing-sword/characters/base-stats/')
blazing_base = pd.read_html(StringIO(blazing_base_r.text))
blazing_base_0 = pd.DataFrame(blazing_base[0]) #lyn prologue in separate table
blazing_base_1 = pd.DataFrame(blazing_base[1])
blazing_base = pd.concat([blazing_base_0, blazing_base_1])
blazing_base.to_csv('data/unit_base/blazing_base.csv')

blazing_unit_growths_r = r.get('https://serenesforest.net/blazing-sword/characters/growth-rates/')
blazing_unit_growths = pd.read_html(StringIO(blazing_unit_growths_r.text))
blazing_unit_growths = pd.DataFrame(blazing_unit_growths[0])
blazing_unit_growths.to_csv('data/unit_growths/blazing_unit_growths.csv')

blazing_class_growths_r = r.get('https://serenesforest.net/blazing-sword/classes/growth-rates/')
blazing_class_growths = pd.read_html(StringIO(blazing_class_growths_r.text))
blazing_class_growths = pd.DataFrame(blazing_class_growths[0])
blazing_class_growths.to_csv('data/class_growths/blazing_class_growths.csv')

blazing_promotion_gains_r = r.get('https://serenesforest.net/blazing-sword/classes/promotion-gains/')
blazing_promotion_gains = pd.read_html(StringIO(blazing_promotion_gains_r.text))
blazing_promotion_gains = pd.DataFrame(blazing_promotion_gains[0])
blazing_promotion_gains.to_csv('data/promotion_gains/blazing_promotion_gains.csv')

# blazing_class_promotions_r = r.get('https://serenesforest.net/blazing-sword/classes/introduction/')
# blazing_class_promotions = pd.read_html(StringIO(blazing_class_promotions_r.text))
# blazing_class_promotions = pd.DataFrame(blazing_class_promotions[0])
# blazing_class_promotions.to_csv('data/promotion_gains/blazing_class_promotions.csv')
# due to some formatting inconsistencies, the above table required manual editing to be usable. The edited version is saved in the repo as blazing_class_promotions.csv
# please do not mess with it


sacred_base_r = r.get('https://serenesforest.net/the-sacred-stones/characters/base-stats/')
sacred_base = pd.read_html(StringIO(sacred_base_r.text))
sacred_base = pd.DataFrame(sacred_base[0])
sacred_base.to_csv('data/unit_base/sacred_base.csv')

sacred_unit_growths_r = r.get('https://serenesforest.net/the-sacred-stones/characters/growth-rates/')
sacred_unit_growths = pd.read_html(StringIO(sacred_unit_growths_r.text))
sacred_unit_growths = pd.DataFrame(sacred_unit_growths[0])
sacred_unit_growths.to_csv('data/unit_growths/sacred_unit_growths.csv')

sacred_class_growths_r = r.get('https://serenesforest.net/the-sacred-stones/classes/growth-rates/')
sacred_class_growths = pd.read_html(StringIO(sacred_class_growths_r.text))
sacred_class_growths = pd.DataFrame(sacred_class_growths[0])
sacred_class_growths.to_csv('data/class_growths/sacred_class_growths.csv')

sacred_promotion_gains_r = r.get('https://serenesforest.net/the-sacred-stones/classes/promotion-gains/')
sacred_promotion_gains = pd.read_html(StringIO(sacred_promotion_gains_r.text))
sacred_promotion_gains = pd.DataFrame(sacred_promotion_gains[0])
sacred_promotion_gains.to_csv('data/promotion_gains/sacred_promotion_gains.csv')