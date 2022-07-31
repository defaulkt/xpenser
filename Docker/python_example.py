import psycopg2

conn = psycopg2.connect(
    host='localhost',
    port=54320,
    dbname='expenser',
    user='postgres',
    password='my_password',
)
cur = conn.cursor()
cur.execute("INSERT INTO users (name, email, phone, role_id) VALUES (%s, %s, %s, %s)", ("John Connor", "jconnor@gmail.com", "2129111", 1))
cur.execute("SELECT * FROM users;")
result = cur.fetchone()
print(result)
conn.commit()
cur.close()
conn.close()
