from GameClass import Game
from TeamClass import Team
from datetime import datetime
import traceback

try:
    SacredStones = Game("Sacred Stones ")
    Eirika = SacredStones.get_hero("Eirika")
    Seth = SacredStones.get_hero("Seth")
    cavalierM = SacredStones.get_class("Cavalier (M)")
    team1 = Team(SacredStones, "team1")
    team1.add(Eirika, Seth)
    # team1.save("team1.txt")

    print(SacredStones.get_top_n("total_growths"))
    print(SacredStones.get_top_n("total_growth", what = "class")) # error testing

except Exception as e:
    print("An error has occured. Please check logs for more details.")
    error_log_filepath = f".logs/{datetime.now().strftime("%Y%m%d_%H%M%S")}"
    
    with open(error_log_filepath, "w") as f:
        f.write(traceback.format_exc())

# TODO add class filtering to GameClass
#   i.e., cavalier = SacredStones.filter(class = "Cavalier")
#   which would return just the pd df, not wrapped in Hero objs or anything

# TODO encase everything in PYInstaller and do more testing
