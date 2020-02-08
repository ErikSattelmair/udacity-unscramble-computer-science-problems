"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv

total_number_of_seconds_per_phone_number = {}

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

    for call in calls:
        caller = str(call[0])
        callee = str(call[1])
        duration = int(call[3])
        
        if(caller not in total_number_of_seconds_per_phone_number):
            total_number_of_seconds_per_phone_number[caller] = duration
        else:
            total_number_of_seconds_per_phone_number[caller] = total_number_of_seconds_per_phone_number[caller] + duration
        
        if(callee not in total_number_of_seconds_per_phone_number):
            total_number_of_seconds_per_phone_number[callee] = duration
        else:
            total_number_of_seconds_per_phone_number[callee] = total_number_of_seconds_per_phone_number[callee] + duration

phone_nuumber_with_max_time_on_phone = max(total_number_of_seconds_per_phone_number, key=total_number_of_seconds_per_phone_number.get)

max_seconds = total_number_of_seconds_per_phone_number[phone_nuumber_with_max_time_on_phone]

print(phone_nuumber_with_max_time_on_phone + " spent the longest time, " + str(max_seconds) + " seconds, on the phone during September 2016.")

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".
"""
