import sys
import csv
from datetime import datetime


for line in sys.stdin:
    
    line = line.strip()

    
    fields = line.split(',')
    
    if len(fields) < 9:
        continue
    
    
    location = fields[0]
    event_date = fields[1]
    event_type = fields[3]

    
    if 'regains' in event_type.lower():
        
        try:
            date_obj = datetime.strptime(event_date, "%m/%d/%y")
            formatted_date = date_obj.strftime("%Y-%m-%d")
            
            print("{}\t{}".format(location, formatted_date))
        except ValueError:
            continue
