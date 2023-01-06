import time
import logging
import csv
from datetime import date


with open('test.log', 'r') as logfile, open('test.csv', 'w') as csvfile:
    reader = csv.reader(logfile, delimiter='|')
    writer = csv.writer(csvfile, delimiter='|',)
    writer.writerow(['column1', 'column2', 'column3', 'column4'])
    writer.writerows(reader)        

today = date.today()
logging.basicConfig(
    filename='test.log', 
    filemode='w',
    level=logging.DEBUG, 
    format="{asctime} {levelname:<8} {message}", 
    style ='{'
)

logging.debug('This is a Debug msg')
logging.info('This is a Info msg')
logging.warning('This is a Warning msg')
logging.error('This is an Error msg')



print()
print()
print()
print("                     #############################")
print("                     #                           #")
print("                     #      Adventure Game       #")
print("                     #                           #")
print("                     #############################")
print()
print("                          Lost on an Island       ")
print()


def welcome():    
    start_game = input("Would you like to start the game? (Y/N): ")
    if start_game == "n" or start_game == "N":
        logging.info('Not playing the game')
        print("Maybe Later")
        quit()
    elif start_game == 'y' or start_game == 'Y':
        intro_scene()
    else:
        print("Please enter a valid option.")
        welcome()   



def intro_scene():
    first_name = input("What is your name adventurer: ")
    print(f"""
                        ☠️☠️☠️ {first_name}, you are lost on a deserted island! ☠️☠️☠️
    """)
    time.sleep(2)

    print("""
                Your airplane had an engine blow out and you crash landed on an island. 
                You wake up washed ashore and realize you are alone, the only survivor, 
                with only the clothes on your back and a desire to survive.
    """) 
    time.sleep(1)
    scene_start()
 
    
       
def scene_start():
    directions = ["1","2"]
    user_input = input("Type 1 to walk around, type 2 to stay put. Choose wisely!: ")
    while user_input not in directions:
        print("Options: 1 or 2")
        user_input = input()
    if user_input == "1":
        logging.info('Entering game')
        choice_1()  
    elif user_input == "2":
        logging.info('leaving game')
        choice_2()
    else: 
        print("Please enter a valid option.")  



def choice_1():
    user_input = input("What direction would you like to go? (North, South, East, or West): ").lower().strip()
    if user_input == "north":
        cave()
    elif user_input == "south":
        time.sleep(1)
        logging.info('Stuck on the island with Wilson')
        print("""
            You have stumbled upon a beautiful beach stretching for hundreds of yards. 
            As you walk along this beach you stumble upon someone else who survived the crash.
            ....WWWWWIIIILLLLSSSSOOOONNNNNN!!!!
            Just like Tom Hanks in Castaway, Wilson will keep you company on this unforgiving island until you get help.
        """)
        quit()
    elif user_input == "east":
        plane()
    elif user_input == "west":
        forest()
    else:
        print("Please enter a valid option.")
        choice_1()  


def choice_2():
    logging.info('Kicked off the island')
    print ("We warned you brave adventurer, no cowards allowed on this island!")
    quit()
   


def cave():
    print("""
        It's a cave, looks very dark and scary, but theres no turning back now!!
    """)
    user_input = input("You have the option to go left or right in the cave: ").lower().strip()
    if user_input == "left":
        logging.info('Found treasure chest')
        print("""
            There is a treasure chest full of gold, jewels, an old map.
        """)
        user_input = input( """
            Would you like to follow the ancient map of the island or stay in the cave and guard your new found treasure? 
            Choose 1 to follow the map or 2 stay with the gold: """)
        directions = ["1","2"]    
        while user_input not in directions: 
            print("Options: 1 or 2")
            user_input = input()   
        if user_input == "1":
            logging.info('Found useless boat, continue exploring')
            print("""
                Looks like the map led to an old dinghy on the otherside of the island that captain Jack Sparrow used way back when, but you discover the little boat is useless due to the rotting wood. You decide to continue exploring.
            """)
            time.sleep(2)
            plane()
        elif user_input == "2":
            logging.info('Die in cave with treasure')
            print("You are greedy and will rot in the cave forever guarding your treasure")
            print("GAME OVER")
            quit()
    elif user_input == "right":
        logging.info('Eaten by a dragon')
        print("""
            Do you hear something?!!!!
            UH OH you have ran into a couped up dragon that has been waiting for an unlucky adventurer to come stubble upon him for a meal.
            OM NOM NOM NOM Yummy - says the Dragon
        """)
        print("GAME OVER")
    else:
        print("Please enter a valid option.")
        cave()          



def plane():
    print("""
            While you are exploring you stumble upon the first half of the downed plane. 
            Do you wish to explore the wreck or explore more of the island. 
            """)    
    user_input = input("Choose left to explore the wreck or right to turn back: ").lower().strip()        
    if user_input == "left":
        logging.info('Player finds tools and survives island')
        print("""
            Good choice adventurer you found tools to survive the island. 
            A cargo ship was passing by and you used the flare gun you found to signal him down! 
            You have survived!!!
        """)
        exit()
    elif user_input == "right":
        logging.info('Player misses cargo ship')
        print("""
            A cargo ship was passing by and you didn't make it it time to flag it down. 
            Now you're stuck on the island! 
            GAME OVER!
            """) 
        quit()   
    else:
        print("Please enter a valid option.")
        plane()        



def forest():
    actions = ["left", "Left","right", "Right"]
    time.sleep(2)
    print("""
        You have entered a dense forest filled with formidable creatures.
    """)
    user_input = input("You have the option to go left or right: ")
    while user_input not in actions:
        print("Options: left or right")
        user_input = input()
    if user_input == "left":
        logging.info('player finds ax')
        print("""
            To the left you found an ax on the floor. 
            You use this ax to cut down the foliage in your way, you see a pirate ship in the distance. 
            Do you want to take your chances with the infamous Captain Jack Sparrow and his mighty crew or take you chances with the forest.
            """) 
    elif user_input == "right":
        logging.info('Taken by wild monkeys')
        print("""
            There is a tribe of wild monkeys that have taken you hostage.
            Game Over
        """)   
        quit()     
    actions = ["1","2"]        
    print("Choose 1 for Jack Sparrow or 2 for the forest")
    while user_input not in actions:
        print("Options: 1 or 2")
        user_input = input()
    if user_input == "1":
        logging.info('Saved by Jack Sparrow')
        print("""
            Captain Jack Sparrow considers you a worthy adventurer and allows you passage onto his ship.
            You have been saved!
        """)
        quit()
    elif user_input == "2":
        logging.info('Killed by a jaguar')
        print("""
        In the middle of the night you were attacked by a jaguar and didn't make it through the night.
        GAME OVER
        """)
        quit()  
    else:
        print("Please enter a valid option.")
    quit()    
welcome()

