import random
import os
import sys

count = 0

while True:
    num = random.randint(1,14000000)
    if num == 1:
        print(f"lucky - {count}")
        break
    elif count == 14000000:
        print(f"not lucky - {count}")
        break
    else:
        count = count + 1
        #sys.stdout.write(f"({count}-{num})\r")
        sys.stdout.write(f'\033[K({count}-{num})\r')
        #sys.stdout.flush()
        #os.write(count)
        #print(dir(os))
        #print(f"({count}-{num})")
