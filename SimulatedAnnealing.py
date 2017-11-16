import random
import math
import matplotlib.pyplot as plt

def objectiveFunc(x,y):
    first_equation = (4-(2.1*(x**2)) + ((x**4)/3))*x**2
    second_equation = (-4 + (4*(y**2)))*y**2
    return first_equation + (x*y) + second_equation


def moving_Func(numberX,highX,lowX,numberY,highY,lowY):
    randomNumberX = round(numberX + random.uniform(lowX,highX),6)
    randomNumberY = round(numberY + random.uniform(lowY,highY),6)
    while True:
        if randomNumberX <= highX and randomNumberX >= lowX:
            if randomNumberY <= highY and randomNumberY >= lowY:
                break
            randomNumberY = round(numberY + random.uniform(lowY, highY), 6)
        else:
            randomNumberX = round(numberX + random.uniform(lowX,highX),6)

    return (randomNumberX,randomNumberY)



def SA(xInput,yInput,startTemp,endTemp,incrt):
    startingTemp = startTemp
    endingTemp = endTemp
    incrementer = incrt
    x =  random.uniform(-xInput,xInput)
    y = random.uniform(-yInput,yInput)

    prevX = x
    prevY = y
    finalY = 0
    finalX = 0
    finalResult = 0

    while endingTemp < startingTemp:
        for j in range(0,startingTemp,1):
            moving = moving_Func(x, xInput, -xInput, y, yInput, -yInput)
            x = moving[0]
            y = moving[1]

            if objectiveFunc(x, y) <= objectiveFunc(prevX,prevY):

                prevX = x
                prevY = y
            else:

                if random.uniform(0,1) <= math.exp(-((objectiveFunc(x,y)-objectiveFunc(prevX,prevY))/startingTemp)):

                    prevX = x
                    prevY = y

            if objectiveFunc(x,y) <= finalResult:

                finalX = x
                finalY = y
                finalResult = objectiveFunc(x,y)

        startingTemp = int(float(startingTemp) * incrementer)

    return (round(finalResult,4),round(finalX,5),round(finalY,5),startTemp,endTemp,incrt)


print(SA(3,2,450,23,0.98))