define hombre = Character("Abraham Camargo", color="ff0000")
define jugador = Character("You")

label start:

    scene placeholder

    "hola soy payasin"
    "..."
    "texto prueba prueba prueba"
    "un cafecito"
    "bien rico, bien rico"
    "una sonrisita"
    "bonita bonitaa"
    "un abrazito"
    "calientito, calientitoooo"

    show clown_normal

    hombre "ayyy me dister por donde era"
    hombre "n word escrito en el tablero del todo fucking curso"
    hombre "Bonjour j´suis une salope"

    hide clown_normal 
    show clown_aroused

    hombre "im angyyy"

    menu:
        "4":
            call = respuesta4

        "5":
            call2 = respuesta5

    "sssss hola"

return #return del label start.




label respuesta4:
    "Mariangela x Abraham.. 4"
    return
label respuesta5:
    "Maria Angelica... 5"
