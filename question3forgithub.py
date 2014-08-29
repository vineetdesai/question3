# -*- coding: utf-8 -*-
"""
Created on Wed Aug 27 12:19:24 2014

@author: Vineet  Desai
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Aug 27 10:20:45 2014

@author: Vineet  Desai
"""
output = open("output.txt", 'w')
output.close()
num_lines = sum(1 for line in open('shortversion.fasta'))
print "The number of lines is", num_lines
seq_len = 0
flag = True
fp = open("shortversion.fasta")
count = 0
location = 0
header = ''
temp = fp.readline()
count = count + 1
while count <= num_lines:
    if temp[0] == '>':
        header = temp[:]
        temp = fp.readline()
        location = fp.tell()
        count = count + 1
        if len(temp) > 0 and temp[0] == '>':
            print header + str(seq_len)
            output = open("output.txt", 'a')
            output.write("\n" + str(header) + str( seq_len))
            output.close()
            fp.seek(location)
        if len(temp) == 0:
            print header + str(seq_len)
            output = open("output.txt", 'a')
            output.write( "\n" + str(header) + str( seq_len))
            output.close()
            #print str(0)
    else:
        while temp[0] != '>':
            seq_len = seq_len + len(temp.replace('\n', ''))
            location = fp.tell()
            temp = fp.readline()
            if count == num_lines:
                break
            count = count + 1
        print header + str(seq_len)
        output = open("output.txt", 'a')
        output.write("\n" + str(header) + str( seq_len))
        output.close()
        if count == num_lines:
            break
        seq_len = 0