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

        # gets & stores time for right now
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)

        # triggers actual alarm
        if current_time == alarm_time:
            print("Wake Up!")

            # initialise sound
            pygame.mixer.init()

            # loads sound file
            pygame.mixer.music.load(sound_file)

            # plays sound
            # plays for short moment
            pygame.mixer.music.play()

            # keeps sound file playing during while loop
            # sound file will stop being busy (return 'False') -> when song ends or software is stopped prematurely
            while pygame.mixer.music.get_busy():
                time.sleep(1)

            # stops clock from running
            is_running = False

        # updates time every second
        time.sleep(1)


# to run this python file directly
if __name__ == "__main__":

    # prompts user what they want to set alarm to
    alarm_time = input("Enter alarm time (HH:MM:SS): ")

    # runs function body
    set_alarm(alarm_time)

