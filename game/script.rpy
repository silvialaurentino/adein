
label start:

    play music 'ost_ufsc.mp3' fadeout 1
    pause(1)
    call trutru_ 
    scene game_menu with Dissolve(5)

    call screen adein_ with Dissolve(2)
        
    call hallo_ 
    call hashs_ 

    call prismap_ 

    scene black with Dissolve(2)
    call screen credits_ 
    pause 5
    scene main_menu with Dissolve(10)
    return
