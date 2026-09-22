from GameClass import Game
from TeamClass import Team

SacredStones = Game("Sacred Stones ")
Eirika = SacredStones.get_hero("Eirika")
# print(Eirika)
Seth = SacredStones.get_hero("Seth")

cavalierM = SacredStones.get_class("Cavalier (M)")
# print(cavalierM)

team1 = Team("team1")
team1.add_member(Eirika, Seth)
print(team1)

team1.remove_member(Eirika, Seth)
print(team1)