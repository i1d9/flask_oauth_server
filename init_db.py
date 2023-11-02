import os
import psycopg2

conn = psycopg2.connect(
    host=os.environ['HOST'],
    database=os.environ['DB'],
    user=os.environ['DB_USERNAME'],
    password=os.environ['DB_PASSWORD'])

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a command: this creates a new table
cur.execute('DROP TABLE IF EXISTS client;')
cur.execute('CREATE TABLE client (id serial PRIMARY KEY,'
            'secret varchar (150) NOT NULL,'
            'name varchar (50) NOT NULL,'
            'scopes integer NOT NULL,'
            'review text,'
            'inserted_at date DEFAULT CURRENT_TIMESTAMP);',
            'updated_at date DEFAULT CURRENT_TIMESTAMP);'
            )

# Insert data into the table

cur.execute('INSERT INTO books (title, author, pages_num, review)'
            'VALUES (%s, %s, %s, %s)',
            ('A Tale of Two Cities',
             'Charles Dickens',
             489,
             'A great classic!')
            )


cur.execute('INSERT INTO books (title, author, pages_num, review)'
            'VALUES (%s, %s, %s, %s)',
            ('Anna Karenina',
             'Leo Tolstoy',
             864,
             'Another great classic!')
            )

conn.commit()

cur.close()
conn.close()
