import mysql.connector
from mysql.connector import errorcode


class DatabaseManager():
	def __init__(self):
		self.cnx = mysql.connector.connect(option_files='./db.cnf', buffered=True, connection_timeout=300)
		self.cursor = self.cnx.cursor()
	def add_del_update_db_record(self, sql_query, args=()):
		self.cursor.execute(sql_query, args)
		self.cnx.commit()
		return

	def __del__(self):
		self.cursor.close()
		self.cnx.close()

    #Inicia/zera as tabelas
	def init_tables(self):
		self.cursor.execute("DROP TABLE IF EXISTS `Temperature_Data`;")
		self.cursor.execute("DROP TABLE IF EXISTS `Solar_Data`;")
		self.cursor.execute("DROP TABLE IF EXISTS `Ligh_Data`;")
		self.cursor.execute("CREATE TABLE `Temperature_Data`(`id` INT PRIMARY KEY AUTO_INCREMENT,`SensorID` TEXT,`Date_n_Time` TEXT,`Temperature` TEXT);")
		self.cursor.execute("CREATE TABLE `Solar_Data`(`id` INT PRIMARY KEY AUTO_INCREMENT,`SensorID` TEXT,`Date_n_Time` TEXT,`Voltage` TEXT);")
		self.cursor.execute("CREATE TABLE `Ligh_Data`(`id` INT PRIMARY KEY AUTO_INCREMENT,`SensorID` TEXT,`Date_n_Time` TEXT,`Light_incidence` TEXT);")
		self.cnx.commit()
		self.cursor.close()
