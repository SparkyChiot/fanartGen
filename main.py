from random import *


modifiers = {
    "title": "AU",
    "variations": "we have these"
}

fandoms = [
    {
        "title": "Le Petit Prince",
        "characters": ["le Petit Prince", "rose", "fox", "king", "vain man", "drunkard", "businessman", "lamplighter"]
    },
    {
        "title": "My Chemical Romance",
        "characters": ["Gerard Way", "Frank Iero", "Ray Toro", "Mikey Way", "Demolition Woman", "Demolition Man", "The Patient", "Mother War", "Pepe", "The Clerk", "The Gentleman", "His Grand Immortal Dictator", "Marianne", "Sylvia", "Veronika", "Illi McMillin"]    
    },
    {
        "title": "Danger Days",
        "characters": ["Party Poison", "Fun Ghoul", "Jet Star", "Kobra Kid", "Dr. Death Defying", "Show Pony", "The Girl", "Cherri Cola", "Blue", "Red", "Korse", "Phoenix Witch", "Vaya", "Vamos", "Val Velocity", "DJ Hot Chimp"]
    },
    {
        "title": "Green Day",
        "characters": ["Billie Joe Armstrong", "Mike Dirnt", "Tre Cool", "St. Jimmy", "Jesus of Suburbia", "Whatsername"]
    },
    {
        "title": "The Simon Snow Trilogy",
        "characters": ["Simon Snow", "Baz Pitch", "Penelope Bunce", "Agatha Wellbelove", "Niamh Brody", "Shepard", "Fiona Pitch", "Nicodemus Petty", "Ebeneza Petty", "The Mage", "Lucy Salisbury"]
    },
    {
        "title": "Youtube",
        "characters": ["Therm", "The Click", "Kwite"]
    },
    {
        "title": "Jacksepticeye",
        "characters": ["Jacksepticeye", "Antisepticeye", "Chase Brody", "Dr. Schneeplestein", "Jackaboy Man", "Jameson Jackson", "Marvin the Magnificent", "Robbie the Zombie", "Septiceye Sam"]
    },
    {
        "title": "Monster High",
        "characters": ["Abbey Bominable", "Clawdeen Wolf", "Cleo de Nile", "Deuce Gorgon", "Draculaura", "Frankie Stein", "Ghoulia Yelps", "Lagoona Blue", "Amanita Nightshade", "Batsy Claro", "Catty Noir", "Elissabat", "Gigi Grant", "Honey Swamp", "Isi Dawndancer", "Kiyomi Haunterly", "Lorna McNessie", "Jane Boolittle", "Mirasol Coxi", "Operetta", "Posea Reef", "Cawd Wolf", "Finnegan Wake", "Garrot DuRoque", "Gillington Webber", "Heath Burns", "Invisi Billy", "Jackson Jekyll", "Manny Taur", "Neighthon Rot", "Porter Geiss", "Romulus"]
    }
]


def generateFanartPrompt():
    fandom = input("enter a fandom, leave blank for random prompt: ")
    print("Generating fanart prompt...")
    if fandom == "":
        fandom = choice(fandoms)
    medium = choice(mediums)
    composition = choice(compositions)
    modifier = choice(modifiers)




def main():
    while True:
        print("Welcome to the Idea Generator Hub!")
        print("What would you like to do?")
        print("1) Generate a fanart prompt")
        print("2) Generate an OC art prompt")
        print("3) Generate a life drawing prompt")
        print("4) Access the OC generators")
        choice = input()
        if choice == "1":
            generateFanartPrompt()
        elif choice == "2":
            generateOCPrompt()
        elif choice == "3":
            generateLifeDrawingPrompt()
        elif choice == "4":
            accessOCGeneratorMenu()
        elif choice.lower() == "x":
            print("thank you for your patronage!")
            print("shutting down...")
            break
        else:
            print("invalid value, please type a number 1-4 or 'x' to quit")
