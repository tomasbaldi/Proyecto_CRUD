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
            print('users table already exist')