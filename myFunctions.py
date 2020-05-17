#################################################
# List of Functions for "Ausredenkallender"     #
# Creator: Tobias Dominik Weber aka MisterNSA   #
# Version 0.7 17.05.2020                        #
#################################################

import random
import time


# imports excuses from a file and stores it in a list
def Data_import():
    excuses_list = []
    Data_source = open('Ausreden.txt', 'r')  # Path to File with excuses
    for excuse in Data_source:
        excuses_list.append(excuse)
    Data_source.close()
    return(excuses_list)


# Return day as a Int-value | first day = 1 and so on
def Today():
    return int(time.strftime("%d", time.localtime()))


# Choose a random excuse from the list
def Choose_random_excuse(excuses_list):
    excuse = random.choice(excuses_list)
    return(excuse)


# Checks, if excuse was already used
# three return Values:
# True - excuse wasent used jet
# False - excuse was used, but the are unused excuses left
# "All excuses used" - should be self explaining
def Check_for_duplicates(excuse, excuse_used, excuses_list):
    if excuse in excuse_used:
        if len(excuses_list) == len(excuse_used):
            return("All excuses used")
        else:
            return False
    else:
        return True
