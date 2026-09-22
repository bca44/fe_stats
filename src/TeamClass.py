from HeroClass import Hero

class Team:
    def __init__(self, name : str):
        self.name = name
        self.members = []

    def __repr__(self):
        return f"Team {self.name} {{Members: {self.members}}}"

    def add_member(self, *heroes : Hero):
        self.members.extend(heroes)

    def remove_member(self, *heroes : Hero):
        for hero in heroes:
            self.members.remove(hero)

# TODO - add game checking? duplicates checking?
# TODO - add save method - write to JSON format probs, plus read method to construct list from written output
