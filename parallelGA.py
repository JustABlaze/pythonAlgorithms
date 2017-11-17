

''''

Name: Mustafa Khalil
ID:   140201100

'''

import random
import multiprocessing as mp


def objectiveFuncparallel(x,y,a,b,c,d,e):
    first_equation = (a-(b*(x**2)) + ((x**4)/c))*x**2
    second_equation = (-d + (e*(y**2)))*y**2
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


def generateValues(array,xCons,yCons,lenOfChromo,function,constArray):

    for i in range(0,len(array)):
        x = convertTodecimal(array[i].x)
        y = convertTodecimal(array[i].y)
        x = (x * presision(xCons, lenOfChromo)) - xCons
        y = (y * presision(yCons, lenOfChromo)) - yCons

        array[i].value = round(function(x=x,y=y,a=constArray[0],b=constArray[1],c=constArray[2],d=constArray[3],e=constArray[4]),4)


    return array


def createInitialPopulation(neededPop,lenOfChromo,xCons,yCons,function,constArray):
    thisArray = []
    for i in range(0,neededPop):
        thisArray.append(gene(x= generateChromo(lenOfChromo),y =generateChromo(lenOfChromo)))
    thisArray = generateValues(array=thisArray,xCons=xCons,yCons=yCons,lenOfChromo=lenOfChromo,function=function,constArray=constArray)
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

def crossOver(prnt1,prnt2,xCons,yCons,lenOfChromo,function,constArray):
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

    children = generateValues([child1,child2],xCons=xCons,yCons=yCons,lenOfChromo=lenOfChromo,function=function,constArray=constArray)

    return (children[0],children[1])

def mutation(array,mutationValue,lenOfChromo,xCons,yCons,function,constArray):
    for i in range(0,len(array)):
        rand = random.uniform(0,1)
        if rand < mutationValue:
            randomMutation = round(random.uniform(0,lenOfChromo-1))
            array[i].x[randomMutation] = 0 if array[i].x[randomMutation] == 1 else 1
            array[i].y[randomMutation] = 0 if array[i].y[randomMutation] == 1 else 1

    children = generateValues([array[0], array[1]], xCons=xCons, yCons=yCons, lenOfChromo=lenOfChromo,function=function,constArray=constArray)
    return (children[0],children[1])


def pickBetterFitness():

    return None

def GA(x,y,population,lenOfChromo,generations,function,array):
    pc = 1.0
    mutationValue = 0.11
    lenOfChromo = lenOfChromo
    Xcon = x
    Ycon = y
    numberOfPop = population
    G_MAX = generations
    ps = numberOfPop // 2
    startingPop = createInitialPopulation(neededPop=numberOfPop, lenOfChromo=lenOfChromo, xCons=Xcon, yCons=Ycon,
                                          function=function, constArray=array)
    zValue = startingPop[0]

    for i in range(0, G_MAX):
        childrenPop = []

        for i in range(0, ps):
            chld1 = gene()
            chld2 = gene()
            rand = random.uniform(0, 1)
            gotChildren = False
            (x1, x2) = pickParents(startingPop)

            if rand < pc:
                gotChildren = True
                (chld1, chld2) = crossOver(x1, x2, xCons=Xcon, yCons=Ycon, lenOfChromo=lenOfChromo, function=function,
                                           constArray=array)


            if gotChildren == True:
                (chld1, chld2) = mutation([chld1, chld2], mutationValue=mutationValue, lenOfChromo=lenOfChromo,
                                          xCons=Xcon, yCons=Ycon, function=function, constArray=array)
                childrenPop.append(chld1)
                childrenPop.append(chld2)

        childrenPop = sorted(childrenPop, key=lambda x: x.value)
        childrenPop = calculateFitness(childrenPop)
        nextGen = []
        temp = []

        for i in range(0, len(startingPop)):
            temp.append(startingPop[i])

        for i in range(0, len(childrenPop)):
            temp.append(childrenPop[i])

        temp = sorted(temp, key=lambda x: x.value)

        for i in range(0, numberOfPop):
            nextGen.append(temp[i])

        nextGen = sorted(nextGen, key=lambda x: x.value)

        startingPop = nextGen

        if startingPop[0].value < zValue.value:
            zValue = startingPop[0]

    return zValue.value










