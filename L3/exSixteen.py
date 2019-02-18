import math

def upper(floatNum):
    x = math.ceil(floatNum)
    return x

fnum = 4.1
fupnum = upper(fnum)

print("Math ceil of {} = {}".format(fnum, fupnum))