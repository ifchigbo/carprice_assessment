from getBodytype import getUniqueBodyType
from getDatPDDF import getCarasPDDF
from getDatPDDF import getDataColumns
import pandas as pd
import tui

#The bodychoice varaible in the method
# allows the user enter an int value to view cars under diffrent body type as was retrieved from getCarasPDDF function from the getDatPDDF module
def getSalesSummary(cardataframe):
    car_body= sorted(getUniqueBodyType()) # create a list variable using the column data from the getBodytype module
    
    columns = getDataColumns() # creare list variable to hold the returned list from the getDatPDDF module
    
    try:

        try:
            #The if and elif blocks below does the following for total_1 to total_5
            # assigns the sum of sales per car body type to the variable total_1 to total_5
            # The display function display the output of the computation as a data frame, we used the display function to format our output
            while True:
                bodychoice = tui.carBodyType()
                if bodychoice == 1:
                    total_1 = cardataframe.loc[cardataframe[columns[4]] == car_body[0]].price.sum()              
                    print('Total Sales Price for {} is ${:,}'.format(car_body[0].upper(),total_1))
                elif bodychoice == 2:
                    total_2 = cardataframe.loc[cardataframe[columns[4]] == car_body[1]].price.sum()              
                    print('Total Sales Price for {} is ${:,}'.format(car_body[1].upper(),total_2))
                elif bodychoice ==3:
                    total_3 = cardataframe.loc[cardataframe[columns[4]] == car_body[2]].price.sum()              
                    print('Total Sales Price for {} is ${:,}'.format(car_body[2].upper(),total_3))
                elif bodychoice ==4:
                    total_4 = cardataframe.loc[cardataframe[columns[4]] == car_body[3]].price.sum()              
                    print('Total Sales Price for {} is ${:,}'.format(car_body[3].upper(),total_4))
                elif bodychoice ==5:
                    total_5 = cardataframe.loc[cardataframe[columns[4]] == car_body[4]].price.sum()              
                    print('Total Sales Price for {} is ${:,}'.format(car_body[4].upper(),total_5))
                elif bodychoice ==0: 
                    break
                else:
                    print("Please enter a valid menu option")
        except BaseException as error:
            print("THe following error occured : {}".format(error))


    except BaseException as error:
        print("The following error ocurred: {}".format(error))


