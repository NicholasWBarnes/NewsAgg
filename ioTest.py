#NewsAgg FileTest
#This is a Python program to create, write, and read a file

wFile = open('testFile.txt', 'w')
wFile.write('\nThis is a test write\n')
intVal = 42
strVal = str(intVal)
strVal = strVal + '\n'
wFile.write(strVal)
wFile.write('This line comes after 42. Newline!! Yay!\n')
wFile.close()

rFile = open('testFile.txt', 'r')
inString = rFile.read()
print(inString)
rFile.close()

