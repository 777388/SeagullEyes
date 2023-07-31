import sys
import os
target = sys.argv[1] 
i = 0
with open('rootservers.txt', 'r') as file:
    for line in file:
        i += 1
        c = os.system("dig +trace +noidnin +noidnout "+line.rstrip())
        z = os.system("hellfire --txt --file=rootservers.txt")
        x = os.system("gau "+str(target)+" --o "+str(i)+".txt")
            
print("diff -u 1.txt 2.txt > a.txt")
