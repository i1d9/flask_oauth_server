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
cur.execute('DROP TABLE IF EXISTS clients;')
cur.execute('CREATE TABLE clients (id varchar PRIMARY KEY,'
            'secret varchar (255) NOT NULL,'
            'name varchar (255) NOT NULL,'
            'scopes VARCHAR[] NOT NULL,'       
            'inserted_at date DEFAULT CURRENT_TIMESTAMP);',
            'updated_at date DEFAULT CURRENT_TIMESTAMP);'
            )

# Insert data into the table
cur.execute('INSERT INTO clients (id, name, secret, scopes)'
            'VALUES (%s, %s, %s, %s)',
            ('client_id',
             'client_name',
             'client_secret',
             '{"Joe", "Root"}'
            ))



conn.commit()

cur.close()
conn.close()
