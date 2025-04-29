import sys

# Read input line by line
for line in sys.stdin:
    line = line.strip()
    words = line.split()
    for word in words:
        # Use the % operator for compatibility
        print("%s\t%d" % (word, 1))
