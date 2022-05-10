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

    # Question 1
    # StartLocationName = input('Please enter a Start Location Name: ')
    # DestinationName = input('Please enter a Destination Name: ')
    # Date = input('Please enter a Date:')
    # for row in cursor.execute('''   SELECT 
    #                                 t.StartLocationName, t.DestinationName, f.Date, f.ScheduledStartTime, f.ScheduledArrivalTime, f.DriverName, f.BusID 
    #                                 FROM 
    #                                 Trip t, TripOffering f 
    #                                 WHERE 
    #                                 t.TripNumber = f.TripNumber AND t.StartLocationName = "%s" AND t.DestinationName = "%s" AND f.Date = "%s"
    #                           ''' % (StartLocationName, DestinationName, Date)):
    #     print(row)
        
    # # Question 2
    
    # # Question 3 
    # Trip = input('Enter a trip: ')
    # for row in cursor.execute('''   SELECT
    #                                 t.StopNumber
    #                                 FROM
    #                                 TripStopInfo t
    #                                 WHERE
    #                                 t.TripNumber = "%s"
    #                           ''' % (Trip)):
    #     print(row)
    
    # Done
    # Question 4
    # driverName = input("Please enter driver name:")
    # date = input("Please enter the date the driver is supposed to drive:")
    # for row in cursor.execute('''SELECT * FROM TripOffering WHERE DriverName = "%s" AND Date = "%s" ''' % (driverName, date)):
    #     print(row)

    # Done 
    # # Question 5
    # driverName = input("Please enter the driver name you would like to add:")
    # driverTelephone = input("Enter the phone number:")
    # for row in cursor.execute('''INSERT INTO Driver(DriverName, DriverTelephoneNumber) VALUES("%s", "%s")''' % (driverName, driverTelephone)):
    #     print(row)
    
    # Question 6
    # busID = input("Please enter the new BusID:")
    # busPlate = input("Please enter the bus plate:")
    # busYear = input("Please enter the year:")
    # busMake = input("Please enter the make:")
    # cursor.execute('''INSERT INTO Bus(BusID, Plate, Year, Make) VALUES("%s", "%s", "%s", "%s")''' % (busID, busPlate, busYear, busMake))

    # for row in cursor.execute('''SELECT * FROM Bus'''):
    #     print(row)

    # Question 7
    BusID = input('Enter a BusID to delete: ')
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
except Error as e: 
    print(e)