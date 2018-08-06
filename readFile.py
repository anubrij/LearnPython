from sys import argv
script , file = argv

#open the file from parameter, and it is ready to read
text = open(file)
value = text.read()
name = "Anubrij Chandra"
print(value)
