from time import localtime, sleep
from display import digit_display
import re
import sys


def pytimer(countdown_time: str, timer: bool = True) -> str:
    """
    Outputs a countdown clock, counting down provided minutes or to provided time with timer=False

    :params:
    countdown_time: str -> amount of time or a set time, in 24hr format HH:MM:SS 
    (optional) timer: bool = True -> when set to false counts down to provided countdown_time in 24hr format

    prints countdown clock to console
    """

    # Check time format
    try:
        assert re.search(r'[0-2][0-9]:[0-5][0-9]:[0-5][0-9]', countdown_time)
    except AssertionError:
        print('Time not understood, provide as follows in 24hr format -> HH:MM:SS')
        sys.exit()

    # Calculate amount of seconds in countdown_time
    hours, mins, secs = countdown_time.split(':')
    time_in_seconds = (int(hours) * 3600) + (int(mins) * 60) + int(secs)

    # If counting down to specified time, determine seconds until then
    if not timer:
        lt = localtime()
        now = ((lt.tm_hour * 3600) + (lt.tm_min * 60) + lt.tm_sec)
        time_in_seconds = time_in_seconds - now

    # Every second, print the time remaining until timer is up
    done = False

    while not done:

        time_in_seconds -= 1
        hours = (time_in_seconds // 3600)
        if hours < 10:
            hours = '0' + str(hours)
        mins = (time_in_seconds % 3600 // 60)
        if mins < 10:
            mins = '0' + str(mins)
        secs = (time_in_seconds % 60)
        if secs < 10:
            secs = '0' + str(secs)

        sleep(1)

        print(('\n' * 10))
        print(digit_display(f'{hours}:{mins}:{secs}', 6))

        if time_in_seconds == 0:
            print('Times up!')
            done = True


if __name__ == "__main__":
    try:
        y = input('Type [y/Y] if providing a time -> ')
        if y:
            pytimer(countdown_time=input(
                'Enter time HH:MM:SS -> '), timer=False)
        else:
            pytimer(countdown_time=input('Set timer HH:MM:SS -> '))
    except KeyboardInterrupt:
        print('\nCountdown cancelled')
        sys.exit()
