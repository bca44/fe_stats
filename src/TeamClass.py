from HeroClass import Hero
from GameClass import Game

class Team:
    def __init__(self, game : Game, name : str):
        self.name = name
        self.game = game
        self.members = []
        self.member_names = []

    def __repr__(self):
        return f"Team {self.name} {{Members: {self.members}}}"

    def add(self, *heroes : Hero):
        for hero in heroes:
            self.members.append(hero)
            self.member_names.append(hero.name)

    def remove(self, *heroes : Hero):
        for hero in heroes:
            self.members.remove(hero)
            self.member_names.remove(hero.name)

    def save(self, filepath):
        with open(filepath, "w") as f:
            f.write(f"{{\n\tname: {self.name},\n\tgame: {self.game.game_name},\n\tmembers:\n\t\t{self.members}\n}}")
            

# TODO - add game checking? duplicates checking?
