
import random

def genPlot():
    journey = ""
    journey_file = open("story_options/plot/journey.txt", "r")
    data = journey_file.read()
    journey = data.split("\n")

    conflict = ""
    conflict_file = open("story_options/plot/conflict.txt", "r")
    data = conflict_file.read()
    conflict = data.split("\n")

    resolution = ""
    resolution_file = open("story_options/plot/resolution.txt", "r")
    data = resolution_file.read()
    resolution = data.split("\n")

    print('Our hero must ' + random.choice(journey) + ', a task that requires them to ' + random.choice(conflict) + ' so that ' \
        + random.choice(resolution) + '.')