import psycopg2
try:
	cnn = psycopg2.connect("dbname=<db_name> host=localhost user=<user_name> password=*****")
	cur = cnn.cursor()
	cur.execute("select * from <db_name>")
	rows = cur.fetchall()
	for line in rows:
		print(line)
except (psycopg2.OperationalError) as e:
	print (e)
