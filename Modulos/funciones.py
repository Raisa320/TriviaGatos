from Modulos.colores import *
#Variables Globales
puntaje = 0  #Putntaje inicial
isFoundSecret = False  #Por si descubre la palabra secreta (solo se descubre una vez)

####FUNCIONES ############
#PARA VALIDACION DE LA PREGUNTA SI ESTA EN EL RANGO O SE DESCUBRE LA PALABRA SECRETA
def validacionRpta(nroPregunta=0):
    # Almacenamos la respuesta del usuario en la variable "respuesta"
    respuesta = input(UBLUE + B_BLUE + "\nTu respuesta:" + RESET + RESET + " ")
    while respuesta.lower() not in ("a", "b", "c", "d", "prrr", "miau"):
        respuesta = input("*** Debes responder a, b, c o d.*** \n Ingresa nuevamente tu respuesta: ")
    #Esta es la palabra secreta, solo se descubre 1 vez
    if (respuesta == "miau"):
        global isFoundSecret #para usar variable global
        if (isFoundSecret):
            print("Ya no puedes decirme eso. Ya me lo has dicho! Mejor responde la pregunta")
        else:
            print(B_GREEN+"Vaya, nunca me habian dicho algo tan lindo! Has descubierto la palabra secreta en la trivia. Genial, Obtienes 100 puntos"+RESET)
            global puntaje
            puntaje += 100 #suma 100 puntos si se descubre palabra
            print(B_RED+"\n******Ey! Aún tienes que responder la pregunta.******"+RESET)
            isFoundSecret = True
        respuesta = validacionRpta(nroPregunta)
    #Esta es una palabra que se menciona si responde "no" en la pregunta random es una ayuda para el jugador, (solo funciona en la pregunta 2)
    if respuesta == "prrr" and nroPregunta == 2:
        print("****-> Todo sea por ese ronroneo, Tip: La respuesta esta en tu"+B_RED+ " NARIZ"+RESET +".Creo que la respuesta es obvia!")
        respuesta = validacionRpta()
    elif respuesta == "prrr":
        print("****-> Ey! aunque ronronees, pero esta no es la pregunta con ayuda. Vamos sé que tú puedes!.")
        respuesta = validacionRpta()
    return respuesta.lower()#devuelve en minuscula

#PARA MOSTRAR EL MENSAJE ACTUAL
def mostrarPuntajeActual(user, puntaje):
    print(B_YELLOW +
          "\n=========================================================")
    print("||", user, "tu puntaje actual es de:", puntaje, "puntos ||")
    print("=========================================================" + RESET)


#PARA IMPRIMIR LAS OPCIONES DE RESPUESTA
def printOpciones(listaOpciones):
    alternativas = ["a", "b", "c", "d"]
    for alt, opcion in zip(alternativas, listaOpciones):
        print("\t" + alt + ") " + opcion)

#PARA VALIDAR QUE INGRESE UN NÚMERO
def validarNum(mensaje):
    try:
        numero=int(input(mensaje))
        print(type(numero))
        return numero
    except:
        print("No se ha ingresado un número")
        numero=validarNum(mensaje)
        return numero
#####FIN DE FUNCIONES#################