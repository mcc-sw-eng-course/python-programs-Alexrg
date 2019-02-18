import time

def cpuTime():
    start = time.time()
    end = time.time()
    timed = end - start
    return timed

def clockTime():
    clockStart = time.clock()
    closkEnd = time.clock()
    clockTimed = closkEnd - clockStart
    return clockTimed

clockTimed = clockTime()
timed = cpuTime()

print("Clock time: {}".format(clockTimed*1000))
print("CPU time: {}".format(timed*1000))

"A prerequisite before we dive into the difference of measuring time in Python is to" \
"understand various types of time in the computing world. The first type of time is" \
"called CPU or execution time, which measures how much time a CPU spent on executing a" \
"program. The second type of time is called wall-clock time, which measures the total" \
"time to execute a program in a computer. The wall-clock time is also called elapsed or" \
"running time. Compared to the CPU time, the wall-clock time is often longer because the" \
"CPU executing the measured program may also be executing other program's instructions at" \
"the same time. "