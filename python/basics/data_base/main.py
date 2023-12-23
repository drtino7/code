import sqlite3
import getpass

def main(): 
    
    def login():
        username=input("type your username: ")
        password=getpass.getpass("type your password: ")
        conn = sqlite3.connect('data_base/sqlite.db',isolation_level=None)#isolation_level=None
        cursor=conn.cursor()
        
        rows = cursor.execute(f"SELECT id FROM user WHERE username='{username}' AND password='{password}'")
        
        data = rows.fetchone()
        
        cursor.close()
        conn.close()
      
        if(data == None):
         return False
        return True
    
    def singup(username,password):
        username=input("type your username: ")
        password=getpass.getpass("type your password: ")
        #"DELETE FROM user WHERE id=4" 
        conn = sqlite3.connect('data_base/sqlite.db',isolation_level=None)
        cursor = conn.cursor()
      
        rows = cursor.execute(f"SELECT id FROM user WHERE username='{username}'")
        data=rows.fetchone()

        if(data == None):
            query = f"INSERT INTO user(id,username,password) VALUES('7','{username}','{password}');"
            rows=cursor.execute(query)
        else:
            print("the user is already registered")
    
        cursor.close()
        conn.close()


if(__name__ == "__main__"):
    main()