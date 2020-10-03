import pygame
import sys
import emoji
import time
from datetime import datetime
from termcolor import colored, cprint


print()
cprint('Hello! I am Chotu the bot.\u270b', 'red', 'on_cyan', attrs=['bold'])
print()

cprint("I will help you with the following:\n",'green', attrs=['bold'])

cprint("1) Stay hydrated\n2) Exercise\n3) Checking Twitter\n", 'magenta')

cprint("New features", 'red', 'on_yellow', attrs=['bold'], end='')
print(" will be introduced with regular updates! Stay connected \u2764\n")

print("For what purpose do you want me to run? Enter yes or no respectively.\n")

cprint("Water :",'blue',attrs=['bold'],end=" ")
water = input().lower()

cprint("Exercise :",'red',attrs=['bold'],end=" ")
exercise = input().lower()

cprint("Twitter :",'green',attrs=['bold'],end=" ")
twitter = input().lower()

print()

if water == 'yes':
    print()
    cprint("Hello, Mien hoon jal devta! I will help you drink 3.5 liters of water in 12 hours!", 'blue', attrs=['bold'])
    cprint("->> You will have to drink ", 'blue', attrs=['bold'],end="")
    print("500 ml",end="")
    cprint(" of water every time I remind you!", 'blue', attrs=['bold'])
    print()
    water = 'ok'

if exercise == 'yes':
    print()
    cprint("Hello, Mien hoon bal devta! I will help you exercise every", 'red', attrs=['bold'],end=" ")
    print("4 hours! ",end="")
    cprint("two times a day.", 'red', attrs=['bold'])
    print()
    exercise = 'ok'

if twitter == 'yes':
    print()
    cprint("Hello, Mien hoon social minister! I will remind you to check your twitter every", 'green', attrs=['bold'],end=" ")
    print("2 hours!")
    print()
    twitter = 'ok'

water_main = time.time()
time.sleep(300)

exercise_main = time.time()
time.sleep(300)

twitter_main = time.time()
time.sleep(300)


water_count = 0
exercise_count = 0
twitter_count = 0

while True:

# Water 2 hours - 7200 seconds 7 times
# Exercise 4 hours - 14400 seconds 2 times
# Twitter 2 hours - 7200 seconds 5 times

    water_a = time.time()
    if (water_a - water_main) >= 296 and (water_a - water_main) <= 300 and water == 'ok':
        water_main = water_a
        water_count +=1
        if water_count == 7:
            water = 'not ok'
        pygame.mixer.init() 
        pygame.mixer.music.load("water.mp3") 
        pygame.mixer.music.set_volume(0.7) 
        pygame.mixer.music.play()
        cprint("Enter done after you drink water : ", 'blue', attrs=['bold'], end="")
        while True:
            wstop = input().lower()
            if wstop == 'done':
                pygame.mixer.music.stop()
                time.sleep(5)
                break
            else:
                cprint('wrong input!', 'red')
    
    exercise_a = time.time()
    if (exercise_a - exercise_main) >= 596 and (exercise_a - exercise_main) <= 600 and exercise == 'ok':
        exercise_main = exercise_a
        exercise_count += 1
        if exercise_count == 2:
            exercise = 'not ok'
        pygame.mixer.init() 
        pygame.mixer.music.load("exercise.mp3") 
        pygame.mixer.music.set_volume(0.7) 
        pygame.mixer.music.play()
        cprint("Enter done to stop : ", 'red', attrs=['bold'], end="")
        while True:
            estop = input().lower()
            if estop == 'done':
                pygame.mixer.music.stop()
                time.sleep(5)
                break
            else:
                cprint('wrong input!', 'red')

    twitter_a = time.time()
    if (twitter_a - twitter_main) >= 296 and (twitter_a - twitter_main) <= 300 and twitter == 'ok':
        twitter_main = twitter_a
        twitter_count += 1
        if twitter_count == 5:
            twitter = 'not ok'
        pygame.mixer.init() 
        pygame.mixer.music.load("twitter.mp3") 
        pygame.mixer.music.set_volume(0.7) 
        pygame.mixer.music.play()
        cprint("Enter done to stop : ", 'green', attrs=['bold'], end="")
        while True:
            tstop = input().lower()
            if tstop == 'done':
                pygame.mixer.music.stop()
                time.sleep(5)
                break
            else:
                cprint('wrong input!', 'red')


    if twitter == 'not ok' and exercise == 'not ok' and water == 'not ok':
        print()
        cprint('G','red',attrs=['bold'],end="")
        cprint('O','blue',attrs=['bold'],end="")
        cprint('A','green',attrs=['bold'],end="")
        cprint('L','magenta',attrs=['bold'],end=" ")

        (print(emoji.emojize("COMPLETED :party_popper:")))
        break

        
print()
print('Thanks for using me! enter any number to exit.')
exitt = input()



