
label locool_(_w, _low=0):
    
    image locool = '[_w]'
    image silv = 'silv.png'
    scene locool with Dissolve(2)

    $ hallo = random.choice(_hallos) #str
    $ thall = random.choice(_thalls) #str

    menu:

        "Interagir":
            jump sc_
        "Voltar":
            jump prismap_

label lowcool_(_k):

    $ _w = 1 #int

    while (_w != 0):

        $ lowcool = 'lowcool/%i.png' % (_k) #str
        image lowcool = '[lowcool]' 
        scene lowcool with Dissolve(7)

        $ _k += 1 # int
        $ _w = _k % 5 # int
    
    jump prismap_

label sc_:

    $ _y = -1 #int
    $ _t += 1 #int

    $ _hallos.remove(hallo) #str
    $ _thalls.remove(thall)  #str

    # cap = "caps_%s" % (_t + 1)
    # renpy.call(cap)

    show silv with dissolve

    s_ "[hallo]"

    if _t < 5:

        $ fatrz = _fatrus[_t][0] #str
        $ fatru = _fatrus[_t][1] #str

        call ortrufa_

    elif _t < 7:

        if _t < 6:
            $ corre = [_fatrus[1], _fatrus[2], _fatrus[3]] #str list
        else:
            $ corre = [_fatrus[4], _fatrus[0], _fatrus[1]] #str list

        $ pq =  _qpqs #str
        
        call qp_ 

    elif _t < 9:

        $ tc = _qpqs.keys() #str
        call tic_
    
    else:
        call thall_
        return

    with flashbulb
    s_ "[thall]"

    pause 1
    jump prismap_
