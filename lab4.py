import sqlite3
from sqlite3 import Error

connection = None
dbFile = "database.db"

try: 
    # Establish connection with SQLite database "database.db"
    connection = sqlite3.connect(dbFile, isolation_level=None, detect_types=sqlite3.PARSE_COLNAMES)
    
    # Enables SQLite commands
    cursor = connection.cursor()

    # TripOffering ( TripNumber, Date, ScheduledStartTime, SecheduledArrivalTime,                                                                                                      
    # DriverName, BusID)
    # Bus ( BusID, Model,Year)
    # Driver( DriverName,  DriverTelephoneNumber)
    # Stop (StopNumber, StopAddress)
    # ActualTripStopInfo (TripNumber, Date, ScheduledStartTime, StopNumber, 
    # SecheduledArrivalTime, ActualStartTime, ActualArrivalTime, NumberOfPassengerIn, 
    # NumberOf PassengerOut)
    # TripStopInfo ( TripNumber, StopNumber, SequenceNumber, DrivingTime)

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
        
    # # Question 2
    
    # # Question 3 
    # for row in cursor.execute(''''''):
    #     print(row)
    
    # Question 4
    # driverName = input("Please enter driver name:")
    # date = input("Please enter the date the driver is supposed to drive:")
    # for row in cursor.execute('''SELECT * FROM TripOffering WHERE DriverName = "%s" AND Date = "%s" ''' % (driverName, date)):
    #     print(row)
    
    # Question 5
except Error as e: 
    print(e)