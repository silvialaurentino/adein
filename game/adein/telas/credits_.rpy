## ATL for scrolling screen object. In this case, credits roll.
## Speed is the time for object to move up from initial ypos to finish ypos.

transform credits_scroll(speed):
    ypos 2500
    linear speed ypos 200

## Credits screen.

screen credits_():
    style_prefix "credits"

    add "#000"

    frame at credits_scroll(20):
        xalign 0.5 yalign 0.5 background None

        vbox:
            xsize 565 xalign 0.5 yalign 0.5 
            
            label "Créditos" xalign 0.5 ysize 200

            null height 20

            hbox:
                text "Silvia Laurentino"
                text "Developer  "

            hbox:
                text "Silvia Laurentino"
                text "Designer           "

            hbox:
                text "Silvia Laurentino"
                text "Writer          "

            hbox:
                text "Silvia Laurentino"
                text "Soundtracker       "

            hbox:
                text "Gabriel Lemos     "
                text "Tester"
            
            textbutton "f i m":
                xalign 0.5 ysize 2000 background None          
                action Return(True)


style credits_hbox:
    spacing 100
    ysize 100
