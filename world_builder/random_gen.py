
import numpy as np

names_used = [""]

def name_taken(place_name):
        # See if a generated name has already been used.
        taken = False
        for i in names_used:
            if i == place_name:
                taken = True
        return taken

def get_religion(m):
    name = ""
    while m > 0:
        start = ""
        n = np.random.randint(26)
        if n < 1:
            start = "Children of "
        elif n < 2:
            start = "Disciples of "
        elif n < 3:
            start = "Congregation of "
        elif n < 4:
            start = "Faith of "
        elif n < 5:
            start = "Servants of "
        elif n < 6:
            start = "Warriors of "
        elif n < 7:
            start = "Church of "
        elif n < 8:
            start = "Martyrs of "
        elif n < 9:
            start = "Followers of "
        elif n < 10:
            start = "Order of "
        elif n < 11:
            start = "Holy "
        elif n < 12:
            start = "Sacred "
        elif n < 13:
            start = "Most High "
        elif n < 14:
            start = "Exalted "
        elif n < 15:
            start = "Divine "
        elif n < 16:
            start = "Hallowed "
        elif n < 17:
            start = "Revered "
        elif n < 18:
            start = "Blessed "
        elif n < 19:
            start = "Righteous "
        elif n < 20:
            start = "Saint "
        elif n < 21:
            start = "Pure "
        elif n < 22:
            start = "Dread "
        elif n < 23:
            start = "Fearful "
        elif n < 24:
            start = "Immaculate "
        elif n < 25:
            start = "Terrible "
        elif n < 26:
            start = "Way of "

        middle = ""
        n = np.random.randint(25)
        if n < 1:
            middle = "Andr"
        elif n < 2:
            middle = "Takh"
        elif n < 3:
            middle = "Shogg"
        elif n < 4:
            middle = "Marth"
        elif n < 5:
            middle = "Byz"
        elif n < 6:
            middle = "Seth"
        elif n < 7:
            middle = "Ranc"
        elif n < 8:
            middle = "Kryz"
        elif n < 9:
            middle = "Fion"
        elif n < 10:
            middle = "Zapp"
        elif n < 11:
            middle = "Mehr"
        elif n < 12:
            middle = "Meph"
        elif n < 13:
            middle = "Raph"
        elif n < 14:
            middle = "Metatr"
        elif n < 15:
            middle = "Xenom"
        elif n < 16:
            middle = "Gluh"
        elif n < 17:
            middle = "Ryj"
        elif n < 18:
            middle = "Trans"
        elif n < 19:
            middle = "Tryph"
        elif n < 20:
            middle = "Shub"
        elif n < 21:
            middle = "Nyx"
        elif n < 22:
            middle = "Bob"
        elif n < 23:
            middle = "Niah"
        elif n < 24:
            middle = "Aar"
        elif n < 25:
            middle = "Aman"

        end = ""
        n = np.random.randint(25)
        if n < 1:
            end = "ythal"
        elif n < 2:
            end = "on"
        elif n < 3:
            end = "da"
        elif n < 4:
            end = "aoth"
        elif n < 5:
            end = "den"
        elif n < 6:
            end = "fall"
        elif n < 7:
            end = "dor"
        elif n < 8:
            end = "alha"
        elif n < 9:
            end = "ynneth"
        elif n < 10:
            end = "onadon"
        elif n < 11:
            end = "illian"
        elif n < 12:
            end = "urtz"
        elif n < 13:
            end = "elluvia"
        elif n < 14:
            end = "allory"
        elif n < 15:
            end = "itz"
        elif n < 16:
            end = "ikhea"
        elif n < 17:
            end = "itzen"
        elif n < 18:
            end = "ykariah"
        elif n < 19:
            end = "yvalla"
        elif n < 20:
            end = "ootz"
        elif n < 21:
            end = "unkweh"
        elif n < 22:
            end = "ipple"
        elif n < 23:
            end = "azagon"
        elif n < 24:
            end = "abonibah"
        elif n < 25:
            end = "oof"
        
        name = start + middle + end
        if not name_taken(name):
            names_used.append(name)
            m -= 1

    names_used.pop(0)
    return names_used

