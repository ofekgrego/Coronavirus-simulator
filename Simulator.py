import random
from tkinter import *
import tkinter
import numpy

numOfPeopleGlob = 1000
numOfSicks = 5

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
arrayOfSick = [1] * numOfSicks + [0] * (numOfPeopleGlob-numOfSicks)
arrayOfBeenSick = [False] * numOfPeopleGlob

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
                arrayOfObjects[j] = w.create_rectangle(xAxe,yAxe,xAxe+sizeOfPeople,yAxe+sizeOfPeople, fill="#00FF00")
            else:
                arrayOfObjects[j] = w.create_rectangle(xAxe,yAxe,xAxe+sizeOfPeople,yAxe+sizeOfPeople, fill="#0000FF")
            arrayOfPeople[j] = [xAxe,yAxe]

def nextPressed():
    print("Next Day")

def runPressed():
    w.delete("all")
    w.create_rectangle(450, 450, 550, 550)

    arrayOfObjects = [None] * numOfPeopleGlob
    arrayOfPeople = [None] * numOfPeopleGlob
    arrayOfBeenSick = [False] * numOfPeopleGlob

    makePeople(numOfPeopleGlob)

nextButton = Button(fInfo,text="Next!", command=nextPressed).pack(side=tkinter.TOP)
runButton = Button(fInfo,text="Run!", command=runPressed).pack()

window.mainloop()
