from random_gen import get_nonplot_chr
import random

def genRandom():
    nonplot_chr = get_nonplot_chr(1)

    encounters = ""
    encounters_file = open("story_options/random_elements/encounters.txt", "r")
    data = encounters_file.read()
    encounters = data.split("\n")

    treasures = ""
    treasures_file = open("story_options/random_elements/treasures.txt", "r")
    data = treasures_file.read()
    treasures = data.split("\n")

    hinderances = ""
    hinderances_file = open("story_options/random_elements/hinderances.txt", "r")
    data = hinderances_file.read()
    hinderances = data.split("\n")

    print('Along the way, the antagonists are beset upon by an unexpected ' + nonplot_chr.pop(0) + ' who unwittingly engages the group in an ' + \
        random.choice(encounters) + '. On the bright side, this results in the acquisition of ' + random.choice(treasures) + ', which comes in handy against a sudden '\
            + random.choice(hinderances) + '.')