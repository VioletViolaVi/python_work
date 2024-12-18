# Countdown Exercise

import time

# count up
for num in range(1, 6):    
    print(num)
    time.sleep(1)
print("it's been 5 seconds")

# count down
for num in reversed(range(1, 6)):    
    print(num)
    time.sleep(1)
print("happy new year! 🎆🎇🎆")

# opposite to above
for num in range(5, 0, -1):    
    print(num)
    time.sleep(1)
print("happy new year! 🎆🎇🎆")
