import sys

current_word = None
current_count = 0

for line in sys.stdin:
    line = line.strip()
    word, count = line.split("\t")
    count = int(count)
    
    if word == current_word:
        current_count += count
    else:
        if current_word:
            # Use the % operator for compatibility
            print("%s\t%d" % (current_word, current_count))
        current_word = word
        current_count = count

if current_word:
    # Use the % operator for the last word
    print("%s\t%d" % (current_word, current_count))
