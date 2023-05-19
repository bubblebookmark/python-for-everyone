# Finding Numbers in a Haystack
# In this assignment you will read through and parse a file with text and numbers.
# You will extract all the numbers in the file and compute the sum of the numbers.

import re
lis = []
lst = list()
count = 0
handle = open('regex_sum_1795728.txt')
for line in handle:
    line = line.rstrip()
    Numbers = re.findall('([0-9]+)', line)
    #print(Numbers)
    if len(Numbers) > 0: 
        lis.extend(Numbers)
for value in lis:
            count = count + int(value)
print(count)
