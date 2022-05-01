# import sqlite3 as sq

# conn = sq.connect('data.db')
# print ("Opened database successfully")

# conn.execute('''CREATE TABLE DATATABLE (IND INTEGER PRIMARY KEY AUTOINCREMENT, ID VARCHAR NOT NULL, DATA TEXT NOT NULL); ''')
# print ("Table created successfully")

# data = "hello World, This is love"
# id = "A3"
# conn.execute(" INSERT INTO DATATABLE(ID,DATA) VALUES(?,?)",(id,data))
# conn.commit()

# cursor = conn.execute(" SELECT DATA FROM DATATABLE WHERE ID='"+id+"'")
# print(cursor.fetchone()[0])

# cursor = conn.execute("SELECT ID FROM DATATABLE ORDER BY IND DESC LIMIT 1")
# print(cursor.fetchone()[0])


# conn.close()