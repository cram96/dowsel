import database
i = 0
def mostrarTitulo():
    x=database.main.conseguirTitulos()
    global i
    titulo=x[i]

    return titulo

def mostrarPrueba():
    global i
    x=database.main.conseguirDescripciones()
    prueba=x[i]
    return prueba

def siguiente():
    global i
    i = i + 1
