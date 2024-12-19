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



print(" --- new --- ")



user_seconds = int(input("Enter a number of seconds: "))

for second in range(user_seconds, 0, -1):
    secs = second % 60
    mins = int(second / 60) % 60
    hours = int(second / 3600) % 60
    print(f"{hours:02}:{mins:02}:{secs:02}")
    time.sleep(1)
print("done")
