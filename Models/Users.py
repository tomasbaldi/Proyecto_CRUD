#import hashlib
#h = hashlib.new("sha256", b"cadena")
#print(h.digest())

class Users():
    
    def __init__(self, db_connection):
        
        try:
            self.db_connection = db_connection
            self.db_cursor = db_connection.cursor()
            self.db_cursor.execute("""CREATE TABLE users (
                                                        user TEXT NOT NULL PRIMARY KEY UNIQUE,
                                                        password TEXT NOT NULL
                                    )""")
            self.db_connection.commit()
            self.db_connection.close()
            print("users table created successfully")
        
        except:
            pass

    def getUser(self, user, password):
        user1 = [user]
        password1 = [password]
        self.db_cursor.execute("SELECT * FROM users WHERE user = ? AND password = ?", user1 + password1)
        result = self.db_cursor.fetchall()
        
        return result