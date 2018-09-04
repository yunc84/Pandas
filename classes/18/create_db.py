import sqlite3

with sqlite3.connect('spotify.db') as connection:

	c = connection.cursor()

	c.execute("""CREATE TABLE sgt_pepp_songs
		        (track_num INT,
		        name TEXT,
		        duration INT)
		        """)