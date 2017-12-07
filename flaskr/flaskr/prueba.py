import psycopg2

pruebas=[]
def connection():
	conn_string="host='137.74.168.217' dbname='beermanity' user='postgres'password='beermanity'"
	conn=psycopg2.connect(conn_string)
	c=conn.cursor()

	return c, conn
c,conn=connection()
c.execute("select * from pruebas")
pruebas.append(c.fetchall())
print (pruebas)
print (pruebas[2])