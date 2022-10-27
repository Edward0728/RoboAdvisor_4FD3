#Script used
#Import SQLITE package
import sqlite3

#Create a connection to a database
con=sqlite3.connect("db.sqlite3")
#con.close()
#open cursor
cursor=con.cursor()
#Writing the query
query="Select * from statement"
#query= "SELECT name FROM sqlite_schema WHERE type ='table' AND name NOT LIKE 'sqlite_%';"
#execute query
cursor.execute(query)
#fetch results
result=cursor.fetchall()
#view results
for row in result:
  print(row)
#closing connection
con.close
 