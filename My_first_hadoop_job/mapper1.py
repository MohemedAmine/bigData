
import sys

for line in sys.stdin:
    line = line.strip()

    fields = line.split()
    

    if len(fields) == 6:
        store = fields[2]  
        cost = float(fields[4]) 
        
        
        print(store + "\t" + str(cost))
