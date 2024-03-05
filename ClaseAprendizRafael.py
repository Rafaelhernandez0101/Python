class Aprendiz: 
    def __init__ (self, id, name, surfname, phone, mail, clas): 
        self.id = id
        self.name = name 
        self.surfname = surfname
        self.phone = phone 
        self.mail = mail 
        self.clas = clas 
        
        
    def insert_into_db(self, db): 
        
        query = "INSERT INTO aprendices (id, name, surfname, phone, mail, clas) VALUES (%s,%s,%s,%s,%s,%s)"
        values = (self.id, self.name, self.surfname, self.phone, self.mail, self.clas)
        db.excute_query(query, values)
        db.connection.commit()
        
        
    @staticmethod
    def select_all_from_db(db):
        query = "SELECT * FROM aprendices"
        results = db.excute_query(query)
        return results

    def print_datos(self): 
        data = { 
            "id": self.id,
            "name": self.name,
            "surfname": self.surfname,
            "phone": self.phone,
            "mail": self.mail,
            "clas": self.clas
        }
        return data         