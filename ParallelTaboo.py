
"""
    Name: Mustafa Khalil
    ID: 140201100

"""
import math
import random
import copy
import multiprocessing as mp

class optimizedPath():
    def __init__(self,array,value,moved,index):
        self.array = array
        self.value = value
        self.moved = moved
        self.index = index

class Taboo():
    def __init__(self,tb1 = None,tb2 = None,tb3 = None,dtb1 = None,dtb2 = None,dtb3 = None,memory1 = 1):
        self.tb1 = tb1
        self.tb2 = tb2
        self.tb3 = tb3
        self.dictTb1 = dtb1
        self.dictTb2 = dtb2
        self.dictTb3 = dtb3
        self.Memory = memory1


    def checker(self,path,moved,index):
        if self.tb1 != None and self.tb2 != None and self.tb3 != None:
            if path not in self.dictTb1 and moved not in self.dictTb2 and index not in self.dictTb3:
                return False

        elif self.tb1 != None and self.tb2 != None and self.tb3 == None:
            if path not in self.dictTb1 and moved not in self.dictTb2:
                return False
        elif  self.tb1 != None and self.tb2 == None and self.tb3 == None:
            if path not in self.dictTb1:
                return False
        return True


    def maintain(self):

        temp = self.tb1[0]
        self.tb1 = self.tb1[1:]
        del self.dictTb1[temp]

        if self.tb2 != None:
            temp = self.tb2[0]
            self.tb2 = self.tb2[1:]
            x = self.dictTb2[temp]
            if x == 1:
                del self.dictTb2[temp]
            else:
                self.dictTb2[temp] -= 1

        if self.tb3 != None:

            temp = self.tb3[0]
            self.tb3 = self.tb3[1:]
            x = self.dictTb3[temp]

            if x == 1:
                del self.dictTb3[temp]
            else:
                self.dictTb3[temp] -= 1

    def add(self,path,Object):

        self.tb1.append(path)
        self.dictTb1[path] = True

        if self.tb2 != None:
            self.tb2.append(Object.moved)

            if Object.moved in self.dictTb2:
                self.dictTb2[Object.moved] += 1
            else:
                self.dictTb2[Object.moved] = 1

        if self.tb3 != None:
            self.tb3.append(Object.index)

            if Object.index in self.dictTb3:
                self.dictTb3[Object.index] += 1
            else:
                self.dictTb3[Object.index] = 1



def openTxt():
    with open('test.txt','r') as f:
        content = f.readlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
    content = [x.strip() for x in content]
    return content


def GetData():
    content = openTxt()
    content = content[1:]
    dataArray = []
    i = 0
    for string in content:
        dataArray.append([])
        for word in string.split():
            dataArray[i].append(int(word))

        temp = dataArray[i]
        temp = temp[1:]
        dataArray[i] = temp
        i += 1

    return dataArray

# Gets the fitness of the matrix
def fitenss(currentPlacement,dataArray):

    # initial value of z
    z = 0
    # initial value of the distance
    distance = 0

    # we use the range function which is exclusive for the last element
    ##################
    # the arrays go from 0 and not 1
    # Data array should be matched
    ##################
    # This loop goes from the beginning of the currentPlacement array to n-1
    for i in range(0,len(currentPlacement)-1):

        # This loop goes from the i+1 to the end of the currentPlacement array

        for j in range(i+1,len(currentPlacement)):

            # flow gets the flow element from the lower part of the array
            flow = dataArray[j][i]

            if currentPlacement[i] < currentPlacement[j]:
                distance = dataArray[currentPlacement[i]-1][currentPlacement[j]-1]
            else:
                distance = dataArray[currentPlacement[j]-1][currentPlacement[i]-1]

            z = z + distance*flow
    return z



def update(object,path,tabooDict,tp,bestSoFar,bestPath):

    tabooDict.add(Object=object,path=path)

    if len(tabooDict.tb1) > tp:
        tabooDict.maintain()

    if object.value < bestSoFar:
        bestSoFar = object.value
        bestPath = object.array

    return (tabooDict,bestSoFar,object.array,bestPath)

def taboo():
    tp = 8
    dataSet = GetData()
    intialSolution = []
    for i in range(0,len(dataSet)):
        intialSolution.append(i+1)

    random.shuffle(intialSolution)
    count = 0
    bestSolution = fitenss(intialSolution,dataSet)
    previousSolution = bestSolution
    bestPath = copy.copy(intialSolution)
    tabooLists = Taboo(tb1=[],tb2=[],tb3=[],dtb1={},dtb2={},dtb3={},memory1=3)
    currentPath = copy.copy(intialSolution)

    # while True:
    for i in range(0,450):
        solutionArrays = []
        for i in range(0,len(currentPath)-1):
            for j in range(i+1,len(currentPath)):
                array = copy.copy(currentPath)
                swap = (currentPath[i],currentPath[j])
                array[i] = swap[1]
                array[j] = swap[0]
                solutionArrays.append(optimizedPath(array=array,value=fitenss(array,dataArray=dataSet),moved=swap,index=(i,j)))

        solutionArrays = sorted(solutionArrays, key=lambda x: x.value)

        for i in solutionArrays:

            path = ' '.join(str(e) for e in i.array)
            if tabooLists.checker(path=path,moved=i.moved,index=i.index) == False:
                x = update(object=i, path=path, tabooDict=tabooLists, tp=tp, bestSoFar=bestSolution,bestPath=bestPath)
                bestSolution = x[1]
                tabooLists = x[0]
                currentPath = x[2]
                bestPath = x[3]
                break

            elif tabooLists.checker(path=path,moved=i.moved,index=i.index) and i.value < bestSolution:
                x = update(object=i, path=path,tabooDict=tabooLists,tp=tp,bestSoFar=bestSolution,bestPath=bestPath)
                bestSolution = x[1]
                tabooLists = x[0]
                currentPath = x[2]
                bestPath = x[3]
                break

        # if bestSolution == previousSolution and count == 3:
        #     break
        #
        # if bestSolution == previousSolution:
        #     count += 1
        #
        # if bestSolution < previousSolution:
        #     previousSolution = bestSolution
        #     count = 0

    return (bestPath,bestSolution)


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
    print(taboo())


print(datetime.now() - start)

start=datetime.now()

def func(x):
    print(x)
    print(taboo())

p = mp.Pool(processes=8)
p.map(func,array)

print(datetime.now() - start)