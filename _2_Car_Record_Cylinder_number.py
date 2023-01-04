from getDatPDDF import getCarasPDDF # import the data frame variable from the 
from loaddata import df_header
from IPython.display import display
import tui



#below we define a function with parameter that takes cylinder as a paramter to get the number of cylinders a given car has
# This function is called in the getCarbyCylinderNumber function below
def chooseCylindertoDisplay(df,cylinder):
    try:
        car_by_cylinder_num = df.loc[df["cylindernumber"] == cylinder]
        return car_by_cylinder_num
    except BaseException as error:
        print("The following error occured {}".format(error))

# function below handles all logic responsible for getting cars with a particulare cylinder number
def getCarbyCylinderNumber(df):

    #The line below, get the unique cylinder numbers using set () from the data frame index to the cylinder numbe
    unique_cylinder_numbers = [cylinders for cylinders in set(df["cylindernumber"])]
    # the block below under the tr and except block will
    # give menu displaying cyliner options available for analysis in the data set
    # vallidate the user entry
    # allow the user to exit this program if they change their mind on running the program
    try:
        choice = int(input("We have cars with a set of cylinder number, press 1 to view them or press 2 to quite - please enter an Integer"))
        print("\n")
        
        if choice == 1:
            # The code below is a menu that enables the user view the Car cylinder options available in the data set
            # Enter the cylinder type you want to view you make this call via the TUI module for car Cylinders
            while True:
                cylinder_choice = tui.carCylinder()
                # input validation used to verify that the user has entered a cylinder number within the range of cylinder numbers in
                # given in the unique _cylinder_number variable 
                if cylinder_choice == 0:
                    break
                elif cylinder_choice not in unique_cylinder_numbers: 
                    print("Your Selected option is invalid")
                else:                
                    display(chooseCylindertoDisplay(df,cylinder_choice))
    
        elif choice == 2:
            print("You have exited this menu\n")
            print("Thank you for testing my functionalities!")
            
        else:
            print("Your input is invalid")
    except BaseException as error:
        print("The following error occured {}".format(error))

