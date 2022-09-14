import time
import random  #Libreria random
import os #Libreria para limpiar pantalla 
###CONSTANTES DE COLORES
RED = '\033[31m'
GREEN = '\033[32m'
PURPLE = '\033[0;95m'
RESET = '\033[0m'
#COLORES CON NEGRITA
B_RED = "\033[1;31m"  # Red
B_GREEN = "\033[1;32m"  # Green
B_YELLOW = "\033[1;33m"  # Yellow
B_BLUE = "\033[1;34m"  # Blue
B_PURPLE = "\033[1;35m"  # Purple
B_CYAN = "\033[1;36m"  # Cyan
#COLORES CON SUBRAYADO
URED = "\033[4;31m"  # Red
UGREEN = "\033[4;32m"  # Green
UYELLOW = "\033[4;33m"  # Yellow
UBLUE = "\033[4;34m"  # Blue
#COLORES CON BACKGROUND
BG_CYAN = "\033[0;106m"  # Cyan
####FIN DE CONSTANTES#####

###VARIABLES
puntaje = 0  #Putntaje inicial
isFoundSecret = False  #Por si descubre la palabra secreta (solo se descubre una vez)
iniciarTrivia = True  #Repetir trivia
intentos = 1  #Nro de intentos de trivia
listaPuntajeIntentos=[] #Guarda el puntaje que se realiza en cada intento
#os.name (define el sistema operativo), var es la palabra para limpiar pantalla 
if os.name == "posix":
   var = "clear"       
elif os.name == "ce" or os.name == "nt" or os.name == "dos":
   var = "cls"

####FIN DE VARIABLES#####


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


#####FIN DE FUNCIONES#################

#######COMIENZO DEL PROGRAMA EN CONSOLA
# Lo primero es mostrar en pantalla el texto de bienvenida para quien juegue tu trivia
print(B_YELLOW + "★★★★★" + GREEN + " Bienvenido a mi trivia sobre Gatos" + RESET + B_YELLOW + " ★★★★★" + RESET)

# Agregaremos personalización para nuestros jugadores, preguntando y almacenando sus nombres en una variable
user = input("\nHola!, ¿Cuál es tu nombre?: ")
user = user.capitalize()  #El primer caracter se pone en mayuscula
print(f"{PURPLE} \u261E Bueno {user},el día de hoy pondremos a prueba tus conocimientos sobre gatos\n {RESET}")

# Es importante dar instrucciones sobre cómo jugar:
print(GREEN + "=====================================================")
print("|| INDICACIONES:                                   ||")
print("|| 1. Para contestar una pregunta debes escribir   ||")
print("||    la letra de la alternativa y presionar ENTER ||")
print("|| 2. Cada respuesta correcta se te sumará puntos  ||")
print("|| 3. Cada respuesta incorrecta se restará puntos  ||")
print("=====================================================" + RESET)

