from getDatPDDF import getCarasPDDF


#The method below selects columns of interest for our visual analysis
def getColumnsofInterest():
    carData = getCarasPDDF()
    try:
        # create a dataframe for analysis, with specified columns listed below
        df4_analysis = carData[['doornumber','fueltype','drivewheel','horsepower','price','carbody']]
        return df4_analysis
    except BaseException as error:
        print("The following error occured: {}".format(error))

#Chart to compare total sales of cars, sales are dependent on the door number (2/4 doors) - Infer Cars with 4 doors sells more, this may be due to family cars
def getBarChartofMostSalesbyDoor():
    try:
        # Get DF with Columns of the sum of Door Types and Total price of cars under each door type category
        chartbydoorsales = getColumnsofInterest().groupby('doornumber').sum().drop(columns='horsepower').reset_index()
        return chartbydoorsales
        
    except BaseException as error:
        print("The following error occured: {}".format(error))