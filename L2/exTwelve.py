"""
Add a method in myPowerList to merge another list with the current list
- Lmerge (merge the list as prefix)
- Rmerge (merge the list as suffix)
"""
def Lmerge(listOne, myPowerList):
    list = myPowerList + listOne
    return list

def Rmerge(listOne, myPowerList):
    list = listOne + myPowerList
    return list