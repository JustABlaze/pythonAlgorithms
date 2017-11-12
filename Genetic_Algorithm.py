''''

Name: Mustafa Khalil
ID: 140201100

'''

import random

class gene():
    def __init__(self,x = [],y = []):
        self.x = x
        self.y = y
        self.value = 0.0

def invRounding(number):
    if isinstance(number, float):
        return round(number) - 1 if round(number)>number else round(number) + 1

def getPopulation(x):
    array = []
    for i in range(0,x):
        array.append(invRounding(random.uniform(0,1)))
    return array


def presision(num,len):
    return (num - (-num))/(2**len) -1

def convertTodecimal(a):
    number = 0
    for num in range(0,len(a)):
        if a[(len(a)-1)-num] == 1:
            number += 2**num
    return number

def generatePopulation(inital):
    array = []
    for i in range(0,inital):
        array.append(gene(getPopulation(3),getPopulation(3)))
    return array

print(generatePopulation(4))
