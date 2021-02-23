# health programmer
# 9am -5pm
# water - water song (3.5l/day) -drank log - every 40 minutes
# eyes-rotation - eyes songs - every 30mintues -eyedone -log
# physical activitu = physical song - every 45min - exdone - log

# pygame module to play audio

# importing in-built  libraries
from pygame import mixer
from time import time
import datetime


def musicloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        stopper_sms = str(input("Enter the stopper message: "))
        names = input("Enter name :- ")
        if stopper_sms == stopper:
            mixer.music.stop()
            break


def start_game():
    if __name__ == '__main__':

        init_water = time()
        init_eyes = time()
        init_exercise = time()
        water_secs = 20
        exercise_secs = 50
        eye_secs = 5
        while True:
            if time() - init_water > water_secs:
                print("Its water drinking time, enter drank to stop the music!")
                musicloop("musicbyaden-jurgance-beach.mp3", "drank")
                init_water = time()
                log_now("Drank water at : ")
            elif time() - init_exercise > exercise_secs:
                print("its time to move your bones!")
                musicloop("TouMouX-HardJump.mp3", "Done")
                init_exercise = time()
                log_now("Eyes relax  at : ")

            elif time() - init_eyes > eye_secs:
                print("Its time to blink your eyes!")
                musicloop("Cartoon-eye-blink-sound-effect-free-download.mp3", "Done")
                init_eyes = time()
                log_now("Physical activity done at : ")

            else:
                menu()
# clear log function
def clear():
    f = open("mylogs.txt", "r+")
    f.truncate()
    f.close()
    print("~~~~~~~~~~~~~~~~~~~~~~LOGS cleared successfully~~~~~~~~~~~~~~~~~~~~~~")


# lof viewer function
def view_log():
    with open("mylogs.txt", "r") as f:
        content = f.read()
        print(content)
        f.close()


# menu function
def menu():
    print("\t 1] Start game \n\t 2] View log file. \n\t 3] Clear log details. \n\t 4] Exit")
    user_input = int(input("Enter your choice : "))
    if user_input == 1:
        start_game()
        menu()
    elif user_input == 2:
        view_log()
        menu()
    elif user_input == 3:
        clear()
        menu()
    elif user_input == 4:
        exit()
    else:
        print("Choose correct input!!")
        menu()


# function for logging sms
def log_now(sms):
    with open("mylogs.txt", "a") as f:
        string = " "
        string += str("\n")
        string += str("\t") + str("--------The exercise details-----")
        string += str('\n') + str(" ")
        string += str("\t") + str(sms) + str(" ") + str(datetime.datetime.now())
        f.write(string)
    print("Information added successfully!!!")


menu()
start_game()
