import sqlite3
#connection to the databese, single file
conn = sqlite3.connect('hotels.db')


SELECT name from restaurants WHERE area = 'center' AND pricerange = 'hi'
