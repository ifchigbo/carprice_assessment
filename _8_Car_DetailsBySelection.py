#QUESTION 2D
from getDatPDDF import getCarasPDDF, getDataColumns
from sys import exit
from IPython.display import display
import tui
#cardata = getCarasPDDF()
dfcolumns = getDataColumns()

def getSpecColumnsbyCarID(cardata):
    # The code below below handles two scenarios
    # a user who wants to see all the detail of cars
    # or a user wants to see the detail of cars based on the users selection
    try:
        view_feature_list = [] # collect a set of features to view
        collected_feature_list = [] # get the column name of the selected features
        view_option = int(input("Please select 1 to see all details \n, Select 2 to see specific details \n"))
        print("\n")
        if view_option == 1:
            display(cardata)
        elif view_option == 2:
            ###### List the feature avaialable from the column data set ####
            col_count = 0
            while col_count < len(dfcolumns):
                print("Enter option {} to see {} column in your feature set ".format(col_count+1,dfcolumns[col_count] ))
                print("\n")
                col_count +=1
            ###### end of code block for feature menu view #########
            truth_table = True #condition that enables the user enter as much features as possible
            
            ### code block collects the index of feature details we want to view ####
            while truth_table:
                # The detailsl variable collects the desired number of columns the user is interested in displaying
                #details = input("Enter the columns you want to see, enter 'q' to quit when you are satistfied with your choice of selection")
                details = tui.uniqueColumnDataChoice()
                if details not in view_feature_list and details !=0:  #'q'
                    view_feature_list.append(int(details) -1) # index starts from orignal value - one (1) - because list index startf rom zero
                else:
                    truth_table = False
                    break
            ### End of code block for feature collection ####

            ## get the Column names for the feature details and append to collected feature list #####
            for features in range(len(dfcolumns)):
                if features in view_feature_list:
                    collected_feature_list.append(dfcolumns[features])

            #display the results based on the feature details the user has selected to view
            display(cardata[collected_feature_list])
            
        else:
            print("Please select a valid option")
    except BaseException as error:
        print("The following error has occured: {}".format(error))
        

