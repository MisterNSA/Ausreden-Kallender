#################################################
# List of Functions for "Ausredenkallender"     #
# Creator: Tobias Dominik Weber aka MisterNSA   #
# Version 0.7.1 19.05.2020                      #
#################################################

import random
import time
import os
import sys


# imports excuses from a file and stores it in a list
def Data_import():
    excuses_list = []
    count = 0
    # try to extract the Path from the config .txt
    try:
        config = open("config.txt", "r")
        for line in config:
            # Count -> so that only the first is Read. Extendable if more config values are needed
            if count == 0:
                SOURCE = line
            count += 1
        config.close()
        # Strip Text in fron of Path and \n after Path
        SOURCE = SOURCE.lstrip("Path to excuses: â€ª")
        SOURCE = SOURCE.strip()

    except FileNotFoundError:
        # create a new config file
        f = open("config.txt", "w")
        f.write("Path to excuses: \n")
        f.write("Please let a single Space after the colon!")
        f.close()
        print("The config.txt was not found. A new one was created. Please insert the Path to your Excuses and rerun the programm!")
        sys.exit(0)
    # adds excuses to excuses_list
    if os.path.exists(SOURCE):
        Data_source = open(SOURCE, "r")
        for excuse in Data_source:
            excuses_list.append(excuse)
        Data_source.close()
        return(excuses_list)
    else:
        print("The Path isnt correct. Please check the Path in the config.txt or delete it, to create a new one!")
        sys.exit(0)


# Return day as a Int-value | first day = 1 and so on
def Today():
    return int(time.strftime("%d", time.localtime()))


# Choose a random excuse and remove it from the list
def Choose_random_excuse(excuses_list):
    excuse = random.choice(excuses_list)
    index = excuses_list.index(excuse)
    excuses_list.pop(index)
    return(excuse)

