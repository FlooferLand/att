import configs.GLOBAL_CONFIG as global_config
from importlib import import_module
from random import randrange
from pyautogui import *
from tools import *
import os

# The options and their default values
config_options = (
    ("time_until_start"        , 3     ),
    ("time_between_lines"      , 1.25  ),
    ("min_time_between_keys"   , 0.02  ),
    ("max_time_between_keys"   , 0.08  ),
    ("shiftenter_on_null_line" , True  ),
    ("repeat_text"             , False ),
    ("autostart"               , False ),
    ("enter"                   , True  ),
)


# Reading config file
config = None
text_path = None
_config = file("config.txt")
for line in _config.splitlines():
    words = line.strip().split('=')
    if words[0].strip().startswith("config"):
        name = words[1].strip()
        config = import_module(f"configs.{name}.{name}")
        text_path = os.path.join("configs", name, config.text_name)


# Respecting global config, f
# There's probably a better way to do this but this works
for option in config_options:
    try:
        # Checking if an option is in global_config and if it is use it
        exec(f"test = global_config.{option[0]}")
        exec(f"config.{option[0]} = global_config.{option[0]}")
    except Exception:
        pass

# Setting default values
for option in config_options:
    try:
        # Checking if an option isn't in config
        exec(f"test = config.{option[0]}")
    except Exception as e:
        exec(f"config.{option[0]} = {option[1]}")



# Changing text path
text = file(text_path)


# Main functions ----------------
def waitForUser():
    for count in range(int(config.time_until_start)):
        print(f"Time remaining until mass spam:\n\t{config.time_until_start-count} seconds")
        sleep(1)


def main():
    global config
    try:
        while True:
            # going trough each line typing it out
            for line in text.splitlines():
                if len(line) < 2:
                    if config.shiftenter_on_null_line:
                        hotkey("shift", "enter")
                        sleep(config.time_between_lines / 2)
                else:
                    typewrite(
                        line,
                        interval=randrange(
                            int(config.min_time_between_keys * 1000),
                            int(config.max_time_between_keys * 1000)
                        ) * 0.001
                    )
                    if config.enter: press("enter")
                    sleep(config.time_between_lines)
            if not config.repeat_text: break
    except FailSafeException:
        print("Program paused.")
        inpu = input("(press enter to quit or type in \"unpause\" to unpause)")
        if inpu.lower().strip().startswith("un"):
            waitForUser()
            main()



# Visual start of the program
print("Press enter to start.")
print("Hold your cursor in a corner to exit.")
if not config.autostart: input()
waitForUser()
main()
