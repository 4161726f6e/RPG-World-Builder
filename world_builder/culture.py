from random_gen import get_religion
import random

def genCulture():
    names = ""
    name_file = open("map_assets/city_names.txt", "r")
    data = name_file.read()
    names = data.split("\n")

    random.shuffle(names)
    name1 = names.pop()
    random.shuffle(names)
    name2 = names.pop()

    politics = ""
    politics_file = open("story_options/culture/politics.txt", "r")
    data = politics_file.read()
    politics = data.split("\n")

    war = ""
    war_file = open("story_options/culture/war.txt", "r")
    data = war_file.read()
    war = data.split("\n")

    resources = ""
    resources_file = open("story_options/culture/resources.txt", "r")
    data = resources_file.read()
    resources = data.split("\n")

    religion = get_religion(1)

    print('The land of ' + name1 + ', also known as the center of faith for the ' + religion.pop(0) + ', has been focused on ' \
        + random.choice(politics) + '. They recently have been ' + random.choice(war) + ' ' + name2 + ', of which ' + random.choice(resources) \
            + " was a factor.")