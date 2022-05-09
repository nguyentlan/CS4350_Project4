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

    # SQL Command to Create Tables
    tripTable = """ CREATE TABLE IF NOT EXISTS Trip(TripNumber TEXT, StartLocationName TEXT, DestinationName TEXT) """
    
    tripOfferingTable = """ CREATE TABLE IF NOT EXISTS TripOffering(TripNumber TEXT PRIMARY KEY, Date TEXT PRIMARY KEY, 
                            ScheduledStartTime TEXT, ScheduledArrivalTime TEXT, DriverName TEXT, BUSID TEXT)"""
    
    busTable = """ CREATE TABLE IF NOT EXISTS Bus(BusID TEXT PRIMARY KEY, Plate TEXT, Year TEXT, Make TEXT)"""
    
    driverTable = """ CREATE TABLE IF NOT EXISTS Driver(DriverName TEXT PRIMARY KEY, DriverTelephoneNumber TEXT)"""
    
    stopTable = """ CREATE TABLE IF NOT EXISTS Stop(StopNumber TEXT, StopAddress TEXT)"""
    
    actualTripStopInfoTable = """ CREATE TABLE IF NOT EXISTS ActualTripStopInfo(TripNumber TEXT, Date TEXT, ScheduledStartTime
                                  TEXT, StopNumber TEXT, SecheduledArrivalTime TEXT, ActualStartTime TEXT, ActualArrivalTime TEXT, 
                                  NumberOfPassengerIn TEXT, NumberOfPassengerOut TEXT)"""
    
    tripStopInfo = """ CREATE TABLE IF NOT EXISTS TripStopInfo(TripNumber TEXT, StopNumber TEXT, SequenceNumber TEXT, 
                       DrivingTime TEXT)"""
    
    # Creating the tables
    cursor.execute(busTable)

    connection.commit()
    #connection.close()

except Error as e: 
    print(e)