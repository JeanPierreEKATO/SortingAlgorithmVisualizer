x = 0

if x == 0:
    print("zero")
elif(x > 0):
    print("positive")
elif(x < 0):
    print("negative")


for i in range(0, 10):
    if i % 2 == 0:
        print(f"{i} is even")
    else:
        print(f"{i} is odd")

stop: bool = False

while stop == False:
    user_input = input("Enter stop to stop the while loop: ")
    if user_input.lower() == 'stop':
        stop = True

def ist_gerade(n):
    return n % 2 == 0

def begruesse_person(name = "Jean-Pierre", stadt = "Hausen"):
    print(f"Hallo {name} aus {stadt}!")

def mittelwert(liste):
    sum = 0
    for i in liste:
        sum += i
    median = sum / len(liste)
    return median


def prüfe_name(name = "Jean-Pierre", liste = ["Jean-Pierre", "Max", "Moritz"]):
    for i in liste:
        if i == name:
            return True
    return False

class Spieler:
    def __init__(self , name, level, punkte):
        self.name = name
        self.level = level
        self.punkte = punkte

    def zeige_status(self):
        print(f"Name: {self.name}, Level: {self.level}, Punkte: {self.punkte}")

    def level_up(self):
        self.level += 1
        self.punkte = 0

Player1 = Spieler("Player1", 1, 0)
Player2 = Spieler("Player2", 1, 0)

Player1.zeige_status()
Player2.zeige_status()
Player1.level_up()
Player2.level_up()

import numpy as np
#1
eindimensionales_array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

#2
np.mean(eindimensionales_array)
np.std(eindimensionales_array)

#3
zweidimensionales_array1 = np.array([[1, 2], [4, 5], [7, 8]])
zweidimensionales_array2 = np.array([[10, 11], [13, 14], [16, 17]])
# Matrix muss transponiert werden, um die Dimensionen kompatibel zu machen
zweidimensionales_array2 = zweidimensionales_array2.T

np.dot(zweidimensionales_array1, zweidimensionales_array2)

#4
zufall_array = np.random.rand(4, 4)
print(zufall_array[0])
