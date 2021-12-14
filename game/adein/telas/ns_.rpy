    screen ns_():

        grid 1 2:
            align 0.5, 0.5 
            at transform:
                alpha 0 
                pause 0.5 
                linear 2 alpha 1.0 

            frame:
                align 0.5, 0.5 xsize 500 ysize 150
                vbox: 
                    xalign 0.5 yalign 0.5 
                    text "Nome:":
                        xalign 0.5
                    input default "nullname":
                        pixel_width(500)
                        value VariableInputValue("_n")

            frame:
                align 0.5, 0.5 xsize 500 ysize 150
                vbox:
                    align 0.5, 0.5
                    text "Sexo:"

                    textbutton "F": 
                        xalign 0.5
                        action Return('a')

                    textbutton "M":
                        xalign 0.5
                        action Return('o')
                