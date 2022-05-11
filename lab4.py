import sqlite3
from sqlite3 import Error

connection = None
dbFile = "database.db"

try: 
    # Establish connection with SQLite database "database.db"
    connection = sqlite3.connect(dbFile, isolation_level=None, detect_types=sqlite3.PARSE_COLNAMES)
    
    # Enables SQLite commands
    cursor = connection.cursor()

    tripTable = """ CREATE TABLE IF NOT EXISTS Trip(TripNumber TEXT PRIMARY KEY, StartLocationName TEXT, DestinationName TEXT) """
    
    tripOfferingTable = """ CREATE TABLE IF NOT EXISTS TripOffering(TripNumber TEXT, Date TEXT, 
                            ScheduledStartTime TEXT, ScheduledArrivalTime TEXT, DriverName TEXT, BusID TEXT,
                            PRIMARY KEY(TripNumber, Date, ScheduledStartTime),
                            FOREIGN KEY(BusID) REFERENCES Bus(BusID), FOREIGN KEY(TripNumber) REFERENCES Trip(TripNumber),
                            FOREIGN KEY(DriverName) REFERENCES Driver(DriverName))"""
    
    busTable = """ CREATE TABLE IF NOT EXISTS Bus(BusID TEXT PRIMARY KEY, Plate TEXT, Year TEXT, Make TEXT)"""
    
    driverTable = """ CREATE TABLE IF NOT EXISTS Driver(DriverName TEXT PRIMARY KEY, DriverTelephoneNumber TEXT)"""
    
    stopTable = """ CREATE TABLE IF NOT EXISTS Stop(StopNumber TEXT PRIMARY KEY, StopAddress TEXT)"""
    
    actualTripStopInfoTable = """ CREATE TABLE IF NOT EXISTS ActualTripStopInfo(TripNumber TEXT, Date TEXT, ScheduledStartTime
                                  TEXT, StopNumber TEXT, SecheduledArrivalTime TEXT, ActualStartTime TEXT, ActualArrivalTime TEXT, 
                                  NumberOfPassengerIn TEXT, NumberOfPassengerOut TEXT,
                                  PRIMARY KEY(StopNumber, Date, ScheduledStartTime, TripNumber),
                                  FOREIGN KEY(StopNumber) REFERENCES Stop(StopNumber), FOREIGN KEY(Date, ScheduledStartTime, 
                                  TripNumber) REFERENCES 
                                  TripOffering(Date, ScheduledStartTime, 
                                  TripNumber))"""
    

    tripStopInfo = """ CREATE TABLE IF NOT EXISTS TripStopInfo(TripNumber TEXT, StopNumber TEXT, SequenceNumber TEXT, 
                       DrivingTime TEXT,
                       PRIMARY KEY(StopNumber, TripNumber),
                       FOREIGN KEY(TripNumber) REFERENCES Trip(TripNumber), FOREIGN KEY(StopNumber) REFERENCES
                       Stop(StopNumber))"""
    
    # Creating the tables
    # cursor.execute(tripTable)
    # cursor.execute(busTable)
    # cursor.execute(driverTable)
    # cursor.execute(stopTable)
    # cursor.execute(tripOfferingTable)
    # cursor.execute(actualTripStopInfoTable)
    # cursor.execute(tripStopInfo)

    connection.commit()
    #connection.close()

    cursor.execute

    menu = False

    while menu is True:

        menuChoice = input("""Please choose an option from the menu
                <1>  Question 1 
                <2>  Question 2 
                <3>  Question 3 
                <4>  Question 4 
                <5>  Question 5 
                <6>  Question 6 
                <7>  Question 7 
                <8>  Question 8 
                <9>  Quit \n""")

        if menuChoice == '1':
            print("Display the schedule of all trips given dt")
            StartLocationName = input('Please enter a Start Location Name: ')
            DestinationName = input('Please enter a Destination Name: ')
            Date = input('Please enter a Date:')
            for row in cursor.execute('''   SELECT 
                                            t.StartLocationName, t.DestinationName, f.Date, f.ScheduledStartTime, f.ScheduledArrivalTime, f.DriverName, f.BusID 
                                            FROM 
                                            Trip t, TripOffering f 
                                            WHERE 
                                            t.TripNumber = f.TripNumber AND t.StartLocationName = "%s" AND t.DestinationName = "%s" AND f.Date = "%s"
                                      ''' % (StartLocationName, DestinationName, Date)):
                print(row)

        if menuChoice == '2':
            question2 = True

            while question2 is True:
                question2Choice = input("""Please choose an option from the menu
                <1>  Delete a Trip Offering
                <2>  Add a Trip Offering
                <3>  Change the Driver of a Trip Offering
                <4>  Change the Bus of a Trip Offering
                <5>  Quit\n""")

                if question2Choice == '1':
                    tripNumber = input('Please specify the Trip Number: ')
                    dateNumber = input("Please input the Trip's Date: ")
                    scheduledStartTime = input("Please input the Trip's Starting Time: ")

                    print("Here is the old version of the table: ")
                    for row in cursor.execute(''' SELECT * FROM TripOffering'''):
                        print(row)

                    cursor.execute(''' DELETE FROM TripOffering WHERE
                                TripNumber = "%s" AND Date = "%s" AND ScheduledStartTime = "%s" ''' 
                                % (tripNumber, dateNumber, scheduledStartTime))

                    print("Here is the updated version of the table: ")
                    for row in cursor.execute(''' SELECT * FROM TripOffering'''):
                        print(row)

                    userChoice = input("Would you like to continue with Question 2? (Y/N)")
                    if userChoice == "Y":
                        question2 = True
                    if userChoice == "N":
                        question2 = False

                if question2Choice == '2':
                    tripNumber = input("Please specify the Trip Number: ")
                    dateNumber = input("Please input the Trip's Date: ")
                    scheduledStartTime = input("Please input the Trip's Starting Time: ")
                    scheduledArrivalTime = input("Please input the Trip's Arrival Time: ")
                    driverName = input("Please input the Trip's Driver Name: ")
                    busID = input("Please input the Trip's busID: ")
                    
                    print("Here is the old version of the table: ")
                    for row in cursor.execute(''' SELECT * FROM TripOffering'''):
                        print(row)
                    
                    cursor.execute('''INSERT INTO TripOffering(TripNumber, Date, ScheduledStartTime, ScheduledArrivalTime,
                                DriverName, BusID) VALUES("%s","%s","%s","%s","%s", "%s")'''
                                % (tripNumber, dateNumber, scheduledStartTime, scheduledArrivalTime, driverName, busID))
                    
                    print("Here is the updated version of the table: ")
                    for row in cursor.execute(''' SELECT * FROM TripOffering'''):
                        print(row)
                    
                    userChoice = input("Would you like to continue with Question 2? (Y/N)")
                    if userChoice == "Y":
                        question2 = True
                    if userChoice == "N":
                        question2 = False

                if question2Choice == '3':
                    tripNumber = input('Please specify the Trip Number: ')
                    dateNumber = input("Please input the Trip's Date: ")
                    scheduledStartTime = input("Please input the Trip's Starting Time: ")
                    driverName = input("Please input the Driver Change for this Trip: ")

                    print("Here is the old version of the table: ")
                    for row in cursor.execute(''' SELECT * FROM TripOffering'''):
                        print(row)

                    cursor.execute('''UPDATE TripOffering SET DriverName = "%s" WHERE TripNumber = "%s" AND
                                Date = "%s" AND ScheduledStartTime = "%s"''' % (driverName, tripNumber, dateNumber, 
                                scheduledStartTime))

                    print("Here is the updated version of the table: ")
                    for row in cursor.execute(''' SELECT * FROM TripOffering'''):
                        print(row)

                    userChoice = input("Would you like to continue with Question 2? (Y/N)")
                    if userChoice == "Y":
                        question2 = True
                    if userChoice == "N":
                        question2 = False
                    
                if question2Choice == '4':
                    tripNumber = input('Please specify the Trip Number: ')
                    dateNumber = input("Please input the Trip's Date: ")
                    scheduledStartTime = input("Please input the Trip's Starting Time: ")
                    busID = input("Please input the Bus ID Change for this Trip: ")

                    print("Here is the old version of the table: ")
                    for row in cursor.execute(''' SELECT * FROM TripOffering'''):
                        print(row)

                    cursor.execute('''UPDATE TripOffering SET busID = "%s" WHERE TripNumber = "%s" AND
                                Date = "%s" AND ScheduledStartTime = "%s"''' % (busID, tripNumber, dateNumber, 
                                scheduledStartTime))

                    print("Here is the updated version of the table: ")
                    for row in cursor.execute(''' SELECT * FROM TripOffering'''):
                        print(row)

                if question2Choice == '5':
                    question2 = False
        if menuChoice == '3':
            print("Display the stops of a given trip")
            Trip = input('Enter a trip: ')
            for row in cursor.execute('''   SELECT
                                            t.StopNumber
                                            FROM
                                            TripStopInfo t
                                            WHERE
                                            t.TripNumber = "%s"
                                        ''' % (Trip)):
                print(row)


        if menuChoice == '4':
            print("Display the weekly schedule of a given driver and date")
            driverName = input("Please enter driver name:")
            date = input("Please enter the date the driver is supposed to drive:")
            for row in cursor.execute('''SELECT * FROM TripOffering WHERE DriverName = "%s" AND Date = "%s" ''' % (driverName, date)):
                print(row)

        if menuChoice == '5':
            print("Add a driver")
            driverName = input("Please enter the driver name you would like to add:")
            driverTelephone = input("Enter the phone number:")
            print("Here is the old version of the table")
            for row in cursor.execute(''' SELECT * FROM Driver'''):
                print(row)
            for row in cursor.execute('''INSERT INTO Driver(DriverName, DriverTelephoneNumber) VALUES("%s", "%s")''' % (driverName, driverTelephone)):
                print(row)

            print("Here is the updated version of the table")
            for row in cursor.execute(''' SELECT * FROM Driver'''):
                print(row)

        if menuChoice == '6':
            print("Add a Bus")
            busID = input("Please enter the new BusID:")
            busPlate = input("Please enter the bus plate:")
            busYear = input("Please enter the year:")
            busMake = input("Please enter the make:")
            print("Here is the old version of the table")
            for row in cursor.execute(''' SELECT * FROM Bus'''):
                print(row)
            cursor.execute('''INSERT INTO Bus(BusID, Plate, Year, Make) VALUES("%s", "%s", "%s", "%s")''' % (busID, busPlate, busYear, busMake))
            print("Here is the updated table")
            for row in cursor.execute('''SELECT * FROM Bus'''):
                print(row)

        if menuChoice == '7':
            print("Delete a BusID")
            BusID = input('Enter a BusID: ')
            print('Here is your old table: ')
            for row in cursor.execute(''' SELECT *
                                        FROM Bus
            '''):
                print(row)
            cursor.execute(''' DELETE FROM
                                        Bus
                                        WHERE
                                        BusID = "%s"
            ''' % (BusID))
            print('BusID has been deleted, here is your new Bus Table: ')
            for row in cursor.execute(''' SELECT *
                                        FROM Bus
            '''):
                print(row)

        # if menuChoice == '8':

        if menuChoice == '9':
            menu = False
except Error as e: 
    print(e)