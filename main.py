from time import localtime, sleep
from display import digit_display
import re
import sys

'''
TO DO:

Reduce complexity of pytime:
    Break out print while loop to seperate function
Add time increment setting
Show start / stop time at conclusion
Utilise flags to set args

'''


def pytime(time_as_string: str = None, countdown_to_time: bool = False, increment_seconds: int = 1):
    """
    Outputs a digital clockface, counting down provided hours:minutes:seconds to a set time, counting down a specified amount of time, or running as a stopwatch if no arguments are passed (default).

    :params:
    (optional) countdown_to_time: str -> amount of time or a set time, in 24hr format HH:MM:SS 
    (optional) countdown_to_time: bool = False -> when set to false counts down to provided countdown_time in 24hr format
    (optional) increment_seconds: int = 1 -> set time inverval

    uses digit_display to draw digital clock

    """
    if not time_as_string:
        time_in_seconds = 0
        direction = increment_seconds - (2 * increment_seconds)

    elif time_as_string:
        # Check time format
        try:
            assert re.search(
                r'[0-2][0-9]:[0-5][0-9]:[0-5][0-9]', time_as_string)
        except AssertionError:
            print('Time not understood, provide as follows in 24hr format -> HH:MM:SS')
            sys.exit()

        # Calculate amount of seconds in time_as_string
        hours, mins, secs = time_as_string.split(':')
        time_in_seconds = (int(hours) * 3600) + (int(mins) * 60) + int(secs)
        direction = increment_seconds

        # If counting down to specific time, determine amount of seconds between current time and provided time
        if countdown_to_time:
            lt = localtime()
            now = ((lt.tm_hour * 3600) + (lt.tm_min * 60) + lt.tm_sec)
            time_in_seconds = time_in_seconds - now

    else:
        print(
            f'Error: please check arguments below:\nTime in seconds: {time_in_seconds}\nCountdown to specific time: {countdown_to_time}')

    # Every second, print the time remaining until timer is up
    done = False

    while not done:
        hours = (time_in_seconds // 3600)
        if hours < 10:
            hours = '0' + str(hours)
        mins = (time_in_seconds % 3600 // 60)
        if mins < 10:
            mins = '0' + str(mins)
        secs = (time_in_seconds % 60)
        if secs < 10:
            secs = '0' + str(secs)
        time_in_seconds -= direction

        print(('\n' * 20))
        print(digit_display(f'{hours}:{mins}:{secs}', 6))

        sleep(increment_seconds)

        if time_in_seconds <= 0:
            print('Times up!')
            done = True


if __name__ == "__main__":
    try:
        i = input(
            'Press enter to start as stopwatch or use T [timer] or C [countdown]: ')
        if not i:
            pytime()
        else:
            time_string = input('Enter time in format HH:MM:SS: ')
            if i == 'C':
                pytime(time_as_string=time_string, countdown_to_time=True)
            elif i == 'T':
                pytime(time_as_string=time_string)
    except KeyboardInterrupt:
        print('\nTimer stopped')
        sys.exit()
