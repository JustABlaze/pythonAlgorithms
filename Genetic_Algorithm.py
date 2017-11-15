''''

Name: Mustafa Khalil
ID: 140201100

'''

import random


def objectiveFunc(x,y):
    first_equation = (4-(2.1*(x**2)) + ((x**4)/3))*x**2
    second_equation = (-4 + (4*(y**2)))*y**2
    return first_equation + (x*y) + second_equation


class gene():
    def __init__(self,x=[],y=[],value=0.0,fitness = 0.0):
        self.x = x
        self.y = y
        self.value = value
        self.fitness = fitness

def generateChromo(numberOfChromo):
    array = []
    for i in range(0,numberOfChromo):
        array.append(round(random.uniform(0,1)))
    return array

def convertTodecimal(a):
    number = 0
    for num in range(0,len(a)):
        if a[(len(a)-1)-num] == 1:
            number += 2**num
    return number

def presision(constrants,lenOfChromo):
    return (constrants - (-constrants))/(2**lenOfChromo-1)


def generateValues(array,xCons,yCons,lenOfChromo):

    for i in range(0,len(array)):
        x = convertTodecimal(array[i].x)
        y = convertTodecimal(array[i].y)
        x = (x * presision(xCons, lenOfChromo)) - xCons
        y = (y * presision(yCons, lenOfChromo)) - yCons

        array[i].value = round(objectiveFunc(x,y),6)


    return array


def createInitialPopulation(neededPop,lenOfChromo,xCons,yCons):
    thisArray = []
    for i in range(0,neededPop):
        thisArray.append(gene(x= generateChromo(lenOfChromo),y =generateChromo(lenOfChromo)))
    thisArray = generateValues(array=thisArray,xCons=xCons,yCons=yCons,lenOfChromo=lenOfChromo)
    thisArray = sorted(thisArray, key=lambda x: x.value)
    return thisArray


def pickParents(array):
    x1 = None
    x2 = None
    arrayOfParents = calculateFitness(array=array)

    fit = 0.0
    rand = random.uniform(0,1)
    for i in range(0,len(arrayOfParents)):
        fit += arrayOfParents[(len(arrayOfParents)-1)-i].fitness
        if rand < fit:
            x1 = arrayOfParents[(len(arrayOfParents)-1)-i]

    while x2 == None:
        rand = random.uniform(0, 1)
        fit = 0.0
        for i in range(0, len(arrayOfParents)):
            fit += arrayOfParents[(len(arrayOfParents)-1)-i].fitness
            if rand < fit and x1 != arrayOfParents[(len(arrayOfParents)-1)-i]:
                x2 = arrayOfParents[(len(arrayOfParents)-1)-i]

    return (x1,x2)


def calculateFitness(array):

    minValue = array[0].value
    sumValue = 0.0
    for i in range(0,len(array)):
        array[i].fitness = 1/(array[i].value + abs(minValue) + 1)
        sumValue += array[i].fitness

    for i in range(0,len(array)):
        array[i].fitness = (array[i].fitness/sumValue)
    return array

def crossOver(prnt1,prnt2,xCons,yCons,lenOfChromo):
    child1 = gene(x= generateChromo(lenOfChromo),y =generateChromo(lenOfChromo))
    child2 = gene(x= generateChromo(lenOfChromo),y =generateChromo(lenOfChromo))

    for i in range(0,int(lenOfChromo/2)):
        rand = round(random.uniform(0,1))
        if rand == 0:
            child1.x[i] = prnt1.x[i]
            child1.y[i] = prnt2.y[i]
            child2.x[i] = prnt2.x[i]
            child2.y[i] = prnt1.y[i]
        if rand == 1:
            child1.x[i] = prnt2.x[i]
            child1.y[i] = prnt1.y[i]
            child2.x[i] = prnt1.x[i]
            child2.y[i] = prnt2.y[i]

    children = generateValues([child1,child2],xCons=xCons,yCons=yCons,lenOfChromo=lenOfChromo)

    return (children[0],children[1])

def mutation(array,mutationValue,lenOfChromo,xCons,yCons):
    for i in range(0,len(array)):
        rand = random.uniform(0,1)
        if rand < mutationValue:
            randomMutation = round(random.uniform(0,lenOfChromo-1))
            array[i].x[randomMutation] = 0 if array[i].x[randomMutation] == 1 else 1
            array[i].y[randomMutation] = 0 if array[i].y[randomMutation] == 1 else 1

    children = generateValues([array[0], array[1]], xCons=xCons, yCons=yCons, lenOfChromo=lenOfChromo)
    return (children[0],children[1])


def pickBetterFitness():

    return None

def GA():
    mutationValue = 0.11
    lenOfChromo = 11
    Xcon = 3
    Ycon = 2
    numberOfPop = 10
    G_MAX = 100
    ps = int(numberOfPop/2)
    startingPop = createInitialPopulation(neededPop=numberOfPop,lenOfChromo=lenOfChromo,xCons=Xcon,yCons=Ycon)


    for i in range(0,G_MAX):
        childrenPop = []
        for i in range(0,ps):
            (x1,x2) = pickParents(startingPop)
            (chld1,chld2) = crossOver(x1,x2,xCons=Xcon,yCons=Ycon,lenOfChromo=lenOfChromo)
            (chld1,chld2) = mutation([chld1,chld2],mutationValue = mutationValue,lenOfChromo= lenOfChromo,xCons=Xcon,yCons=Ycon)
            childrenPop.append(chld1)
            childrenPop.append(chld2)

        childrenPop = sorted(childrenPop, key=lambda x: x.value)
        childrenPop = calculateFitness(childrenPop)

        temp = []
        for i in range(0,int(len(startingPop)/2)):
            temp.append(startingPop[i])
            temp.append(childrenPop[i])

        startingPop = temp
        startingPop = sorted(startingPop, key=lambda x: x.value)

    print(startingPop[0].value)


for i in range(0,30):
    GA()