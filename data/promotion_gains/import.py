import pandas as pd
import requests as r
from io import StringIO

binding_promotion_gains_r = r.get('https://serenesforest.net/binding-blade/classes/promotion-gains/')
binding_promotion_gains = pd.read_html(StringIO(binding_promotion_gains_r.text))
binding_promotion_gains = pd.DataFrame(binding_promotion_gains[0])
binding_promotion_gains.to_csv('data/promotion_gains/binding_promotion_gains.csv')

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

sacred_promotion_gains_r = r.get('https://serenesforest.net/the-sacred-stones/classes/promotion-gains/')
sacred_promotion_gains = pd.read_html(StringIO(sacred_promotion_gains_r.text))
sacred_promotion_gains = pd.DataFrame(sacred_promotion_gains[0])
sacred_promotion_gains.to_csv('data/promotion_gains/sacred_promotion_gains.csv')
