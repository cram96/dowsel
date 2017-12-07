import psycopg2
ListaTitulos = []
ListaDescripciones = []
ListaPruebas = []
class main:

    conn_string = "host='localhost' dbname='beermanity' user='postgres' password='beermanity'"
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()
    cursor.execute("Select * from pruebas")
    for row in cursor.fetchall():
        ListaTitulos.append(row[0])
        ListaDescripciones.append(row[1])


    def conseguirTitulos():
        return ListaTitulos

    def conseguirDescripciones():
        return ListaDescripciones

