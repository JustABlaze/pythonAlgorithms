
"""
    Name: Mustafa Khalil
    ID: 140201100

"""
import math

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
    # we use the range function with is exclusive for the last element
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
                flow = dataArray[currentPlacement[j]-1][currentPlacement[i]-1]

            z = z + distance*flow
    return z




def taboo():

    dataSet = GetData()
    print(len(dataSet))
    print(fitenss([4,2,3,6,8,9,5,10,7,15,1,12,13,14,11],dataSet))


"""

Matlab equivalent fitness test:
 
 fitness(4,[1,4,2,3],data)

"""