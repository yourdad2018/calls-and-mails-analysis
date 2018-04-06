"""
Intro to Python Lab 1, Task 4

Complete each task in the file for that task. Submit the whole folder
as a zip file or GitHub repo. 
Full submission instructions are available on the Lab Preparation page.
"""

"""
Read file into texts and calls. 
It's ok if you don't understand how to read files
You will learn more about reading files in future lesson
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers: 
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message: 
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

textsNumbers = set()
callsReceiveNumbers = set()
callsMakeNumbers = set()
telemarketerNumbers = []

for i in texts:
    textsNumbers.add(i[0])
    textsNumbers.add(i[1])

for i in calls:
    callsReceiveNumbers.add(i[1])
    callsMakeNumbers.add(i[0])

for i in callsMakeNumbers:
    if i not in textsNumbers and i not in callsReceiveNumbers:
        telemarketerNumbers.append(i)

telemarketerNumbers.sort()
print("These numbers could be telemarketers: ")
for i in telemarketerNumbers:
    print(i)
