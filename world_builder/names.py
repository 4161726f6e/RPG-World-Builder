import numpy as np

names_used = [""]

def name_taken(place_name):
        # See if a generated name has already been used.
        taken = False
        for i in names_used:
            if i == place_name:
                taken = True
        return taken

def get_religion(n):
    name = ""
    while n > 0:
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
            start = "Dread"
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
            middle = "Metat"
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
            n -= 1

    names_used.pop(0)
    return names_used

