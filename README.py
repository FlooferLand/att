"""
    <!> Don't change these since this is just documentation,
    the .py extension is used for syntax highlighting.

    Below are all the default settings, their names, and descriptions.
    When a setting isn't set the program will use these defaults.

    If you wanna change a default value change it in main.py however
    i recommend against that since it could break configs.

    All default options are overwritten by the ones in configs/GLOBAL_CONFIG.py
    if they're specified.

    And remember, every config file is a Python file so you can do pretty much
    anything in it.
"""

# The time until the program starts (in integer seconds)
# (3 seconds by default)
time_until_start = 3

# The time spent between each line (or between each enter press)
# (1.25 seconds by default)
time_between_lines = 1.25

# The minimum and maximum time each key press could take (in seconds, probably)
# (0.02 and 0.08 by default)
min_time_between_keys = 0.02
max_time_between_keys = 0.08

# Whenever it should shift-enter when there's no character on a line
# (True by default)
shiftenter_on_null_line = True

# Repeat text?
# (False by default)
repeat_text = False

# Enter?
# (True by default)
enter = True
