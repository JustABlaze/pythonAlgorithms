
import random
import copy

layout = [
 [0, 1, 2, 3, 4, 1, 2, 3, 4, 5, 2, 3, 4, 5, 6],
 [10, 0, 1, 2, 3, 2, 1, 2, 3, 4, 3, 2, 3, 4, 5],
 [0, 1, 0, 1, 2, 3, 2, 1, 2, 3, 4, 3, 2, 3, 4],
 [5, 3, 10, 0, 1, 4, 3, 2, 1, 2, 5, 4, 3, 2, 3],
 [1, 2, 2, 1, 0, 5, 4, 3, 2, 1, 6, 5, 4, 3, 2],
 [0, 2, 0, 1, 3, 0, 1, 2, 3, 4, 1, 2, 3, 4, 5],
 [1, 2, 2, 5, 5, 2, 0, 1, 2, 3, 2, 1, 2, 3, 4],
 [2, 3, 5, 0, 5, 2, 6, 0, 1, 2, 3, 2, 1, 2, 3],
 [2, 2, 4, 0, 5, 1, 0, 5, 0, 1, 4, 3, 2, 1, 2],
 [2, 0, 5, 2, 1, 5, 1, 2, 0, 0, 5, 4, 3, 2, 1],
 [2, 2, 2, 1, 0, 0, 5, 10, 10, 0, 0, 1, 2, 3, 4],
 [0, 0, 2, 0, 3, 0, 5, 0, 5, 4, 5, 0, 1, 2, 3],
 [4, 10, 5, 2, 0, 2, 5, 5, 10, 0, 0, 3, 0, 1, 2],
 [0, 5, 5, 5, 5, 5, 1, 0, 0, 0, 5, 3, 10, 0, 1],
 [0, 0, 5, 0, 5, 10, 0, 0, 2, 5, 0, 0, 2, 4, 0]]

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



def update(object,path,taboolist1,taboolist2,taboolist3,tp,bestSoFar,bestPath):

    taboolist1.append(path)
    taboolist1.append(object[2])
    taboolist1.append(object[3])

    if len(taboolist1) > tp:
        taboolist1 = taboolist1[1:] # update tabu if more than allowed
        taboolist2 = taboolist2[1:] # update tabu if more than allowed
        taboolist3 = taboolist3[1:] # update tabu if more than allowed

    if object[1] < bestSoFar:
        bestSoFar = object[1]
        bestPath = object[0]

    return ([taboolist1,taboolist2,taboolist3],bestSoFar,object[0],bestPath)



def taboo(tabuPeriod,layout):
    tp = tabuPeriod
    dataSet = layout
    intialSolution = []
    for i in range(0,len(dataSet)):
        intialSolution.append(i+1)
    random.shuffle(intialSolution)

    bestSolution = fitenss(intialSolution,dataSet)
    bestPath = copy.copy(intialSolution)
    tabooList1 = [] # tabu list 1 where it saves the current path placement
    tabooList2 = [] # tabu list 2 where it saves the swapped items
    tabooList3 = [] # tabu list 3 where it saves the indices of the swapped items
    currentPath = copy.copy(intialSolution)


    for i in range(0,10):

        solutionArrays = []

        for i in range(0,len(currentPath)-1):
            for j in range(i+1,len(currentPath)):
                array = copy.copy(currentPath)
                swap = (currentPath[i],currentPath[j])
                array[i] = swap[1]
                array[j] = swap[0]
                solutionArrays.append((array,fitenss(array,dataArray=dataSet),swap,(i,j)))

        solutionArrays = sorted(solutionArrays, key=lambda x: x[1])

        for i in solutionArrays:

            path = ' '.join(str(e) for e in i[0])

            if i[0] not in tabooList1 and i[2] not in tabooList2 and i[3] not in tabooList3:
                # this elif check if it's tabu.

                x = update(object=i, path=path, taboolist1=tabooList1,taboolist2=tabooList2,taboolist3=tabooList3, tp=tp, bestSoFar=bestSolution,bestPath=bestPath)
                bestSolution = x[1]
                tabooList1 = x[0][0] # updating the tabu lists
                tabooList2 = x[0][1] # updating the tabu lists
                tabooList3 = x[0][2] # updating the tabu lists
                currentPath = x[2]
                bestPath = x[3]

                break

            elif (i[0] in tabooList1 or i[2] in tabooList2 or i[3] in tabooList3) and i[1] < bestSolution:
                # this elif check if it's tabu.
                x = update(object=i, path=path,taboolist1=tabooList1,taboolist2=tabooList2,taboolist3=tabooList3,tp=tp,bestSoFar=bestSolution,bestPath=bestPath)
                bestSolution = x[1]
                tabooList1 = x[0][0] # updating the tabu lists
                tabooList2 = x[0][1] # updating the tabu lists
                tabooList3 = x[0][2] # updating the tabu lists
                currentPath = x[2]
                bestPath = x[3]
                break

    return (bestPath,bestSolution)


x = taboo(tabuPeriod=1,layout=layout)
print(x)




