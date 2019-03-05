import random
from exEleven import sortList
from exTwelve import Rmerge, Lmerge
from exThirteen import saveToTextFile

"""
Create a class called myPowerList, implement methods for
- Adding items
- Removing the n- th item
"""

def addItem(list):
    x = random.randint(1,9)
    list.append(x)
    return list

def removeLastItem(list):
    x = list[-1:]
    list.remove(x)
    return list

myPowerList = []
myOtherPowerList = [1,2,3]

for i in range(0,5):
    addItem(myPowerList)

print("My power list: {}".format(myPowerList))
print("Just a second list: {}".format(myOtherPowerList))

right_merge = Rmerge(myOtherPowerList,myPowerList)
left_merge = Lmerge(myOtherPowerList,myPowerList)

print("Right merge: {}".format(right_merge))
print("Left merge: {}".format(left_merge))

saveToTextFile("ale")
file = open("testfile.txt", "r")
print (file.read())
