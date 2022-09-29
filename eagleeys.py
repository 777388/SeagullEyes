import sys
import os 
target = sys.argv[1] 
i = 0
with open('rootservers.txt', 'r') as file:
    for line in file:
        i += 1
        c = ("wsl dig +trace "+line.rstrip()+" +noidnin +noidnout & gau "+str(target)+" --o "+str(i)+".txt")
        o = os.system(c)
            
print("diff -u 1.txt 2.txt > a.txt")
