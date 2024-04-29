import mysql.connector



mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="bcaty"
)

mycursor = mydb.cursor()

# Corrected the SQL statement with placeholders (%s for strings, %d for integers)
sql = "INSERT INTO conndemo(id,name,city) VALUES (%s,%s,%s)"

val = [
    ("1","yash","Ahemedabad"),
    ("2","Arpit","Baroda"),
    ("3","Rakesh","Naroda")
]

# Executed the query with the correct SQL statement
mycursor.executemany(sql,val)

# Commit the transaction
mydb.commit()

# Close the cursor and database connection
mycursor.close()
mydb.close()

print(mycursor.rowcount, "records inserted.")
