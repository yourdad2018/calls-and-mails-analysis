"""
Intro to Python Lab 1, Task 2

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
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message: 
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.". 

HINT: Build a dictionary with telephone numbers as keys, and their
total time spent on the phone as the values. You might find it useful
to write a function that takes a key and a value and modifies a 
dictionary. If the key is already in the dictionary, add the value to
the key's existing value. If the key does not already appear in the
dictionary, add it and set its value to be the given value.
"""

calls_dict = {}
max_time = 0


def set_call_time(call, time):
    if calls_dict.get(call):
        calls_dict[call] += time
    else:
        calls_dict[call] = time


for i in calls:
    set_call_time(i[0], int(i[3]))
    set_call_time(i[1], int(i[3]))


for i in calls_dict:
    if calls_dict[i] > max_time:
        max_time = calls_dict[i]
        tel_number = i

print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(tel_number,max_time))