def get_nonplot_chr(m):
    name = ""
    names_used.clear()

    while m > 0:
        start = ""
        n = np.random.randint(26)
        if n < 1:
            start = "insane "
        elif n < 2:
            start = "hostile "
        elif n < 3:
            start = "greedy "
        elif n < 4:
            start = "nosy "
        elif n < 5:
            start = "self-righteous "
        elif n < 6:
            start = "moody "
        elif n < 7:
            start = "aggressively helpful "
        elif n < 8:
            start = "narcoleptic "
        elif n < 9:
            start = "jovial "
        elif n < 10:
            start = "perplexing "
        elif n < 11:
            start = "indignant "
        elif n < 12:
            start = "motherly "
        elif n < 13:
            start = "traitorous "
        elif n < 14:
            start = "whimsical "
        elif n < 15:
            start = "generous "
        elif n < 16:
            start = "intimidating "
        elif n < 17:
            start = "wisecracking "
        elif n < 18:
            start = "extremely loud "
        elif n < 19:
            start = "depressed "
        elif n < 20:
            start = "extremely anxious "
        elif n < 21:
            start = "uncomfortably randy "
        elif n < 22:
            start = "narcissistic "
        elif n < 23:
            start = "manic "
        elif n < 24:
            start = "slovenly "
        elif n < 25:
            start = "immaculate "
        elif n < 26:
            start = "anachronistic "

        middle = ""
        n = np.random.randint(25)
        if n < 1:
            middle = "cabbage cart vendor "
        elif n < 2:
            middle = "travelling merchant "
        elif n < 3:
            middle = "religious zealot "
        elif n < 4:
            middle = "barbarian woman "
        elif n < 5:
            middle = "entertainer "
        elif n < 6:
            middle = "mercenary "
        elif n < 7:
            middle = "bounty hunter "
        elif n < 8:
            middle = "former house servant "
        elif n < 9:
            middle = "convicted felon "
        elif n < 10:
            middle = "exiled member of a foreign royal court "
        elif n < 11:
            middle = "man "
        elif n < 12:
            middle = "peasant "
        elif n < 13:
            middle = "crafty wizard in disguise "
        elif n < 14:
            middle = "deity "
        elif n < 15:
            middle = "crown prince "
        elif n < 16:
            middle = "adventurer "
        elif n < 17:
            middle = "shepherd "
        elif n < 18:
            middle = "hunter "
        elif n < 19:
            middle = "diplomat "
        elif n < 20:
            middle = "errand boy "
        elif n < 21:
            middle = "travelling artist "
        elif n < 22:
            middle = "monk "
        elif n < 23:
            middle = "soldier "
        elif n < 24:
            middle = "lost child "
        elif n < 25:
            middle = "otherworldly being "

        end = ""
        n = np.random.randint(25)
        if n < 1:
            end = "on the run from the law"
        elif n < 2:
            end = "looking for fun"
        elif n < 3:
            end = "plotting evil"
        elif n < 4:
            end = "on a mission"
        elif n < 5:
            end = "with an attitude"
        elif n < 6:
            end = "with no sense of personal space"
        elif n < 7:
            end = "who believes the world is ending"
        elif n < 8:
            end = "who has become the voice of a previously unknown god"
        elif n < 9:
            end = "exploring the wilderness"
        elif n < 10:
            end = "looking for a fight"
        elif n < 11:
            end = "with a keen fashion sense"
        elif n < 12:
            end = "who is unafraid of everything except cats"
        elif n < 13:
            end = "who evangelizes their favorite workout routine"
        elif n < 14:
            end = "who will not take no for an answer"
        elif n < 15:
            end = "who everyone else can see is actually three feet taller than they think they are"
        elif n < 16:
            end = "with a deep fear of thunder"
        elif n < 17:
            end = "who misinteprets everything that is said to them as the opposite of the actual meaning"
        elif n < 18:
            end = "who is looking for love in all the wrong places"
        elif n < 19:
            end = "who is looking to start a revolution"
        elif n < 20:
            end = "who dropped out of college but believes that they know everything about everything"
        elif n < 21:
            end = "who recently became religious and wants to tell you all about it"
        elif n < 22:
            end = "who saw a dragon recently and now wants to recruit a group to go slay it"
        elif n < 23:
            end = "who has awoken from a great slumber and now stalks the earth"
        elif n < 24:
            end = "with a love for turtles"
        elif n < 25:
            end = "who is actually from the real planet Earth from modern times, inserted into this story to make the author feel that there is a time and place where they can actually be respected and loved without fear of abandonment"
        
        name = start + middle + end
        if not name_taken(name):
            names_used.append(name)
            m -= 1

    #names_used.pop(0)
    return names_used