#Bucle de trivia si se repite
while iniciarTrivia:
    ##PREGUNTA RANDOM: Que otorga una pista en la primera pregunta, si responde que le encantan los gatos
    print("\nAntes de comenzar, tengo una pregunta importante que hacerte:")
    pregunta_random = input(B_BLUE +"¿Eres un fanatico de los gatos?[si/no]: " + RESET)
    if (pregunta_random.lower() == "si"):
        print( GREEN +"\n¡Yo también!, te regalaré una pista de la primera pregunta, pero no se lo digas a nadie, será nuestro secreto. Porque en esta trivia amamos los gatos y a quienes aman a los gatos \n" + RESET + B_RED + "PISTA: Son menos de 34" + RESET)
    elif (pregunta_random.lower() == "no"):
        print(B_CYAN + "\nVaya! entonces este no será una trivia muy fácil para ti :c. \n" + RESET + B_GREEN + "TIP: Intenta escribir 'Prrr' en alguna pregunta puede que haya una ayuda para ti" + RESET)
    else:
        print(RED + "\n*** Vaya! Parece que no nos estamos entendiendo, debias escribir: si o no. Tienes 3 puntos menos por tu rebeldia! ***" + RESET)
        puntaje = -3
      
    #Funcion que retrasa un poco el comienzo de las siguientes sentencias
    time.sleep(2)
    #Mensaje de inicio y también muestra el numero de intentos
    print( B_PURPLE + "\n Bueno, comencemos! Buena suerte," + user + " con tu " + RESET + B_BLUE + "intento número ", intentos, "\n" + RESET)
    time.sleep(2)
    #Inicio de puntaje random
    puntaje += random.randint(0, 21)
    #Mostrar puntaje actual
    print(B_GREEN + "=========================================")
    print("|| Inicias con:", puntaje, "puntos     ||")
    print("=========================================" + RESET)

    print(UYELLOW + "\n★★★★★" + RESET + UGREEN + " Trivia sobre Gatos" +
          RESET + UYELLOW + " ★★★★★\n" + RESET)
    ###PANTALLA DE CARGA CON UN LOOP FOR - DESAFIO CICLOS
    print(B_BLUE + "Cargando la trivia.")
    for x in range(5, 0, -1):
        print(x)
        time.sleep(1)
    print(RESET + B_GREEN + "\nTrivia lista!\n" + RESET)
    
    ########PREGUNTA 1
    valorRandom = random.randint(6, 15)
    print(f"{BG_CYAN}->PREGUNTA 1:{RESET} {URED}({valorRandom} puntos si es correcta o -{valorRandom} si es incorrecta){RESET}")
    print("1) ¿Cuántos músculos tienen los gatos en las orejas?")
    #Funcion que imprime las opciones desde una lista
                    #a     b     c    d
    printOpciones(["32", "34", "30", "36"])
    ##Validación de que la respuesta se encuentre en el rango de [a,b,c,d]
    respuesta_1 = validacionRpta()
    if (respuesta_1 == "a"):
        print(B_GREEN, "Bien hecho", user,
            "! Los gatos tienen 32 músculos en la oreja y pueden girarlas 180 grados, pero la ciencia ha demostrado que las usan para ignorarte.", RESET)
        puntaje += valorRandom
    else:
        print(B_RED, user, "tu respuesta es incorrecta!", RESET)
        puntaje -= valorRandom

    #Mostrar puntaje actual
    mostrarPuntajeActual(user, puntaje)
    ##Tiempo de espera para que pueda ver resultados y respuestas
    time.sleep(2)

    ####### Pregunta 2
    valorRandom = random.randint(9, 20)
    print(f"{BG_CYAN}\n->PREGUNTA 2:{RESET} {URED}({valorRandom} puntos si es correcta o -{valorRandom} si es incorrecta){RESET}")
    print("\n2) ¿Cuál es la parte del cuerpo de un gato que podría considerarse su huella digital?")
    #Funcion que imprime las opciones desde una lista
                    #a     b     c    d
    printOpciones(["cola", "patas", "nariz", "lengua"])

    ##Validación de que la respuesta se encuentre en el rango de [a,b,c,d]
    respuesta_2 = validacionRpta(2)
    if (respuesta_2 == "c"):
        print(B_GREEN, "Es CORRECTO", user,". La nariz de un gato domestico tiene un patrón único", RESET)
        puntaje += valorRandom
    else:
        print(B_RED, user, "tu respuesta es incorrecta!", RESET)
        puntaje -= valorRandom
    #Mostrar puntaje actual
    mostrarPuntajeActual(user, puntaje)
    ##Tiempo de espera para que pueda ver resultados y respuestas
    time.sleep(2)

    ####### Pregunta 3
    valorRandom = random.randint(5, 13)
    print(f"{BG_CYAN}\n->PREGUNTA 3:{RESET} {URED}({valorRandom} puntos si es correcta o -{valorRandom} si es incorrecta){RESET}")
    print("\n3) ¿Qué raza de gato ha sido asociada a lo largo de la historia con el lujo y la realeza?")
    #Funcion que imprime las opciones desde una lista
                    #a     b     c    d
    printOpciones(["Gato Siberiano", "Gato Siamés", "Gato Esfinge", "Gato Persa"])

    ##Validación de que la respuesta se encuentre en el rango de [a,b,c,d]
    respuesta_3 = validacionRpta()
    if (respuesta_3 == "a"):
        print(B_RED, "Incorrecto!", user,'Este tipo de gatos son asociados al hogar. Se les suele llamar el más "perro" de los gatos porque su carácter es más amigable, cariñoso y fiel que el de la mayoría de los gatos.',RESET)
        puntaje -= valorRandom
    elif respuesta_3 == "b":
        print(B_RED, "Incorrecto!", user, "Este tipo de gatos son asociados al mundo espirtual. Se creía que este gato era un gran defensor de los espíritus, ya que de alguna manera podía absorber el espíritu de un difunto y hacer que este permaneciera vivo evitando los ataques de malos espíritus.",RESET)
        puntaje -= valorRandom
    elif respuesta_3 == "c":
        print(B_RED, "Incorrecto!", user, "Los gatos esfinge debido a su falta de pelaje, su aspecto delgado y con arrugas son a menudo asociados con la maldad o perversidad, pero realmente son gatos tan buenos y cariñosos como otro cualquiera." + RESET)
        puntaje -= valorRandom
    else:
        print(B_GREEN, "Bien hecho", user,"! El gato persa es una de las razas de gatos más antiguas del mundo",RESET)
        puntaje += valorRandom
    #Mostrar puntaje actual
    mostrarPuntajeActual(user, puntaje)
    ##Tiempo de espera para que pueda ver resultados y respuestas
    time.sleep(2)

    ####### Pregunta 4
    #La puntuación de esta pregunta será dependiendo de la que se elija asi pruebo lo de usar OPERADORES MATEMATICOS (DESAFIO)
    print(f"{BG_CYAN}\n->PREGUNTA 4:{RESET} {URED}El puntaje de esta pregunta dependerá de la respuesta que elijas. Elige sabiamente.{RESET}")
    print("\n4) ¿Qué usan los gatos para orientarse y detectar si alcanzan a pasar por un espacio?")
    #Funcion que imprime las opciones desde una lista
                    #a     b     c    d
    printOpciones(["Las patas", "La cola", "Los bigotes", "Las orejas"])

    ##Validación de que la respuesta se encuentre en el rango de [a,b,c,d]
    respuesta_4 = validacionRpta()
    if (respuesta_4 == "a"):
        print(B_YELLOW, "Es incorrecto, pero tendría algo de sentido.", user, "por tu creatividad de elección te doy 5 puntos", RESET)
        puntaje += 5
    elif (respuesta_4 == "b"):
        print(B_RED, "En serio", user,"? Tu respuesta es incorrecta, pero soy buena onda, solo te restaré 5 puntos",RESET)
        puntaje -= 5
    elif (respuesta_4 == "c"):
        print(B_GREEN, "Totalmente Correcto", user,". Sus bigotes miden aproximadamente la anchura de su cuerpo lo que les permite calcular distancias y profundidades de los objetos con mucha precisión. [Te multiplicaremos tu puntaje]",RESET)
        puntaje *= 2
    else:
        print(B_RED,"Por qué serian las orejas? Es totalmente disparatado, dividiremos tu puntaje a la mitad.",RESET)
        puntaje /= 2

    #Mostrar puntaje actual
    mostrarPuntajeActual(user, puntaje)
    ##Tiempo de espera para que pueda ver resultados y respuestas
    time.sleep(2)

    ####### Pregunta 5
    valorRandom = random.randint(3, 10)
    print(f"{BG_CYAN}\n->PREGUNTA 5:{RESET} {URED}({valorRandom} puntos si es correcta o -{valorRandom} si es incorrecta){RESET}")
  
    print("\n5) ¿Qué zona del cuerpo es preferible NO acariciar a un gato porque le disgusta?")
    #Funcion que imprime las opciones desde una lista
                    #a     b     c    d
    printOpciones(["El cuello", "La barriga", "Tras las orejas", "Bajo la barbilla"])

    ##Validación de que la respuesta se encuentre en el rango de [a,b,c,d]
    respuesta_5 = validacionRpta()
    if (respuesta_5 == "b"):
        print(B_GREEN,"Correcto! La barriga es una zona muy vulnerable de su cuerpo. Asi que a modo de supervivencia, rechazará cualquier tipo de contacto en esa parte.",RESET)
        puntaje += valorRandom
    else:
        print(B_RED, "Incorrecto!", user," Como norma general, a la mayoría de los gatos les encanta que les toquen alrededor de las zonas en las que se localizan las glándulas faciales.", RESET)
        puntaje -= valorRandom
    #Mostrar puntaje actual
    mostrarPuntajeActual(user, puntaje)
    ##Tiempo de espera para que pueda ver resultados y respuestas
    time.sleep(2)

    ###RESULTADOS
    print(UGREEN + "\nRESULTADOS: " + RESET)
    ##RULETA DE PUNTAJE FINAL - MODIFICA EL PUNTAJE POR UN JUEGO DE AZAR
    azar = input( "Ey! Antes de mostrarte tus resultados. ¿Te gustaria un juego al azar con tus puntos?[si/no]: ")
    if (azar.lower() == "si"):
        print(B_BLUE + "¡Genial! Eres un ser humano arriesgado" + RESET)
        ##Vamos a darle 5 opciones  de puntajes que podria sumar o restar
        opcionesNum = []
        print("Elige cuanto quieres ganar o perder...: ")
        for i in range(1, 6, 1):
            numRandom = random.randint(20, 400)
            print(i, ")", numRandom)
            opcionesNum.append(numRandom)
        indiceNum = int(input("Elija una opcion: "))
        indiceNum -= 1
        while (indiceNum >= len(opcionesNum)):
            print("No puede elegir una opcion fuera de rango [1-5]")
            indiceNum = int(input("Elija una opcion: "))
            indiceNum -= 1
        numRandom = opcionesNum[indiceNum]
        time.sleep(2)
        print(B_GREEN + "**** Podrias sumar", numRandom,"puntos o podrias restarle", numRandom,"a tu puntaje ****" + RESET)
        print("Dejemos que la suerte decida tu destino!")
        #Si el numero que elige el usuario es el mismo al del random se suma
        numeroEleccionUsuario = int(input("Elige [1 o 2]: "))
        resultado = random.randint(1, 3)
        ####FOR -LOOP DEL DESAFIO DE CICLOS.
        print("Resultado en: ")
        for x in range(3, 0, -1):
            print(x)
            time.sleep(1)
        if resultado == numeroEleccionUsuario:
            print(B_BLUE + "Genial! Tienes mucha suerte se te sumaran", numRandom, "puntos" + RESET)
            puntaje += numRandom
        else:
            print(B_RED + "Vaya suerte la tuya. Por desgracia se estaran", numRandom, "puntos" + RESET)
            puntaje -= numRandom
    elif (azar.lower() == "no"):
        print(UYELLOW + "Oh! Es una pena podrias haber sumado más puntos." + RESET)
    else:
        print(URED + "No nos estamos entendiendo :c, era escribir si o no." + RESET)

    print(UBLUE + B_BLUE + "\nObtuviste", puntaje, "puntos.", end=" ")
    ###Resultados segun pregunta random
    if (pregunta_random == "si" and puntaje <= 10):
        print("Esperaba más de un fanático de los gatos.")
    elif (pregunta_random == "si" and puntaje >= 40):
        print("Realemente eres un gran fanático de los gatos.")
    elif pregunta_random == "si":
        print("Bien hecho eres un fanático promedio.")

    #Resultados para los que contestaron "no" o si escribieron cualquier cosa
    if (pregunta_random != "si" and puntaje <= 10):
        print("Bueno al menos aprendiste algo nuevo.")
    elif (pregunta_random != "si" and puntaje >= 40):
        print("¿Estas seguro que no eres un fanático de los gatos?.")
    elif pregunta_random != "si":
        print("Eso no estuvo mal para no saber mucho de gatos.")

    ##PREGUNTA SI EL USUARIO QUIERE JUGAR DE NUEVO PUNTAJE VUELVE A 0
    print(RESET + B_YELLOW + UYELLOW +
          "\n¿Deseas intentar la trivia nuevamente?" + RESET)
    repetir_trivia = input("Ingresa 'si' para repetir, o cualquier tecla para finalizar: ").lower()
    listaPuntajeIntentos.append(puntaje)
    puntaje = 0
    intentos += 1
    isFoundSecret = False ##Retorna a false porque al ser nuevo intento puede escribirla de nuevo
    time.sleep(2)
    os.system(var)
    if repetir_trivia != "si": 
        print(f"{UGREEN}\nEspero {user} que lo hayas pasado bien, hasta pronto!{RESET}")
        #RESUMEN DEL JUEGO CON LOS INTENTOS, SU PUNTAJE Y SUMA DE ESTOOS
        print(B_YELLOW+UYELLOW+"RESUMEN DE JUEGO:"+RESET)
        for puntos in listaPuntajeIntentos:
          print("-> Intento",(listaPuntajeIntentos.index(puntos)+1),":",puntos,"puntos")
        print(B_BLUE,"Puntaje total:",RESET,sum(listaPuntajeIntentos),"puntos")
        iniciarTrivia = False  # Cambiamos el valor de iniciar_trivia a False para evitar que se repita.
        print(UGREEN+"¡Gracias por jugar!" + RESET)