"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

bangalore_fixed_line_prefix = "(080)"
fixed_line_prefix = "("
fixed_line_suffix = ")"
telemarketer_prefix = "140"

number_of_calls_from_banganlore_fixed_line = 0
number_of_calls_to_banganlore_fixed_line = 0
list_of_codes = set()

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

    for call in calls:
        caller = str(call[0])
        callee = str(call[1])
        
        if(caller.startswith(bangalore_fixed_line_prefix)):
            number_of_calls_from_banganlore_fixed_line += 1.0
            
            if(callee.startswith(bangalore_fixed_line_prefix)):
                number_of_calls_to_banganlore_fixed_line += 1.0
            
            if(callee.startswith(telemarketer_prefix)):
                list_of_codes.add(telemarketer_prefix)
            elif(callee.startswith(fixed_line_prefix)):
                list_of_codes.add(callee[:callee.index(fixed_line_suffix) + 1])
            else:
                list_of_codes.add(callee[:4])

ordered_list_of_codes = list(list_of_codes)
ordered_list_of_codes.sort()
print("The numbers called by people in Bangalore have codes:")
for code in ordered_list_of_codes:
    print(code)

from_bangalore_to_bangalore_ratio = (number_of_calls_to_banganlore_fixed_line / number_of_calls_from_banganlore_fixed_line) * 100

print("{0:.2f}".format(round(from_bangalore_to_bangalore_ratio, 2)) + " percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
