import sqlite3

# Connect to sqlite
connection = sqlite3.connect("student.db")

# Create a cursor obj to insert record, create table
cursor = connection.cursor()

# Create the table
table_info = """Create table STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25), SECTION VARCHAR(25));"""

cursor.execute(table_info)

# Insert few more records

cursor.execute('''Insert Into STUDENT values('Vikash', 'MLOps', 'A')''')
cursor.execute('''Insert Into STUDENT values('Peter', 'MLOps', 'B')''')
cursor.execute('''Insert Into STUDENT values('Tony', 'AI', 'A')''')
cursor.execute('''Insert Into STUDENT values('TChala', 'Sales', 'B')''')

# Display all the records
print("Below are the inserted records...")
data = cursor.execute('''select * from STUDENT''')
for rec in data:
    print(rec)

# Commit your changes in the DB
connection.commit()
connection.close()