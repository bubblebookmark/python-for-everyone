# Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. 
# You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour.

handle = open("mbox-short.txt")
dic = dict()
for lines in handle:
    if lines.startswith('From:'):
        continue
    elif lines.startswith('From'):
        #print('line: ',line)
        words = lines.split(':')
        letters = words[0].split()
        dic[letters[5]] =dic.get(letters[5],0) + 1
for k,v in sorted(dic.items()):
    print(k,v)
    