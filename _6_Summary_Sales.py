
from getBodytype import getUniqueBodyType
from getDatPDDF import getCarasPDDF
from getDatPDDF import getDataColumns
from IPython.display import display
import pandas as pd
import tui

#The bodychoice varaible in the method
# allows the user enter an int value to view cars under diffrent body type as was retrieved from getCarasPDDF function from the getDatPDDF module
def getSalesSummary(cardataframe):
    car_body= sorted(getUniqueBodyType()) # create a list variable using the column data from the getBodytype module
    #cardataframe=getCarasPDDF() # retrieve processed data frame from the getDatPDDF moudle
    columns = getDataColumns() # creare list variable to hold the returned list from the getDatPDDF module
    
    try:
        # get input from the 
        #bodychoice = int(input("Enter 1 for {} \n, Enter 2 for {} \n, Enter 3 for {} \n, Enter 4 for {} \n, Enter 5 for {} \n".format(car_body[0],car_body[1],car_body[2],car_body[3],car_body[4])))
        
        
        try:
            #The if and elif blocks below does the following for total_1 to total_5
            # assigns the sum of sales per car body type to the variable total_1 to total_5
            # The display function display the output of the computation as a data frame, we used the display function to format our output
            while True:
                bodychoice = tui.carBodyType()
                if bodychoice == 1:
                    total_1 = cardataframe.loc[cardataframe[columns[4]] == car_body[0]].price.sum()              
                    display(pd.DataFrame({'Total Sales Price for {}'.format(car_body[0].upper()):[total_1]}).style.hide_index())
                elif bodychoice == 2:
                    total_2 = cardataframe.loc[cardataframe[columns[4]] == car_body[1]].price.sum()              
                    display(pd.DataFrame({'Total Sales Price for {}'.format(car_body[1].upper()):[total_2]}).style.hide_index())
                elif bodychoice ==3:
                    total_3 = cardataframe.loc[cardataframe[columns[4]] == car_body[2]].price.sum()              
                    display(pd.DataFrame({'Total Sales Price for {}'.format(car_body[2].upper()):[total_3]}).style.hide_index())
                elif bodychoice ==4:
                    total_4 = cardataframe.loc[cardataframe[columns[4]] == car_body[3]].price.sum()              
                    display(pd.DataFrame({'Total Sales Price for {}'.format(car_body[3].upper()):[total_4]}).style.hide_index())
                elif bodychoice ==5:
                    total_5 = cardataframe.loc[cardataframe[columns[4]] == car_body[4]].price.sum()              
                    display(pd.DataFrame({'Total Sales Price for {}'.format(car_body[4].upper()):[total_5]}).style.hide_index())
                elif bodychoice ==0: 
                    break
                else:
                    print("Please enter a valid menu option")
        except BaseException as error:
            print("THe following error occured : {}".format(error))


    except BaseException as error:
        print("The following error ocurred: {}".format(error))

if __name__ =='__main__':
    getSalesSummary()
