import mysql.connector 

class MySQLDatabase: 

    def __init__(self, host, username, password, database): 
        self.connection = None 
        self.host = host 
        self.username = username 
        self.password = password
        self.database = database 
        
        
    def connect(self): 
        try:
            self.connection = mysql.connector.connect( 
                host=self.host,
                user=self.username,
                password=self.password,
                database=self.database

            )
            print("conexion exitosa a la base de datos")
            
        except mysql.connector.Error as error: 
            print(f"Error al conectar a la base de datos: {error}")
        
    def disconnect(self):
        if self.connection:
            self.connection.close()
            print("conexion cerrada")
        
        
    def excute_query(self, query, values=None):
        if self.connection:
            cursor = self.connection.cursor() 
            
            
            try:
                    if values: 
                        cursor.excute(query, values) 
                    else: 
                        cursor.excute(query)
                    results = cursor.fetchall()
                    self.connection.commit()
                    return results 
            
            except mysql.connector.Error as error: 
                print(f"Error al ejecturar la consulta")
            finally:
                cursor.close() 