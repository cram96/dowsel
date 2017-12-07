import psycopg2
import flaskr

def connection():
	conn_string="host='localhost' dbname='beermanity' user='postgres'password='beermanity'"
	conn=psycopg2.connect(conn_string)
	c=conn.cursor()

	return c, conn

def getPruebas():
	c,conn=connection()
	c.execute("select * from pruebas")
	for row in c.fetchall():
		flaskr.titulos.append(row[0])
		flaskr.pruebas.append(row[1])

def insertUser(a,b):
	c,conn=connection()
	query="Insert into users values("+a+","+b+");"
	c.execute(query)
	conn.commit()
	
def validarUser(attempted_username,attempted_password):
	c,conn=connection()
	usuario="'"+attempted_username+"'"
	contrasena="'"+attempted_password+"'"
	query="Select * from users where name="+usuario+" and password="+contrasena+";"
	c.execute(query)
	x=c.fetchone()
	if x is not None:
		flaskr.validar=True