from getDatPDDF import getCarasPDDF, getDataColumns
from IPython.display import display
from sys import exit
import tui

#cardata = getCarasPDDF()
dfcolumns = getDataColumns()

def getSpecColumnsbyCarID(cardata):
    print("You can only enter a maximum of 5 columns")
    print("Select the column you want to display for a given car ID, except the Car_ID column")
    print("\n")
   
    # your must enter a set of 5 numbers corresponding to the the column you are interested
    # in displaying for a given car ID
    try:
        entry_count = 0 # collection of options for column to view
        col_option_list = [1] # list to hold our choices, option 1 in this list already reserves a space for the carIDvariable
        # The while block is used to get a set of column input in int that represents column values that the user wants retireved 
        # This will be columns related to an indivual car
        while entry_count < 5:
            #choice = int(input("Enter the value for the columns you want to display: "))
            choice = tui.uniqueColumnData()
            # The last element of our column list is on index 19 which is 20
            # The if block validates whether the user's input is more than 20 
            if choice > 20:
                print("Your Column input should not be more than 20 (Index of the last Column element)")
                break
            if choice not in col_option_list: # condition to check and confirm that no same number is entered twice
                col_option_list.append(choice)
            else:
                print("Please select unique columns")
                break
            entry_count += 1

        if len(col_option_list) == 6: # the sixth value is the CarID value that will be part of the program's display result
            car_id_choice = int(input("Enter the Car ID you want to display its details for the columns above")) # get the Car ID from the Use
        else:
            print("\n")
            print("The code is exiting .............")
            exit()

        # The new_car_df variable below is formated create a sub data frame from that original data frame that enables our program display our selected columns
        new_car_df = cardata[[dfcolumns[0],dfcolumns[col_option_list[0]],dfcolumns[col_option_list[1]],dfcolumns[col_option_list[2]],dfcolumns[col_option_list[3]],dfcolumns[col_option_list[4]]]] # create new data frame with the selected user columns
        display(new_car_df.loc[new_car_df[dfcolumns[0]] == car_id_choice])
        
    except BaseException as error:
        print("\n")
        print("The following error has occured: {}".format(error))


