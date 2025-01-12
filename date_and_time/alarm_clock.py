# Alarm Clock

# 'time' -> to change time every second for alarm clock
# 'datetime' -> allows to work w/ string representations of time 
# 'pygame' -> to provide sound effects
import time, datetime, pygame

# display string representation of time
def set_alarm(alarm_time):
    print(f"Alarm set time for: {alarm_time}")

    # for file sound is in
    sound_file = "sound_file.mp3"

    # determines if alarm clock is running
    is_running = True

    # keeps going until alarm clock is to run no more
    while is_running:



# to run this python file directly
if __name__ == "__main__":

    # prompts user what they want to set alarm to
    alarm_time = input("Enter alarm time (HH:MM:SS): ")

    # runs function body
    set_alarm(alarm_time)

