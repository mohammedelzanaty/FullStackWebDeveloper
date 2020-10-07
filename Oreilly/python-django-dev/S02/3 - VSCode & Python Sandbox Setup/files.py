# Python has functions for creating, reading, updating, and deleting files.

import os


__location__ = os.path.realpath(os.path.join(
    os.getcwd(), os.path.dirname(__file__)))

# Open a file
myFile = open(os.path.join(__location__, 'test.txt'), 'w')

# Get some info
print('Name: ', myFile.name)
print('Is Closed: ', myFile.closed)
print('Opening Mode: ', myFile.mode)

# Write to file
myFile.write('I love Python')
myFile.write(' and JavaScript')
myFile.close()

# Append to file
myFile = open(os.path.join(__location__, 'myfile.txt'), 'a')
myFile.write(' I also like PHP')
myFile.close()

# Read from file
myFile = open(os.path.join(__location__, 'myfile.txt'), 'r+')
text = myFile.read(100)
print(text)