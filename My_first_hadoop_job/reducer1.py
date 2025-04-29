#!/usr/bin/env python3
import sys

current_store = None
current_total_sales = 0.0

# Read input line by line
for line in sys.stdin:
    line = line.strip()
    
    # Split the line into store and cost
    store, cost = line.split("\t")
    
    try:
        cost = float(cost)
    except ValueError:
        continue  
    

    if store == current_store:
        current_total_sales += cost
    else:

        if current_store:
            print(current_store + "\t" + str(current_total_sales))
        

        current_store = store
        current_total_sales = cost


if current_store:
    print(current_store + "\t" + str(current_total_sales))
