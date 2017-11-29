

import random
import math
import multiprocessing as mp

def objectiveFuncparallel(x,y,a,b,c,d,e):
    first_equation = (a-(b*(x**2)) + ((x**4)/c))*x**2
    second_equation = (-d + (e*(y**2)))*y**2
    return first_equation + (x*y) + second_equation


def moving_Func(numberX,highX,lowX,numberY,highY,lowY):
    randomNumberX = round(numberX + random.uniform(-1,1),6)
    randomNumberY = round(numberY + random.uniform(-1,1),6)
    while True:
        if randomNumberX <= highX and randomNumberX >= lowX:
            if randomNumberY <= highY and randomNumberY >= lowY:
                break
            randomNumberY = round(numberY + random.uniform(-1,1), 6)
        else:
            randomNumberX = round(numberX + random.uniform(-1,1),6)

    return (randomNumberX,randomNumberY)


def SA_Algorithmpa(xInput,yInput,a,b,c,d,e):
    startingTemp = 5000
    endTemp = 23
    incrementer = 0.98
    x = random.uniform(-xInput,xInput)
    y = random.uniform(-yInput,yInput)
    prevX = x
    prevY = y
    finalY = 0
    finalX = 0
    finalResult = 0
    # while startingTemp != endTemp:
    #     for i in range(startingTemp):
    for i in range(0,450):
        for i in range(200):
            moving = moving_Func(x,xInput,-xInput,y,yInput,-yInput)
            x = moving[0]
            y = moving[1]

            if objectiveFuncparallel(x, y,a,b,c,d,e) <= objectiveFuncparallel(prevX,prevY,a,b,c,d,e):
                prevX = x
                prevY = y
            else:

                if random.uniform(0,1) <= math.exp(-((objectiveFuncparallel(x,y,a,b,c,d,e)-objectiveFuncparallel(prevX,prevY,a,b,c,d,e))/startingTemp)):

                    prevX = x
                    prevY = y

            if objectiveFuncparallel(x,y,a,b,c,d,e) <= finalResult:
                finalX = x
                finalY = y
                finalResult = objectiveFuncparallel(x,y,a,b,c,d,e)

        startingTemp = (startingTemp * incrementer)

    return (f"Final Result: {round(finalResult,4)}",f"X Coord: {round(finalX,6)}",f"Y Coord: {round(finalY,6)}")


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


for i in range(0,array.__len__()):

    print(SA_Algorithmpa(3,2,array[i][0],array[i][1],array[i][2],array[i][3],array[i][4]))


print(datetime.now() - start)


start=datetime.now()
import multiprocessing as multi
from multiprocessing import Manager

manager = Manager()

glob_data= manager.list([])

def func(x):
    print(x)
    print(SA_Algorithmpa(3,2,x[0],x[1],x[2],x[3],x[4]))


p = multi.Pool(processes=8)
p.map(func,array)

print(datetime.now() - start)

# normal SA
#single 0:04:51.939504
#parallel 0:01:27.703517

#Dynamic SA
# single: 0:00:25.150841
# parallel 0:00:06.772638


# 0:02:02.617523
# 0:00:35.323333


# pop of 30
# 0:03:12.804871
# 0:01:00.130893

# pop of 18
# 0:01:42.705822
# 0:00:32.519575

# pop of 8
# 0:00:40.779901
# 0:00:11.884592