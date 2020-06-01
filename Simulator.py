import random
from tkinter import *
import tkinter
import numpy

numOfPeopleGlob = 1000
numOfSicks = 5
possibleStore = 20
chanceToSickStore = 40
chanceToSickTwice = 20
timeToSpot = 2
timeToHeal = 14
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
arrayOfBeenSick = [False] * numOfPeopleGlob
arrayOfThird = [False] * numOfPeopleGlob

inputLabel = [Label(text="\n\nNumber Of People:"),Label(text="Sick People At Start:"),Label(text="Chance To Go To Store(%):")
,Label(text="Chance To Get Sick In Store(%):"),Label(text="Chance To Get Sick Twice(%):"),Label(text="Time To Spot Sickness:")
,Label(text="Time To Heal:"),Label(text="Chance To Die(%):"),Label(text="Chance To Get Sick Third(T/F):")]
inputEntry = [Entry(width=5),Entry(width=5),Entry(width=5),Entry(width=5),Entry(width=5),Entry(width=5),Entry(width=5),Entry(width=5),Entry(width=5),Entry(width=5)]

for i in range(len(inputLabel)):
    inputLabel[i].pack(side=tkinter.TOP)
    inputEntry[i].pack(side=tkinter.TOP)

inputEntry[0].insert("0",numOfPeopleGlob)
inputEntry[1].insert("0",numOfSicks)
inputEntry[2].insert("0",possibleStore)
inputEntry[3].insert("0",chanceToSickStore)
inputEntry[4].insert("0", chanceToSickTwice)
inputEntry[5].insert("0",timeToSpot)
inputEntry[6].insert("0",timeToHeal)
inputEntry[7].insert("0",deathChance)
inputEntry[8].insert("0", "F")

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
    sickInside = False
    arrayOfChance = [None] * numOfPeopleGlob
    for i in range(len(arrayOfPeople)):
        if arrayOfDeath[i] == False:
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
    for i in range(len(arrayOfSick)):
        if arrayOfDeath[i] == False:
            if arrayOfSick[i] > 0:
                arrayOfSick[i] += 1
            if arrayOfSick[i] == timeToHeal+1:
                chanceOfDeath = random.randint(1,1000)
                if chanceOfDeath <= (deathChance*10):
                    arrayOfDeath[i] = True
                else:
                    arrayOfSick[i] = 0

    if sickInside == True:
        for j in range(len(arrayOfNowInStore)):
            if ThirdChance == True:
                if arrayOfNowInStore[j] == True and arrayOfSick[j] == 0:
                    Chance = random.randint(1, 100)
                    if arrayOfBeenSick[j] == False:
                        if  chanceToSickStore >= Chance:
                            arrayOfSick[j] = 1
                            arrayOfBeenSick[j] = True
                    else:
                        if  chanceToSickTwice >= Chance:
                            arrayOfSick[j] = 1
                            arrayOfThird[j] = True
            elif arrayOfThird[j] == False:
                if arrayOfNowInStore[j] == True and arrayOfSick[j] == 0:
                    Chance = random.randint(1, 100)
                    if arrayOfBeenSick[j] == False:
                        if  chanceToSickStore >= Chance:
                            arrayOfSick[j] = 1
                            arrayOfBeenSick[j] = True
                    else:
                        if  chanceToSickTwice >= Chance:
                            arrayOfSick[j] = 1
                            arrayOfThird[j] = True


def nextPressed():
    refrashData()

def runPressed():
    global arrayOfObjects,arrayOfPeople,arrayOfChance,arrayOfNowInStore,arrayOfSick,arrayOfDeath
    global numOfPeopleGlob,numOfSicks,possibleStore,chanceToSickStore
    global timeToHeal,timeToSpot,ThirdChance,chanceToSickTwice, arrayOfThird,arrayOfBeenSick

    w.delete("all")
    w.create_rectangle(450, 450, 550, 550)

    numOfPeopleGlob = int(inputEntry[0].get())
    numOfSicks = int(inputEntry[1].get())
    possibleStore = int(inputEntry[2].get())
    chanceToSickStore = int(inputEntry[3].get())
    chanceToSickTwice = int(inputEntry[4].get())
    timeToSpot = int(inputEntry[5].get())
    timeToHeal = int(inputEntry[6].get())
    deathChance = float(inputEntry[7].get())
    if inputEntry[8].get().upper() == "T":
        ThirdChance = True
    elif inputEntry[8].get().upper() == "F":
        ThirdChance = False

    arrayOfObjects = [None] * numOfPeopleGlob
    arrayOfPeople = [None] * numOfPeopleGlob
    arrayOfChance = [None] * numOfPeopleGlob
    arrayOfNowInStore = [None] * numOfPeopleGlob
    arrayOfSick = [1] * numOfSicks + [0] * (numOfPeopleGlob-numOfSicks)
    arrayOfDeath = [False] * numOfPeopleGlob
    arrayOfBeenSick = [False] * numOfPeopleGlob
    arrayOfThird = [False] * numOfPeopleGlob

    makePeople(numOfPeopleGlob)

nextButton = Button(fInfo,text="Next!", command=nextPressed).pack(side=tkinter.TOP)
runButton = Button(fInfo,text="Run!", command=runPressed).pack()

window.mainloop()
