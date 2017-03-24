from sys import exit

print "Welcome to Adventure Chronicles!"
user_name = raw_input("Please input your name: ")

def Atlantis():
    print "Welcome to Atlantis!"
    print "Please take all the treasure away!"
    print "You win!"
    exit(0)

def Ancient_China():
    print "Welcome to ancient China!"
    print "If you can complete the task, you will get the first piece of the map guiding to Atlantis."
    Ancient_India()



def Ancient_India():
    print "Welcome to ancient India!"
    print "The second piece of the map to Atlantis is kept in this room and the door is guarded by a leopard."
    print "You'd better feed it with something which could draw it away from the door."
    print "Remember: you must open door as soon as the leopard is moving from the door."
    print "Otherwise, the leopard will come back and chew your leg off."
    print "Please feed the leopard with:"
    leopard_moved = False

    while True:
        next = raw_input("> ")

        if next == "vegetable":
            dead("The leopard looks at you then slaps your face off.")
        elif next == "meat" and not leopard_moved:
            print "The leopard moved from the door. You can go through it now."
            leopard_moved = True
        elif next == "meat" and leopard_moved:
            dead("The leopard gets pissed off and chews your leg off.")
        elif next == "open door" and leopard_moved:
            print "Congratulations! You've successfully obtained the second piece of the map to Atlantis."
            print "Now, the Time machine is sending you to ancient Babylon."
            Ancient_Babylon()
        else:
            print "I got no idea what that means."



def Ancient_Babylon():
    print "Welcome to ancient Babylon!"
    print "You cannot get the third piece of the map unless you guess a mysterious number."

    import random
    n = random.randint(1, 99)
    guess = int(raw_input("Enter an integer from 1 to 99: "))
    while n != "guess":
        print
        if guess < n:
            print "guess is low"
            guess = int(raw_input("Enter an integer from 1 to 99: "))
        elif guess > n:
            print "guess is high"
            guess = int(raw_input("Enter an integer from 1 to 99: "))
        else:
            print "you guessed it!"
            break
        print
    print "Now, the third piece of the map is yours."
    print "Now, the Time machine is sending you to ancient Egypt."
    Ancient_Egypt()


def Ancient_Egypt():
    print "Welcome to ancient Egypt!"
    print "The ancient monster, Sphinx, is guarding the Hieroglyphic Plate, which records the path to Atlantis."
    print "If you want to obtain it, you must answer a question asked by Sphinx."
    print 'Sphinx: "Hey! %s, please answer my question."' % user_name

    while True:
        print "What's the most famous building in Egypt?"
        Answer = raw_input("> ")

        if Answer == "pyramid" or Answer == "Pyramid":
            print "Good job! You got it. The Hieroglyphic Plate is yours."
            print "So far, you have collected four pieces of the map to Atlantis."
            print "Now, the entrance to Atlantis has been open."
            Atlantis()
            break
        else:
            print "Sorry, you're wrong!"


def dead(why):
    print why
    exit(0)

def start_adventure():
    print "Brave %s, you are going to look for an ancient island called Atlantis." % user_name
    print "Atlantis, which used to be a prosperous civilization, was sunk to the bottom of the sea thousands of years ago."
    print "However, archaeologists have discovered a map in which you can find some information about Atlantis."
    print "The map is now preserved in China." 
    print "There is a Timemachine in front of you."
    print "It can send you to the following country: China, India, Babylon and Egypt."
    print "Please select the country:"
    

    while True:
        country = raw_input("> ")

        if country == "China":
            Ancient_China()
            break
        elif country == "India":
            Ancient_India()
            break
        elif country == "Babylon":
            Ancient_Babylon()
            break
        elif country == "Egypt":
            Ancient_Egypt()
            break
        else:
            print "Timemachine can not send you to that country." 
            print "Please select the country:"


start_adventure()