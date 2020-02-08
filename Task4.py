"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

telemarketer_prefix = "140"
possible_telemarketers = set()

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    
    for call in calls:
        caller = str(call[0])
        callee = str(call[1])
        
        if(caller.startswith(telemarketer_prefix)):
            possible_telemarketers.add(caller)
            
        if(callee.startswith(telemarketer_prefix)):
            if(callee in possible_telemarketers):
                possible_telemarketers.remove(callee)
    
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    
    for text in texts:
        sender = str(text[0])
        receiver = str(text[1])
        
        if(sender.startswith(telemarketer_prefix) or receiver.startswith(telemarketer_prefix)):
            if(sender in possible_telemarketers):
                possible_telemarketers.remove(sender)
                
            if(receiver in possible_telemarketers):
                   possible_telemarketers.remove(receiver)

sorted_possible_telemarketers = list(possible_telemarketers)
sorted_possible_telemarketers.sort()
print("These numbers could be telemarketers:")
for possible_telemarketer in sorted_possible_telemarketers:
    print(str(possible_telemarketer))
    
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

