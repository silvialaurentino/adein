label hallo_:

    scene intro with Dissolve(5)
        
    $ _n = '' #str
    $ _s = '' #str 

    show silv with dissolve   
    "Olá."
    "Como posso te chamar?"
    
    $ _n = renpy.input("{cps=0}Como posso te chamar?{/cps}") #str
    $ _n = _n.capitalize() #str

    "Dela, dele ou del?"
    menu:

        "Dela":
            $ _s = 'a' #str
        "Dele":
            $ _s = 'o' #str
        "Del":
            pass
                
    s_ "Ok. {w=0.3}Podes me chamar de Silvia!"
    s_ "Fico feliz por estares interessad[_s] em nos conhecer."
    s_ "Nos, nós: Tu e eu."
    s_ "Espero que seja divertido responder minhas perguntas a teu respeito."
    s_ "Já antecipo que sou bem curiosa.. . ."
    s_ "Estás acostumad[_s] com o formato de uma Visual Novel?"
        
    menu:

        "Sim":
            s_ "Legal!"
            s_ "Seguindo essa interação, serás levad[_s] ao primeiro mapa."
                
        "Não":
            s_ "De maneira similar a forma como escrevestes teu nome e utilizastes um menu de escolhas para me passar tuas informações iniciais, ao decorrer da Visual Novel irás interagir comigo através dessas duas abordagens: Menus e entradas textuais."
        
    s_ "Sempre que uma interação for finalizada, voltarás ao mapa e poderás escolher outro local para iniciares uma próxima."
    s_ "Poderás também explorar os locais sem necessariamente interagir com eles."
    s_ "Ou fazer um bom passeio.. . ."
    s_ "Por hora, interaja com o próximo mapa para me encontrar novamente."
    s_ "Te vejo lá!"