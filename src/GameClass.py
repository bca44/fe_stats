from HeroClass import Hero
from PCClass import PCClass
import pandas as pd

class Game:

    game_dict = {
        "binding blade": {
            "prefix": "binding"
        },
        "blazing blade": {
            "prefix": "blazing"
        },
        "sacred stones": {
            "prefix": "sacred"
        }
    }

    def __init__(self, game_name):
        self.game_name = game_name.lower().strip()

        prefix = self.game_dict[self.game_name]["prefix"]

        unit_base_df = pd.read_csv(
            f"data/unit_base/{prefix}_base.csv"
        )

        unit_growths_df = pd.read_csv(
            f"data/unit_growths/{prefix}_unit_growths.csv"
        )

        self.hero_df = pd.merge(
            unit_base_df,
            unit_growths_df,
            on="name"
        )

        self.class_df = pd.read_csv(
            f"data/class_growths/{prefix}_class_growths.csv"
        )

        self.heroes = {
            row["name"]: Hero(row) for _, row in self.hero_df.iterrows()
        }

        self.classes = {
            row["class_name"]: PCClass(row)
            for _, row in self.class_df.iterrows()
        }

    def get_hero(self, name):
        return self.heroes[name]

    def get_class(self, name):
        return self.classes[name]
