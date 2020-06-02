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
ThirdChance = False
graphRemove = False

sickInside = False
window = Tk()
window.title("Corona Simulator")
window.resizable(False,False) #disable resize
labelOfGraphs = ["Deaths","Sick Now"]
canvas_width = 1000  #x
canvas_height = 1000 #y
fCan = Frame(window, width=canvas_width, height=canvas_width+260)
fCan.pack(side=tkinter.LEFT)
w = Canvas(fCan, width=canvas_width,height=canvas_height, background="gray")
w.pack()
w.create_rectangle(450, 450, 550, 550)
graphCanvas = Canvas(fCan,width=canvas_width,height=260)
graphCanvas.pack()
graphCanvas.create_text(70,30, text=labelOfGraphs[0], font="helvetica 20")
graphCanvas.create_line(50,50,50,250, width=3)
graphCanvas.create_line(50,250,500,250, width=3)
graphCanvas.create_text(580,30, text=labelOfGraphs[1], font="helvetica 20")
graphCanvas.create_line(550,50,550,250, width=3)
graphCanvas.create_line(550,250,1000,250, width=3)
sizeOfPeople = 10
Days = 1
dayText = "Day 1"

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
arrayOfSickGraph = [0]
arrayOfDeathGraph = [0]

creditLabel = Label(fInfo, text="Made By Ofek Grego").pack()
spaceLabel = Label(fInfo,text="").pack()

inputLabel = [Label(text="\n\nNumber Of People:"),Label(text="Sick People At Start:"),Label(text="Chance To Go To Store(%):")
,Label(text="Chance To Get Sick In Store(%):"),Label(text="Chance To Get Sick Twice(%):"),Label(text="Time To Spot Sickness:")
,Label(text="Time To Heal:"),Label(text="Chance To Die(%):"),Label(text="Chance To Get Sick Third(T/F):"),Label(text="\n\n\n\nDays In Next:")]
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
inputEntry[9].insert("0", 1)

Labels = [Label(text="\n\n\nAlive: "),Label(text="Sicks:"),Label(text="Not Spotted:"),
            Label(text="Death")]
for i in Labels:
    i.pack()

def makeSeen():
    w.create_rectangle(0, 0, 130, 50, fill="#666")
    w.create_text(50, 25, text=dayText, font="helvetica 30")
    w.create_rectangle(0,900,170,1000, fill="#666")
    w.create_rectangle(10, 910, 25, 925 , fill="#0000FF")
    w.create_text(75, 916, text="Regular Pesron", fill="white")
    w.create_rectangle(10, 940, 25, 955 , fill="#00FF00")
    w.create_text(87, 948, text="Not Spotted Person", fill="white")
    w.create_rectangle(10, 970, 25, 985 , fill="#FF0000")
    w.create_text(75, 980, text="Spotted Person", fill="white")

def makePeople(numOfPeople):

        global arrayOfPeople, arrayOfObjects,isSickOne
        for j in range(numOfPeople):
            xAxe = 500
            yAxe = 500
            while (450-sizeOfPeople)<xAxe<550 and (450-sizeOfPeople)<yAxe<550:
                xAxe = random.randint(10,canvas_width-25)
                yAxe = random.randint(10,canvas_height-25)
            if arrayOfSick[j] > 0:
                arrayOfBeenSick[j] = True
                if graphRemove == False:
                    arrayOfObjects[j] = w.create_rectangle(xAxe,yAxe,xAxe+sizeOfPeople,yAxe+sizeOfPeople, fill="#00FF00")
            else:
                if graphRemove == False:
                    arrayOfObjects[j] = w.create_rectangle(xAxe,yAxe,xAxe+sizeOfPeople,yAxe+sizeOfPeople, fill="#0000FF")
            arrayOfPeople[j] = [xAxe,yAxe]

def refrashScreen():
    global arrayOfObjects,arrayOfNowInStore,Labels
    for i in range(len(arrayOfPeople)):
        w.delete(arrayOfObjects[i])
        if arrayOfDeath[i] == False:
            if arrayOfChance[i] == True:
                if graphRemove == False:
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
                if graphRemove == False:
                    if arrayOfSick[i] == timeToHeal+1:
                        arrayOfObjects[i] = w.create_rectangle(arrayOfPeople[i][0],arrayOfPeople[i][1],arrayOfPeople[i][0]+sizeOfPeople, arrayOfPeople[i][1]+sizeOfPeople, fill="#0000FF")
                    elif arrayOfSick[i] > timeToSpot:
                        arrayOfObjects[i] = w.create_rectangle(arrayOfPeople[i][0],arrayOfPeople[i][1],arrayOfPeople[i][0]+sizeOfPeople, arrayOfPeople[i][1]+sizeOfPeople, fill="#FF0000")
                    elif arrayOfSick[i] > 0:
                        arrayOfObjects[i] = w.create_rectangle(arrayOfPeople[i][0],arrayOfPeople[i][1],arrayOfPeople[i][0]+sizeOfPeople, arrayOfPeople[i][1]+sizeOfPeople, fill="#00FF00")
                    else:
                        arrayOfObjects[i] = w.create_rectangle(arrayOfPeople[i][0],arrayOfPeople[i][1],arrayOfPeople[i][0]+sizeOfPeople, arrayOfPeople[i][1]+sizeOfPeople, fill="#0000FF")
        else:
            w.delete(arrayOfObjects[i])
            arrayOfObjects[i] = False

