# The code block gets all cars with specific body type
from getBodytype import getUniqueBodyType
from getDatPDDF import getCarasPDDF #gets the car assessment data frame
from loaddata import df_header # Gets the column list from load data module
from IPython.display import display
import tui

car_body_type = sorted(getUniqueBodyType()) # assign the unique car body type to the variable car_body_type
#cardf = getCarasPDDF()
#The method retrieveCarsBody is used to access a group of cars with same body type. 
# The body choice vairable allows the user enter an int value to view cars under diffrent body type as was retrieved from car dataframe (cardf)
def retrieveCarsBody(cardf):
    try:
        
        while True: # creating a tui within the master tui module
            bodychoice = tui.carBodyType()
            # menu option for the different car body type
            # cardf.loc[cardf[df_header[4]] is used to get the Carbody type header from the list of columns
            # car_body_type[x], where x = 0 to 4 is used to get the specific car body types from the car_body_type list
            if bodychoice == 1:
                display(cardf.loc[cardf[df_header[4]]== car_body_type[0]])
            elif bodychoice == 2:
                display(cardf.loc[cardf[df_header[4]]== car_body_type[1]])
            elif bodychoice == 3:
                display(cardf.loc[cardf[df_header[4]]== car_body_type[2]])
            elif bodychoice == 4:
                display(cardf.loc[cardf[df_header[4]]== car_body_type[3]])
            elif bodychoice == 5:
                display(cardf.loc[cardf[df_header[4]]== car_body_type[4]])
            elif bodychoice == 0:
                break
            else:
                print("Your input is invalid")
    except BaseException as error:
        print("The following error has occurred: {}".format(error))    


    