import pandas as pd
from HeroClass import Hero
from PCClass import PCClass

hero_df = pd.read_csv("data/hero_df.csv")
class_growths_df = pd.read_csv("data/class_growths_df.csv")
promotion_gains_df = pd.read_csv("data/promotion_gains_df.csv")

if __name__ == "__main__":
    RoyHero = Hero(hero_df[hero_df['name'] == 'Roy'])

    print(f"Testing HeroClass with Roy:\n{RoyHero}")

    LordEirikaClass = PCClass(class_growths_df[class_growths_df['class_name'] == 'Lord (F)'])

    print(f"Testing PCClass with Lord (Eirika):\n{LordEirikaClass}") # base class testing

    SageFClass = PCClass(
        class_growths_df[(class_growths_df['class_name'] == 'Sage (F)') & (class_growths_df['game'] == 'blazing blade')]
        )

    print(f"Testing PCClass with Sage (F):\n{SageFClass}") # promoted class testing

# the testing, so far, is good
# TODO - some kind of search functionality will be necessary.
# the format is different across dfs, ex Lord (F) vs Lord (Eirika), so will need to be able to reference
# the specific formatting when building teams or simming, etc