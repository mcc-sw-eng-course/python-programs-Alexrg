"""
Add a method in myPowerList to save the current list as a text file
- saveToTextFile(filename)
"""

def saveToTextFile(filename):
    filename = open("testfile.txt", "w")

    filename.write("Hello world")
    filename.write("This is our new textfile")

    filename.close()

    return filename
