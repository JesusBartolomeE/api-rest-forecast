import sqlite3 

class DB:

    def sqlite_connection(self):
        try:
            con = sqlite3.connect('TEMPERATURE.db')
        except sqlite3.OperationalError:
            print('Error')
        return con

    def create_temperature_table(self):
        con = self.sqlite_connection() 
        cur = con.cursor()
        try: 
            cur.execute('''CREATE TABLE IF NOT EXISTS FORECAST (
                            ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,    
                            USER_NAME TEXT NOT NULL, 
                            LOCATION TEXT NOT NULL,
                            FORECAST TEXT NOT NULL,
                            TEMP TEXT NOT NULL,
                            DATE DATE) 
                        ''')
            con.commit()  
            print()
        except sqlite3.OperationalError:
            print('La tabla ya existe')
            
    def insert_values_forecast(self,values):
        self.create_temperature_table()
        con = self.sqlite_connection() 
        cur = con.cursor()
        try:
            cur.execute(
                """INSERT INTO FORECAST VALUES( 
                    NULL , ? , ?, ? , ? , CURRENT_DATE)""",(values[0],values[1],values[2],values[3])
            )
            con.commit()
            print('Datos insertados en la base de datos correctamente')
            return True
        except Exception as e:
            print(e)  
            con.close()
            return False

    def get_information(self, query):
        con = self.sqlite_connection() 
        cur = con.cursor()
        try:
            cur.execute(query)
            row = cur.fetchall()
            name_columns = [value[0] for value in cur.description]
            con.close()
            return row, name_columns
        except Exception as e:
            print(e)
            return True