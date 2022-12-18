line_width = 70
def startModule(msg):
    output="{}".format(msg)
    print("-"*line_width)
    print(output)

def completed(msg):
    print("{}".format(msg))
    print("-"*line_width)

def programmenu():
    print("\n")
    print(f"""Please select one of the following options:
    {"[1]":<10} List Car by ID
    {"[2]":<10} List Car by Cylinder Number
    {"[3]":<10} List Car by Specific Body Type
    {"[4]":<10} List Car Specific Car Columns Based on your Preffered Column Features
    {"[5]":<10} List Car Names in Alphabetical Order
    {"[6]":<10} List Summary of Sales for each Car Body
    {"[7]":<10} List Top 5 Selling Cars by Price
    {"[8]":<10} List Car Details by User Selection"
    {"[0]":<10} Exit

    """)
    print("\n")
    myselection = int(input("Your selection is option: "))
    return myselection


def carBodyType():
    #['convertible', 'hardtop', 'hatchback', 'sedan', 'wagon']
    print("\n")
    print(f"""Please select one of the following options to view details for a specific body type:
    {"[1]":<10} for Convertible
    {"[2]":<10} for Hardtop
    {"[3]":<10} for Hatchback
    {"[4]":<10} for Sedan
    {"[5]":<10} for Wagon
    {"[0]":<10} Quit
    """)
    print("\n")
    carbodyselection = int(input(" Enter your option: "))
    return carbodyselection

def carCylinder():
    print("\n")
    print(f"""Please select one of the following options to view cars the listed Engine Cylinder types:
    {"[1]":<10} 2 Cylinders
    {"[2]":<10} 3 Cylinders
    {"[3]":<10} 4 Cylinders
    {"[4]":<10} 5 Cylinders
    {"[5]":<10} 6 Cylinders
    {"[6]":<10} 8 Cylinders
    {"[7]":<10} 12 Cylinders
    {"[0]":<10} Quit
    """)
    print("\n")
    car_cylinder = int(input(" Enter your option: "))
    return car_cylinder

def uniqueColumnData():
    print("\n")
    print(f"""Please select one of the following options to view cars the listed Engine Cylinder types:
    {"[1]":<10} Enter option 1 to see car_ID column in your feature set
    {"[2]":<10} Enter option 2 to see CarName column in your feature set
    {"[3]":<10} Enter option 3 to see fueltype column in your feature set
    {"[4]":<10} Enter option 4 to see doornumber column in your feature set
    {"[5]":<10} Enter option 5 to see carbody column in your feature set
    {"[6]":<10} Enter option 6 to see drivewheel column in your feature set
    {"[7]":<10} Enter option 7 to see enginelocation column in your feature set
    {"[8]":<10} Enter option 8 to see wheelbase column in your feature set
    {"[9]":<10} Enter option 9 to see carlength column in your feature set
    {"[10]":<10} Enter option 10 to see carwidth column in your feature set
    {"[11]":<10} Enter option 11 to see carheight column in your feature set
    {"[12]":<10} Enter option 12 to see curbweight column in your feature set
    {"[13]":<10} Enter option 13 to see enginetype column in your feature set
    {"[14]":<10} Enter option 14 to see cylindernumber column in your feature set
    {"[15]":<10} Enter option 15 to see enginesize column in your feature set
    {"[16]":<10} Enter option 16 to see fuelsystem column in your feature set
    {"[17]":<10} Enter option 17 to see horsepower column in your feature set
    {"[18]":<10} Enter option 18 to see citympg column in your feature set
    {"[19]":<10} Enter option 19 to see highwaympg column in your feature set
    {"[20]":<10} Enter option 20 to see price column in your feature set
    """)
    print("\n")
    column_options = int(input("Column Options: "))
    return column_options
    
    
def uniqueColumnDataChoice():
    print("\n")
    print(f"""Please select one of the following options to view cars the listed Engine Cylinder types:
    {"[1]":<10} Enter option 1 to see car_ID column in your feature set
    {"[2]":<10} Enter option 2 to see CarName column in your feature set
    {"[3]":<10} Enter option 3 to see fueltype column in your feature set
    {"[4]":<10} Enter option 4 to see doornumber column in your feature set
    {"[5]":<10} Enter option 5 to see carbody column in your feature set
    {"[6]":<10} Enter option 6 to see drivewheel column in your feature set
    {"[7]":<10} Enter option 7 to see enginelocation column in your feature set
    {"[8]":<10} Enter option 8 to see wheelbase column in your feature set
    {"[9]":<10} Enter option 9 to see carlength column in your feature set
    {"[10]":<10} Enter option 10 to see carwidth column in your feature set
    {"[11]":<10} Enter option 11 to see carheight column in your feature set
    {"[12]":<10} Enter option 12 to see curbweight column in your feature set
    {"[13]":<10} Enter option 13 to see enginetype column in your feature set
    {"[14]":<10} Enter option 14 to see cylindernumber column in your feature set
    {"[15]":<10} Enter option 15 to see enginesize column in your feature set
    {"[16]":<10} Enter option 16 to see fuelsystem column in your feature set
    {"[17]":<10} Enter option 17 to see horsepower column in your feature set
    {"[18]":<10} Enter option 18 to see citympg column in your feature set
    {"[19]":<10} Enter option 19 to see highwaympg column in your feature set
    {"[20]":<10} Enter option 20 to see price column in your feature set
    {"[0]":<10} Quit
    """)
    print("\n")
    column_options = int(input("Column Options: "))
    return column_options





