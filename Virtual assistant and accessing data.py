import sqlite3
#connection to the databese, single file
conn = sqlite3.connect('hotels.db')
#in order to actually run queries, we need to create a cursor using this connection
c = conn.cursor()
#by calling connection dot cursor we can execute queries by passing a string c.execute() method
c.execute( "SELECT * FROM hotels WHERE area =  'south' and pricerange = 'hi' ")
#after that, we can get the results from the cursor object, using the cursor's fetchall method, this returns a list of tuples.
c.fetchall()

#result
[( 'Grand Hotel', 'hi', 'south', 5)]

#exercise 
import sqlite3
c = conn.cursor()
c.execute (Select name from hotels where price = 'mid' AND area = 'north')
c.fetchall


#exercise2
# Import sqlite3
import sqlite3

# Open connection to DB
conn = sqlite3.connect('hotels.db')

# Create a cursor
c = conn.cursor()

# Define area and price
area, price = "south", "hi"
t = (area, price)

# Execute the query
c.execute("SELECT * FROM hotels WHERE area= 'south' AND price= 'hi' ")

# Print the results
print(c.fetchall())
