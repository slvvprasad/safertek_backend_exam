import sqlite3

# data for the table
locations_data = [
    (1000, '1297 Via Cola di Rie', '989', 'Roma', '', 'IT'),
    (1100, '93091 Calle della Te', '10934', 'Venice', '', 'IT'),
    (1200, '2017 Shinjuku-ku', '1689', 'Tokyo', 'Tokyo Prefectu', 'JP'),
    (1300, '9450 Kamiya-cho', '6823', 'Hiroshima', '', 'JP'),
    (1400, '2014 Jabberwocky Rd', '26192', 'Southlake', 'Texas', 'US'),
    (1500, '2011 Interiors Blvd', '99236', 'South San', 'California', 'US'),
    (1600, '2007 Zagora St', '50090', 'South Brun', 'New Jersey', 'US'),
    (1700, '2004 Charade Rd', '98199', 'Seattle', 'Washington', 'US'),
    (1800, '147 Spadina Ave', 'MSV 2L7', 'Toronto', 'Ontario', 'CA')
]

countries_data = [
    ('AR', 'Argentina', 2),
    ('AU', 'Australia', 3),
    ('BE', 'Belgium', 1),
    ('BR', 'Brazil', 2),
    ('CA', 'Canada', 2),
    ('CH', 'Switzerland', 1),
    ('CN', 'China', 3),
    ('DE', 'Germany', 1),
    ('IT', 'Italy', 3),
    ('JP', 'Japan', 2),
    ('US', 'Usa', 3)
]

# Used in-memory SQLite database, we can use user defined database by using sqlite3.connect("database_name");
conn = sqlite3.connect(':memory:')

# Creation of locations and countries tables
conn.execute('''CREATE TABLE locations (
                location_id INT,
                street_address TEXT,
                postal_code TEXT,
                city TEXT,
                state_province TEXT,
                country_id TEXT
            )''')

conn.execute('''CREATE TABLE countries (
                country_id TEXT,
                country_name TEXT,
                region_id INT
            )''')

# Insertion data into tables
conn.executemany('INSERT INTO locations VALUES (?, ?, ?, ?, ?, ?)', locations_data)
conn.executemany('INSERT INTO countries VALUES (?, ?, ?)', countries_data)

# Query to find the address of locations in Canada without using JOIN
query = '''
    SELECT l.location_id, l.street_address, l.city, l.state_province, 'Canada' AS country_name
    FROM locations l
    WHERE l.country_id IN (SELECT country_id FROM countries WHERE country_name = 'Canada')
'''

# Execution of the query
cursor = conn.execute(query)

# Fetching and printing the results
for row in cursor.fetchall():
    print(row)

# Closing the database connection
conn.close()
