import database
i=0
def mostrarTitulo():
    global i
    x=database.main.conseguirTitulos()

    titulo=x[i]
    return titulo
def mostrarPrueba():
    global i
    x=database.main.conseguirDescripciones()
    prueba=x[i]
    return prueba
def siguiente():
    global i
    i=i+1

