# Countdown timer

import time

# countdown timer to take off 🚀
def countdown(highest_num, lowest_num=1):
    # to count backwards
    for count in reversed(range(lowest_num, highest_num + 1)):
        print(count)
        time.sleep(1)
    print("Lift off! 🚀")

# countdown from 5 to 1
countdown(1, 5)
# countdown from 10 to 1
countdown(1, 10)
# using default argument, countdown from 3 to 1
countdown(3)


print("------ new ------")
print()



