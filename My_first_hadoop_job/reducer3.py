import sys
from collections import defaultdict

locations = defaultdict(list)

for line in sys.stdin:
    line = line.strip()
    location, event_date = line.split('\t')
    
    locations[location].append(event_date)

for location, dates in locations.items():
    print("{}\t{}".format(location, ",".join(dates)))