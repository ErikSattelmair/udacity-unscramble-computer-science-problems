"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    first_data_set = texts[0]
    print("First record of texts, " + str(first_data_set[0]) + " texts " + str(first_data_set[1]) + " at time " + str(first_data_set[2]))
    
with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    last_data_set = calls[-1]
    print("Last record of calls, " + str(last_data_set[0]) + " calls " + str(last_data_set[1]) + " at time " + str(last_data_set[2]) + " 	lasting " + str(last_data_set[3]) + " seconds")
        
"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""



