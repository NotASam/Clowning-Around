


define hombre = Character("Vincent", color="ff0000")
define jugador = Character("game")
#character per second
default preferences.text_cps = 20
#Fonts
define gui.name_text_font = "MozartNbp-93Ey.ttf"
define gui.text_font = "MozartNbp-93Ey.ttf"
define gui.interface_text_font = "MozartNbp-93Ey.ttf"
#Size of the fonts
define gui.interface_text_size = 80
define gui.text_size = 55
define gui.name_text_size = 65

#talk oscilation
transform talk_bounce:
    linear 0.15 yoffset -10
    linear 0.15 yoffset 0
    repeat

label start:

    scene black

    "Ughhhhhhhhhhhh"
    "..."
    "No veo un CXLX"
    "..."
    
   
    scene bar_1_cropped

    show risa

    hombre "Nah, mentira, te estoy molestando"

    hide risa
    show eyebrow_raised

    hombre "¿Estas curioso que todas mis noches sean iguales, eh?"
    hombre "..."
    hide eyebrow_raised
    show clown_normal

    hombre "A veces pienso que podría ser mejor"
    hide clown_normal
    show clown_aroused
    hombre "Pero cada vez que lo intentas, vuelves a lo mismo."
    hombre "y lo mismo"
    hide clown_aroused
    show tipsy
    hombre "y más de lo mismo"
    hide tipsy
    show eyebrow_raised 
    hombre "De cualquier forma, es todo lo que conozco. ¿Y qué hay de malo?"
    hombre "Mirame a mi… un payaso que trabaja con niños… "
    hide eyebrow_raised
    show clown_aroused
    hombre "..."
    hide clown_aroused
    show clown_normal
    hombre "Y aun asi… no encuentro la felicidad en ellos… ni en nada más…"
    hombre "Siempre caigo en lo mismo… y…"
    hide clown_normal
    show risa
    hombre "Me encanta"

    scene black

    jugador "¿qué quieres hacer primero?"
    menu:
        "Tomar":
            call respuesta4 from _call_respuesta4

        "Gamble":
            jump respuesta5

    scene bar2_cropped

return #return del label start.




label respuesta4:
    scene bar2_cropped
    show risa
    hombre "Ahhh sí. Lo que necesitaba"
    hide risa
    show clown_normal
    hombre "Este ambiente, esta música, esto… es mi vida."
    hombre " Bueno… digamos que por fin comenzaré a vivir."
    hide clown_normal

    scene black 

    jugador "..."
    jugador "tomando"

    scene bar_1_cropped

    show tipsy

    hombre " ¡Este es el mejor día de mi vida! Jajaja!!!"
    hombre "Ja… ja… me siento… raro… ¿crees que debería parar…?"

    menu:
        "Seguir":
            call respuesta1 from _call_respuesta1

        "Parar":
            jump respuesta2

    return #return del label start.

label respuesta1: 
    hide tipsy
    "este juego es un WIP esperamos terminarlo para harvest <3"
    scene Follow_us_4_more_cropped
    return
label respuesta2:
    hide tipsy 
    "Este juego es un WIP esperamos terminarlo para harvest <3"
    scene Follow_us_4_more_cropped
    return
label respuesta5:
    scene billar
    hide tipsy
    show clown_normal
    hombre "¿Que crees que deberiamos apostar?"
menu:
    "500":
        call respuesta6 from _call_respuesta6
    "1000":
        call respuesta7 from _call_respuesta7

return
label respuesta6:
 
    hombre "¡Mixxda, Perdi! "
    hide clown_normal
    show eyebrow_raised
    hombre "¿Qué tal si probamos otro juego?"
    return
label respuesta7:
   
    hombre "¡Mixxda, Perdi! "
    hide clown_normal
    show eyebrow_raised
    hombre "¿Qué tal si probamos otro juego?"
    return
menu:
    "si":
        call respuesta8 from _call_respuesta8
    "no":
        call respuesta9 from _call_respuesta9
return

label respuesta8:
    scene follow
    "Este es un WIP esperamos terminarlo en harvest <3"
    "Historia por Juan Camilo, Arte por Mangie y Coding por Samuel"
    "Nuestros Usuarios de Github"
    "Juanky7"
    "NotASam, inspirado en Nathan"
    "Mang1e-not-mango"
    "gracias por hacer un playtest"
return
label respuesta9:
    scene follow
    "Este es un WIP esperamos terminarlo en harvest <3"
    "Historia por Juan Camilo, Arte por Mangie y Coding por Samuel"
    "Nuestros Usuarios de Github"
    "Juanky7"
    "NotASam, inspirado en Nathan"
    "Mang1e-not-mango"
    "gracias por hacer un playtest"
return