def refrashGraphs():
    if Days > 1:
        graphCanvas.delete("all")
        space = float(450.0/float(Days-1))
        topNumberDeath = max(arrayOfDeathGraph)
        topNumberSick = max(arrayOfSickGraph)
        spaceToVarSick = float(200.0/float(topNumberSick+1))
        spaceToVarDeath = float(200.0/float(topNumberDeath+1))
        # print(topNumberDeath)
        # print(topNumberSick)
        # print(space)
        for i in range(Days-2):
            graphCanvas.create_line((i*space)+550,250-arrayOfSickGraph[i]*spaceToVarSick,(i+1)*space+550,250-arrayOfSickGraph[i+1]*spaceToVarSick)
            graphCanvas.create_line((i*space)+50,250-arrayOfDeathGraph[i]*spaceToVarDeath,(i+1)*space+50,250-arrayOfDeathGraph[i+1]*spaceToVarDeath)

        graphCanvas.create_text(70,30, text=labelOfGraphs[0], font="helvetica 20")
        graphCanvas.create_text(40,70,text=topNumberDeath)
        graphCanvas.create_line(50,50,50,250, width=3)
        graphCanvas.create_line(50,250,500,250, width=3)
        graphCanvas.create_text(580,30, text=labelOfGraphs[1], font="helvetica 20")
        graphCanvas.create_text(530,70,text=topNumberSick)
        graphCanvas.create_line(550,50,550,250, width=3)
        graphCanvas.create_line(550,250,1000,250, width=3)

def refrashData():
    global arrayOfChance,sickInside,dayText,Days,arrayOfDeathGraph,arrayOfSickGraph
    sickNumber = 0
    noSpot = 0
    Days += 1
    dayText = "Day " + str(Days)
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
                sickNumber += 1
            if arrayOfSick[i] == timeToHeal+1:
                chanceOfDeath = random.randint(1,1000)
                if chanceOfDeath <= (deathChance*10):
                    arrayOfDeath[i] = True
                else:
                    arrayOfSick[i] = 0
            if 0 < arrayOfSick[i] <= timeToSpot:
                noSpot += 1

    if sickInside:
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



    Labels[0].config(text= "\n\n\n" + "Alive: "+ str(numOfPeopleGlob-arrayOfDeath.count(True)))
    Labels[1].config(text= "Sicks: " + str(sickNumber))
    Labels[2].config(text= "Not Spotted: " + str(noSpot))
    Labels[3].config(text= "Death: " + str(arrayOfDeath.count(True)))
    arrayOfSickGraph.append(sickNumber)
    arrayOfDeathGraph.append(arrayOfDeath.count(True))




def nextPressed():
    timeNext = int(inputEntry[9].get())
    for i in range(timeNext):
        refrashData()
    makeSeen()
    refrashGraphs()

def runPressed():
    global numOfPeopleGlob,numOfSicks,possibleStore,timeToSpot,chanceToSickStore,timeToHeal,arrayOfChance,arrayOfNowInStore,arrayOfObjects,arrayOfPeople,arrayOfSick,deathChance,w,Days,dayText,arrayOfDeath,arrayOfBeenSick,arrayOfSickGraph,arrayOfDeathGraph,arrayOfThird,ThirdChance

    w.delete("all")
    w.create_rectangle(450, 450, 550, 550)

    Days = 1
    dayText = "Day 1"
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
    arrayOfSickGraph = []
    arrayOfDeathGraph = []

    graphCanvas.delete("all")
    graphCanvas.create_text(70,30, text=labelOfGraphs[0], font="helvetica 20")
    graphCanvas.create_line(50,50,50,250, width=3)
    graphCanvas.create_line(50,250,500,250, width=3)
    graphCanvas.create_text(580,30, text=labelOfGraphs[1], font="helvetica 20")
    graphCanvas.create_line(550,50,550,250, width=3)
    graphCanvas.create_line(550,250,1000,250, width=3)

    makePeople(numOfPeopleGlob)
    makeSeen()
    refrashGraphs()

def removePressed():
    global graphRemove
    if graphRemove:
        graphRemove = False
    else:
        graphRemove = True
    refrashScreen()

nextButton = Button(fInfo,text="Next!", command=nextPressed).pack(side=tkinter.TOP)
runButton = Button(fInfo,text="Run!", command=runPressed).pack()
removeButton = Button(fInfo,text="Remove/Add Visuals", command=removePressed).pack()
refrashGraphs()

window.mainloop()
