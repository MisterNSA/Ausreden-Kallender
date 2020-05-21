#################################################
# Projektname: Ausredenkallender                #
# Creator: Tobias Dominik Weber aka MisterNSA   #
# Version 0.7 17.05.2020                        #
#################################################
import myFunctions

# get List of excuses
today = myFunctions.Today()
excuses_list = myFunctions.Data_import()


def Main_Programm(today, excuses_list):
    excuse = myFunctions.Choose_random_excuse(excuses_list)
    if len(excuses_list) != 0:
        if today == myFunctions.Today():
            print("Todays excuse is: {}".format(excuse))
            ValidInput = False
            while ValidInput == False:
                Input = input("Want to generate a new excuse? Y/N: ")
                Input = Input.lower()
                if Input in ["y", "n", "yes", "no"]:
                    ValidInput = True
                    if Input == "y":
                        Main_Programm(today, excuses_list)
                else:
                    print("Invalid Input. Please enter Y for Yes or n for no!")

        else:
            today = myFunctions.Today()
            excuses_list = myFunctions.Data_import()
            Main_Programm(today, excuses_list)
    else:
        ValidInput = False
        while ValidInput == False:
            Input = input(
                "All Excuses were used. Want to reset the excuses? Y/N: ")
            Input = Input.lower()
            if Input in ["y", "n", "yes", "no"]:
                ValidInput = True
                if Input == "y":
                    today = myFunctions.Today()
                    excuses_list = myFunctions.Data_import()
                    Main_Programm(today, excuses_list)
            else:
                print("Invalid Input. Please enter Y for Yes or n for no!")


if __name__ == "__main__":
    Main_Programm(today, excuses_list)
