### PyTimer

The other day my girlfriend asked me to set a timer for a batch of cookies going in the oven. I was writing some random code at the time and thought, wouldn't it be great if i could just do this from the command line?

One burnt, forgotten tray of cookies later Pytimer was complete...

This is a super simple command line based timer with ~~two~~ three(!) functions, a stopwatch (default) a timer and a countown clock.

Run it: `python3.10 main.py` and hit enter to start a stopwatch

Alternatively answer the prompt: `Press enter to start as stopwatch or use T [timer] or C [countdown]:`
`T` will prompt you to set a timer, `C` will prompt you for an end time.

Provide inputs in 24 hour format HH:MM:SS, such as `12:34:57`

This will display a countdown clock as so:

      ,    ___       ___     ,       ___   ___
     /|       |         |   /|      |     |
      |    ___|  .   ___|  / |   .  |___  |___
      |   |      .      | /__|_  .      | |   |
    __|__ |___       ___|    |       ___| |___|

Thats it!
