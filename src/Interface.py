import pandas as pd

class_growths_df = pd.read_csv("class_growths_df.csv")
hero_df = pd.read_csv("hero_df.csv")
promotion_gains_df = pd.read_csv("promotion_gains_df.csv")

### make command-line callable
def operation_manager():
    ### flags:
    ### search - search hero/unitClass with additional parameters
    ### compare - compare currentHero with others
    ### display - display currentHero
    ### level_up - simulate stat changes on level_up
    ### promote - update currentHero attrs
    ### end - close menu
    choice = input("Please choose a function:\nsearch, compare, display, level_up, promote, help, end\n").lower()
    {'search': search, 'compare': compare, 'display': display, 'level_up': level_up, 'promote': promote, 'help': help_message, 'end': close}[choice]()

### SEARCH by name/class/game
def search():
    hero_or_class = input("Would you like to find a Hero or a Class?\n").lower()
    while hero_or_class not in ['hero', 'class']:
        hero_or_class = input("Please choose a Hero or a Class.\n").lower()

    if hero_or_class == 'hero':
        ### search by name, class, and/or game
        pass
    elif hero_or_class == 'class':
        ### search by ??? TODO
        pass

### COMPARE hero/class by base/growths
def compare():
    print("Comparing...")

### DISPLAY current selection
def display():
    print("Displaying...")

### SIMULATE lvl_up/class_change
def level_up():
    print("Level up...")

def promote():
    print("Promote...")

def help_message():
    print("Help is on the way, dearie!")

def close():
    print("Closing...")

if __name__ == '__main__':
    operation_manager()

### later - encounter sim -> EXP dist -> (maybe) lvl_up
