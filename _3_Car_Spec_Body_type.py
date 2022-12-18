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
        #print("The following Body types are available {}".format(car_body_type))
        #bodychoice = int(input("Enter 1 for {} \n, Enter 2 for {} \n, Enter 3 for {} \n, Enter 4 for {} \n, Enter 5 for {} \n".format(car_body_type[0],car_body_type[1],car_body_type[2],car_body_type[3],car_body_type[4])))
        while True:
            bodychoice = tui.carBodyType()
            # ---print(bodychoice,"this is ", car_body_type[bodychoice])
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

#if __name__ == "__main__":
    #retrieveCarsBody()
        #this should be the highest selling car
    