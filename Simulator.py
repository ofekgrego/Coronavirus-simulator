import random
from tkinter import *
import tkinter
import numpy

numOfPeopleGlob = 100
numOfSicks = 5
timeToSpot = 5
timeToHeal = 14
possibleStore = 20
chanceToSickStore = 40
deathChance = 0.5

window = Tk()
window.title("Corona Simulator")
window.resizable(False,False) #disable resize

canvas_width = 1000  #x
canvas_height = 1000 #y
fCan = Frame(window, width=canvas_width, height=canvas_width+260)
fCan.pack(side=tkinter.LEFT)
w = Canvas(fCan, width=canvas_width,height=canvas_height, background="gray")
w.pack()
w.create_rectangle(450, 450, 550, 550)

sizeOfPeople = 10

fInfo = Frame(window, width=200, height=canvas_height)
fInfo.pack()

arrayOfObjects = [None] * numOfPeopleGlob
arrayOfPeople = [None] * numOfPeopleGlob
arrayOfChance = [None] * numOfPeopleGlob
arrayOfNowInStore = [None] * numOfPeopleGlob
arrayOfSick = [1] * numOfSicks + [0] * (numOfPeopleGlob-numOfSicks)
arrayOfDeath = [False] * numOfPeopleGlob

def makePeople(numOfPeople):
        global arrayOfPeople, arrayOfObjects,isSickOne
        for j in range(numOfPeople):
            xAxe = 500
            yAxe = 500
            while (450-sizeOfPeople)<xAxe<550 and (450-sizeOfPeople)<yAxe<550:
                xAxe = random.randint(10,canvas_width-25)
                yAxe = random.randint(10,canvas_height-25)
            if arrayOfSick[j] > 0:
                arrayOfObjects[j] = w.create_rectangle(xAxe,yAxe,xAxe+sizeOfPeople,yAxe+sizeOfPeople, fill="#00FF00")
            else:
                arrayOfObjects[j] = w.create_rectangle(xAxe,yAxe,xAxe+sizeOfPeople,yAxe+sizeOfPeople, fill="#0000FF")
            arrayOfPeople[j] = [xAxe,yAxe]

def refrashScreen():
    global arrayOfObjects,arrayOfNowInStore
    for i in range(len(arrayOfPeople)):
        w.delete(arrayOfObjects[i])
        if arrayOfDeath[i] == False:
            if arrayOfChance[i] == True:
                if arrayOfSick[i] == timeToHeal+1:
                    arrayOfObjects[i] = w.create_rectangle(500-(sizeOfPeople/2),500-(sizeOfPeople/2),500+(sizeOfPeople/2),500+(sizeOfPeople/2), fill="#0000FF")
                elif arrayOfSick[i] > timeToSpot:
                    arrayOfObjects[i] = w.create_rectangle(500-(sizeOfPeople/2),500-(sizeOfPeople/2),500+(sizeOfPeople/2),500+(sizeOfPeople/2), fill="#00FF00")
                elif arrayOfSick[i] > 0:
                    arrayOfObjects[i] = w.create_rectangle(500-(sizeOfPeople/2),500-(sizeOfPeople/2),500+(sizeOfPeople/2),500+(sizeOfPeople/2), fill="#FF0000")
                else:
                    arrayOfObjects[i] = w.create_rectangle(500-(sizeOfPeople/2),500-(sizeOfPeople/2),500+(sizeOfPeople/2),500+(sizeOfPeople/2), fill="#0000FF")
                arrayOfNowInStore[i] = True
            else:
                arrayOfNowInStore[i] = False

            if arrayOfNowInStore[i] == False:
                if arrayOfSick[i] == timeToHeal+1:
                    arrayOfObjects[i] = w.create_rectangle(arrayOfPeople[i][0],arrayOfPeople[i][1],arrayOfPeople[i][0]+sizeOfPeople, arrayOfPeople[i][1]+sizeOfPeople, fill="#0000FF")
                elif arrayOfSick[i] > timeToSpot:
                    arrayOfObjects[i] = w.create_rectangle(arrayOfPeople[i][0],arrayOfPeople[i][1],arrayOfPeople[i][0]+sizeOfPeople, arrayOfPeople[i][1]+sizeOfPeople, fill="#FF0000")
                elif arrayOfSick[i] > 0:
                    arrayOfObjects[i] = w.create_rectangle(arrayOfPeople[i][0],arrayOfPeople[i][1],arrayOfPeople[i][0]+sizeOfPeople, arrayOfPeople[i][1]+sizeOfPeople, fill="#00FF00")
                else:
                    arrayOfObjects[i] = w.create_rectangle(arrayOfPeople[i][0],arrayOfPeople[i][1],arrayOfPeople[i][0]+sizeOfPeople, arrayOfPeople[i][1]+sizeOfPeople, fill="#0000FF")

def refrashData():
    global arrayOfChance
    sickNumber = 0
    noSpot = 0
    sickInside = False
    arrayOfChance = [None] * numOfPeopleGlob
    for i in range(len(arrayOfPeople)): #enterstore
        if arrayOfNowInStore[i] == True:
            arrayOfNowInStore[i] = False
        if arrayOfSick[i] <= timeToSpot:
            ChanceNumber = random.randint(1,100)
            Chance = False
            if ChanceNumber <= possibleStore:
                Chance = True
                if arrayOfSick[i] > 0:
                    sickInside = True
            else:
                Chance = False
        else:
            Chance = False
        arrayOfChance[i] = Chance

    refrashScreen()
    for i in range(len(arrayOfSick)): #check of been sick a while
        if arrayOfDeath[i] == False:
            if arrayOfSick[i] > 0:
                arrayOfSick[i] += 1
            if arrayOfSick[i] == timeToHeal+1:
                chanceOfDeath = random.randint(1,1000)
                if chanceOfDeath <= (deathChance*10):
                    arrayOfDeath[i] = True
                    print(str(i) + " died")
                else:
                    arrayOfSick[i] = 0

    if sickInside: #adding sick people
        for i in range(len(arrayOfNowInStore)):
            if arrayOfNowInStore[i] == True and arrayOfSick[i] == 0:
                Chance = random.randint(1, 100)
                if chanceToSickStore >= Chance:
                    arrayOfSick[i] = 1

def nextPressed():
    refrashData()

def runPressed():
    global arrayOfObjects,arrayOfPeople,arrayOfChance,arrayOfNowInStore,arrayOfSick,arrayOfDeath
    w.delete("all")
    w.create_rectangle(450, 450, 550, 550)

    arrayOfObjects = [None] * numOfPeopleGlob
    arrayOfPeople = [None] * numOfPeopleGlob
    arrayOfBeenSick = [False] * numOfPeopleGlob
    arrayOfChance = [None] * numOfPeopleGlob
    arrayOfNowInStore = [None] * numOfPeopleGlob
    arrayOfDeath = [False] * numOfPeopleGlob
    arrayOfSick = [1] * numOfSicks + [0] * (numOfPeopleGlob-numOfSicks)

    makePeople(numOfPeopleGlob)

nextButton = Button(fInfo,text="Next!", command=nextPressed).pack(side=tkinter.TOP)
runButton = Button(fInfo,text="Run!", command=runPressed).pack()

window.mainloop()
