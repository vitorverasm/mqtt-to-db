import json
import mysql.connector
from DatabaseManager import DatabaseManager

def temp_Data_Handler(jsonData):
	#Parse Data
	json_Dict = json.loads(jsonData)
	SensorID = json_Dict['Sensor']
	Data_and_Time = json_Dict['Date']
	Temperature = json_Dict['Value']

	#Push into DB Table
	dbObj = DatabaseManager()
	dbObj.add_del_update_db_record("insert into Temperature_Data (SensorID, Date_n_Time, Temperature) values (%s,%s,%s)",[SensorID, Data_and_Time, Temperature])
	del dbObj
	print "Inserted Temperature Data into Database."
	print ""

def solar_Data_Handler(jsonData):
	json_Dict = json.loads(jsonData)
	SensorID = json_Dict['Sensor']
	Data_and_Time = json_Dict['Date']
	Voltage = json_Dict['Value']

	dbObj = DatabaseManager()
	dbObj.add_del_update_db_record("insert into Solar_Data (SensorID, Date_n_Time, Voltage) values (%s,%s,%s)",[SensorID, Data_and_Time, Voltage])
	del dbObj
	print "Voltage generated data inserted into database."
	print ""

def light_Data_Handler(jsonData):
	#Parse Data
	json_Dict = json.loads(jsonData)
	SensorID = json_Dict['Sensor']
	Data_and_Time = json_Dict['Date']
	Temperature = json_Dict['Value']

	#Push into DB Table
	dbObj = DatabaseManager()
	dbObj.add_del_update_db_record("insert into Ligh_Data (SensorID, Date_n_Time, Light_incidence) values (%s,%s,%s)",[SensorID, Data_and_Time, Temperature])
	del dbObj
	print "Inserted light incidence data into Database."
	print ""


#===============================================================
# Funcao chamada para tratar a comunicacao mqtt->db
def sensor_Data_Handler(Topic, jsonData):
	#checa qual o topico
	if Topic == "mqtt/sensors/solar":
		solar_Data_Handler(jsonData)
	else:
		if Topic == "mqtt/sensors/temp":
			temp_Data_Handler(jsonData)
		else:
			light_Data_Handler(jsonData)
#===============================================================
