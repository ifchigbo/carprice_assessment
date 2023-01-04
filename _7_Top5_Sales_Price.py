# QUESTION 2C 
# The code is an edited code block
from getDatPDDF import getCarNames
from getDatPDDF import getDataColumns
from getDatPDDF import getCarasPDDF
from getBodytype import getUniqueBodyType
from getDatPDDF import df_header
from IPython.display import display
import tui

def getMostSellingCars(cardataset):
    cols = getDataColumns() # get all the car header that contains the columns
    #cardataset = getCarasPDDF() 
    unique_body_type = sorted(getUniqueBodyType()) # get the unique body type from the getBodyTypeModule
    
    try:
        # The section below enables the user select the car body from the menu selection below from the tui module
        #The if, elif code block below the while statement, displays the top 5 sellling cars per body type based on the users input from the unique_bodychoice selction
        #The price_body variable is declared to hold the dataframe of the body type, based on the user's input above
        #The result of the processing - top selling cars is displayed based on sorting the dataframe by price (highest to lowest) of the 5 top selling cars
        #The process is repeated from options 1 - 5 that represents each body type
        while True:
            unique_bodychoice = tui.carBodyType()
            if unique_bodychoice == 0:
                break;
            elif unique_bodychoice == 1:
                price_body = cardataset.loc[cardataset[df_header[4]] == unique_body_type[0]] 
                display(price_body.sort_values(by=cols[-1], ascending = False).head(5).reset_index())
            elif unique_bodychoice == 2:
                price_body = cardataset.loc[cardataset[df_header[4]] == unique_body_type[1]]
                display(price_body.sort_values(by=cols[-1], ascending = False).head(5).reset_index())
            elif unique_bodychoice == 3:
                price_body = cardataset.loc[cardataset[df_header[4]] == unique_body_type[2]]
                display(price_body.sort_values(by=cols[-1], ascending = False).head(5).reset_index())
            elif unique_bodychoice == 4:
                price_body = cardataset.loc[cardataset[df_header[4]] == unique_body_type[3]]
                display(price_body.sort_values(by=cols[-1], ascending = False).head(5).reset_index())
            elif unique_bodychoice == 5:
                price_body = cardataset.loc[cardataset[df_header[4]] == unique_body_type[4]]
                display(price_body.sort_values(by=cols[-1], ascending = False).head(5).reset_index())
            else:
                print(" ")
                print("Your input is invalid")
    
    except BaseException as error:
        print("The following error has occured: {}".format(error))


    