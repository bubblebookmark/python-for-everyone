#  Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages.
#  The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
#  The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file.
#  After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
dic = dict()
wor = ()
for lines in handle:
    line = lines.rstrip()
    words = line.split()
    if  len(words) < 1 or words[0] != 'From':
        continue
    dic[words[1]] =dic.get(words[1],0) + 1 
largest = -1
theword = None
for k,v in dic.items():
    if theword is None or v > largest:
        largest = v
        theword = k

print(largest,theword)