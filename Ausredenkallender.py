#################################################
# Projektname: Ausredenkallender                #
# Creator: Tobias Dominik Weber aka MisterNSA   #
# Version 0.7 17.05.2020                        #
#################################################
import myFunctions

# List for alredy used excuses
excuses_used = []
# get List of excuses
excuses_list = myFunctions.Data_import()
today = myFunctions.Today()


def Main_Programm(excuses_used, excuses_list, today):
    excuse = myFunctions.Choose_random_excuse(excuses_list)
    # test if it is the same day
    if today == myFunctions.Today():
        # test if all excuses were used already
        if myFunctions.Check_for_duplicates(excuse, excuses_used, excuses_list) != "All excuses used":
            # test if current excuse was already used
            if myFunctions.Check_for_duplicates(excuse, excuses_used, excuses_list) != False:
                print("Todays excuse is: " + excuse)
                # Add excuse to list of used excuses
                excuses_used.append(excuse)
                print("Want to generate a new excuse? Y/N")
                Input = input().lower()
                if Input == "y":
                    Main_Programm(excuses_used, excuses_list, today)
            else:
                # Restart loop to choose new excuse
                Main_Programm(excuses_used, excuses_list, today)
        else:
            print("All Excuses were used. Want to reset the excuses? Y/N")
            Input = input().lower()
            if Input == "y":
                # update day, clear list of used excuses and restart the loop
                today = myFunctions.Today()
                excuses_used = []
                Main_Programm(excuses_used, excuses_list, today)
    else:
        # update day, clear list of used excuses and restart the loop
        today = myFunctions.Today()
        excuses_used = []
        Main_Programm(excuses_used, excuses_list, today)


if __name__ == "__main__":
    Main_Programm(excuses_used, excuses_list, today)
