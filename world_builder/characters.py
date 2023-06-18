
import random

#--------------------------------------
# Randomly assign gender
#  assuming binary
#--------------------------------------
def gender():
    gender = ['Male', 'Female']
    my_gender = random.choice(gender)

    return my_gender

#--------------------------------------
# Randomly assign name from a file
#  based on gender, assuming binary
#--------------------------------------
def genName(my_gender):
    if my_gender == 'Male':
        names = open('story_options/male_names.txt').readlines()
    else:
        names = open('story_options/female_names.txt').readlines()
    my_name = str.rstrip(random.choice(names))

    return my_name

def genBasicCharacters(cn,an,vn,v_n):

    if cn == 'F':
        hero = genName(gender())
        an = genName(gender())
        antag1 = genName(gender())
        antag2 = genName(gender())
        vn = genName(gender())
    else:
        antag1 = v_n.pop()
        antag2 = v_n.pop()

    if cn == 'F':
        print('The hero of this story is ' + hero + ', ', end = "")
    elif len(cn) == 1:
        print('The hero of this story is ' + cn.pop() + ', ', end = "")
    else:
        print('The heroes of this story are ', end = "")
        i = len(cn)
        for x in range(i):
            if len(cn) == 1:
                print('and ' + cn.pop() + ', ', end = "")
            else:
                print(cn.pop() + ', ', end = "")
    
    print('who joins forces with ' + an + ' in an attempt to stop the villainous ' + vn \
          + ' along with their henchmen ' + antag1 + ' and ' + antag2 + '.')
    

def genFullCharacters(cRequest, numChars, charLevel, mvLevel):
    import character_assets.two_e_character_generator as char

    char_names = []

    for x in range(numChars):
        char_names.append(char.chargen(cRequest[x], 'F', charLevel, 1))

    print("The PCs are:")
    print(char_names)

    an = char.chargen('F', 'F', charLevel, 1)
    print("The PC ally/neutral is " + an)

    villain = char.chargen('F', 'F', mvLevel, 1)
    print("The master villain is " + villain)

    mv_names = []
    for x in range(2):
        mv_names.append(char.chargen('F', 'F', charLevel, 1))
    print("The minor villains are:")
    print(mv_names)
    
    return char_names, an, villain, mv_names