array = [[4,2.1,3,4,4],[4,2.1,3,4,4],[4,2.1,3,4,4],[4,2.1,3,4,4],[4,2.1,3,4,4],[4,2.1,3,4,4],[4,2.1,3,4,4],[4,2.1,3,4,4],[4,2.1,3,4,4],[4,2.1,3,4,4],
         [4, 2.1, 3, 4, 4], [4, 2.1, 3, 4, 4], [4, 2.1, 3, 4, 4], [4, 2.1, 3, 4, 4], [4, 2.1, 3, 4, 4],
         [4, 2.1, 3, 4, 4], [4, 2.1, 3, 4, 4], [4, 2.1, 3, 4, 4], [4, 2.1, 3, 4, 4], [4, 2.1, 3, 4, 4],
         [4, 2.1, 3, 4, 4], [4, 2.1, 3, 4, 4], [4, 2.1, 3, 4, 4], [4, 2.1, 3, 4, 4], [4, 2.1, 3, 4, 4],
         [4, 2.1, 3, 4, 4], [4, 2.1, 3, 4, 4], [4, 2.1, 3, 4, 4], [4, 2.1, 3, 4, 4], [4, 2.1, 3, 4, 4],
         [4, 2.1, 3, 4, 4], [4, 2.1, 3, 4, 4], [4, 2.1, 3, 4, 4], [4, 2.1, 3, 4, 4], [4, 2.1, 3, 4, 4],
         [4, 2.1, 3, 4, 4], [4, 2.1, 3, 4, 4], [4, 2.1, 3, 4, 4], [4, 2.1, 3, 4, 4], [4, 2.1, 3, 4, 4],
         [4, 2.1, 3, 4, 4], [4, 2.1, 3, 4, 4], [4, 2.1, 3, 4, 4], [4, 2.1, 3, 4, 4], [4, 2.1, 3, 4, 4],
         [4, 2.1, 3, 4, 4], [4, 2.1, 3, 4, 4], [4, 2.1, 3, 4, 4], [4, 2.1, 3, 4, 4], [4, 2.1, 3, 4, 4],
         [4, 2.1, 3, 4, 4], [4, 2.1, 3, 4, 4], [4, 2.1, 3, 4, 4], [4, 2.1, 3, 4, 4], [4, 2.1, 3, 4, 4],
         [4, 2.1, 3, 4, 4], [4, 2.1, 3, 4, 4], [4, 2.1, 3, 4, 4], [4, 2.1, 3, 4, 4], [4, 2.1, 3, 4, 4],
         [4, 2.1, 3, 4, 4], [4, 2.1, 3, 4, 4], [4, 2.1, 3, 4, 4], [4, 2.1, 3, 4, 4], [4, 2.1, 3, 4, 4],
         [4, 2.1, 3, 4, 4], [4, 2.1, 3, 4, 4], [4, 2.1, 3, 4, 4], [4, 2.1, 3, 4, 4], [4, 2.1, 3, 4, 4],
         [4, 2.1, 3, 4, 4], [4, 2.1, 3, 4, 4], [4, 2.1, 3, 4, 4], [4, 2.1, 3, 4, 4], [4, 2.1, 3, 4, 4],
         [4, 2.1, 3, 4, 4], [4, 2.1, 3, 4, 4], [4, 2.1, 3, 4, 4], [4, 2.1, 3, 4, 4], [4, 2.1, 3, 4, 4],
         [4, 2.1, 3, 4, 4], [4, 2.1, 3, 4, 4], [4, 2.1, 3, 4, 4], [4, 2.1, 3, 4, 4], [4, 2.1, 3, 4, 4],
         [4, 2.1, 3, 4, 4], [4, 2.1, 3, 4, 4], [4, 2.1, 3, 4, 4], [4, 2.1, 3, 4, 4], [4, 2.1, 3, 4, 4],
         [4,2.1,3,4,4],[4,2.1,3,4,4],[4,2.1,3,4,4],[4,2.1,3,4,4],[4,2.1,3,4,4],[4,2.1,3,4,4],[4,2.1,3,4,4],[4,2.1,3,4,4]
    ,[4,2.1,3,4,4],[4,2.1,3,4,4],[0,1,2,3,4],[0,1,2,3,4],[0,1,2,3,4],[0,1,2,3,4],[0,1,2,3,4],[0,1,2,3,4],[0,1,2,3,4],[0,1,2,3,4],[0,1,2,3,4],
         [0, 1, 2, 3, 4],[0,1,2,3,4],[0,1,2,3,4],[0,1,2,3,4],[0,1,2,3,4],[0,1,2,3,4],[0,1,2,3,4],[0,1,2,3,4],[0,1,2,3,4],
         [0, 1, 2, 3, 4],[0,1,2,3,4],[0,1,2,3,4],[0,1,2,3,4],[0,1,2,3,4],[0,1,2,3,4],[0,1,2,3,4],[0,1,2,3,4],[0,1,2,3,4],
         [0, 1, 2, 3, 4],[0,1,2,3,4],[0,1,2,3,4],[0,1,2,3,4],[0,1,2,3,4],[0,1,2,3,4],[0,1,2,3,4],[0,1,2,3,4],[0,1,2,3,4],
         [0, 1, 2, 3, 4],[0,1,2,3,4],[0,1,2,3,4],[0,1,2,3,4],[0,1,2,3,4],[0,1,2,3,4],[0,1,2,3,4],[0,1,2,3,4],[0,1,2,3,4],
         [0, 1, 2, 3, 4],[0,1,2,3,4],[0,1,2,3,4],[0,1,2,3,4],[0,1,2,3,4],[0,1,2,3,4],[0,1,2,3,4],[0,1,2,3,4],[0,1,2,3,4],
         [0, 1, 2, 3, 4],[0,1,2,3,4],[0,1,2,3,4],[0,1,2,3,4],[0,1,2,3,4],[0,1,2,3,4],[0,1,2,3,4],[0,1,2,3,4],[0,1,2,3,4],
         [0, 1, 2, 3, 4],[0,1,2,3,4],[0,1,2,3,4],[0,1,2,3,4],[0,1,2,3,4],[0,1,2,3,4],[0,1,2,3,4],[0,1,2,3,4],[0,1,2,3,4],
         [0, 1, 2, 3, 4],[0,1,2,3,4],[0,1,2,3,4],[0,1,2,3,4],[0,1,2,3,4],[0,1,2,3,4],[0,1,2,3,4],[0,1,2,3,4],[0,1,2,3,4],
         [0, 1, 2, 3, 4],[0,1,2,3,4],[0,1,2,3,4],[0,1,2,3,4],[0,1,2,3,4],[0,1,2,3,4],[0,1,2,3,4],[0,1,2,3,4],[0,1,2,3,4],
         [0, 1, 2, 3, 4],[0,1,2,3,4],[0,1,2,3,4],[0,1,2,3,4],[0,1,2,3,4],[0,1,2,3,4],[0,1,2,3,4],[0,1,2,3,4],[0,1,2,3,4]]

count = 0
from datetime import datetime
start=datetime.now()
print(mp.cpu_count())


for i in array:
    print(GA(x=3,y=2,population =50,lenOfChromo=11,generations=500, function=objectiveFuncparallel,array=i))


print(datetime.now() - start)

start=datetime.now()

def func(x):
    print(x)
    print(GA(x=3, y=2, population=50, lenOfChromo=11, generations=500, function=objectiveFuncparallel, array=i))

p = mp.Pool(processes=8)
p.map(func,array)

print(datetime.now() - start)
