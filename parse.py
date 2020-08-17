import os
import sys
from dedpulicate import deduplicate
from sort import sort

def parse(filepath):
    with open(filepath, 'r') as file:
        data = file.read().replace('\n', ' ')
        data = ' '.join(deduplicate(data))
        return sort(data)

def main():
    print(parse(sys.argv[1]))

if __name__ == "__main__":
    main()