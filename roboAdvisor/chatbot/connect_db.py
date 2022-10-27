#Script used
#Import SQLITE package
import sqlite3

#Create a connection to a database
con=sqlite3.connect("database.sqlite3")
#con.close()
#open cursor
cursor=con.cursor()
#Writing the query
query="select * from statement"
#query= "SELECT name FROM sqlite_schema WHERE type ='table' AND name NOT LIKE 'sqlite_%';"
#execute query
cursor.execute(query)
#fetch results
result=cursor.fetchall()
#view results

with open('database.txt', 'w') as output_file:
    for row in result:
        #print(str(row))
        output_file.write(str(row)+'\n')
#closing connection
con.close
 