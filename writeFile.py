from sys import argv
#argv is the arguments of script to be passed in execution
#we asign the argument values to the variable
script, filepath = argv
#open the file wiith writable access
file = open(filepath, 'w')
file.truncate()
file.write("this is new text")
#print(file.read())
file.close()
