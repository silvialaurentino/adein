
label setrufa_(n=False):

    while _y < 10:
            
        $ setrufa = ("%s %s ou %s?" % (se, tru, fa)).capitalize() #str
                        
        s_ "[setrufa]"

        menu:
                
            s_ "{cps=0}[setrufa]{/cps}"

            "[tru]":
                j_ "[tru]."
                call ortrufa_(tru, fa, 1) #str, str, int 
            "[fa]":
                j_ "[fa]."
                call ortrufa_(fa, tru, 1) #str, str, int
            "[trufu]":
                if n:
                    j_ "[trufu]."
                    call ortrufa_(tru, fa, 2) #str, str, int
                else:
                    j_ "[trufu]."
                    s_ "[truf].. . ."
                    $ (tru,fa) = (fa,tru) #str, str
                    $ (se, sen) = (sen, se) #str, str
                    call setrufa_(True) #bool
            "[trufz]":
                call person_
                call ortrufa_ (tru, fa, 1) #str, str, int

return

label ortrufa_(_tru=0, _fa=0, _or=0):

    python:

        if _or == 2:
            fatru.append(se + ' ' + _tru) #str, str
            fatrz.append(se + ' ' + _fa) #str, str
        elif _or == 1:
            fatru.append(se + ' ' + _tru) #str, str
            fatrz.append(sen + ' ' + _fa) #str, str

        _y += 1 #int
            
        if _y < 10:

            se = random.choice(_trufas[1]) #str
            sen = random.choice(_trufas[0]) #str

            trufz = random.choice(_trufus[0]) #str
            trufu = random.choice(_trufus[1]) #str

            truf = random.choice(_trufs) #str

            tru = _trafus[_t][1][_y] #str
            fa = _trafus[_t][0][_y] #str

            renpy.jump("setrufa_")
return

label person_:
        
    $ inter = random.choice(_inters) #str
    $ legal = random.choice(_legool) #str
    $ contu = (random.choice(_contex) % (tru, fa, se)).capitalize() #str
    $ contz = (random.choice(_contex) % (tru, fa, sen)).capitalize() #str

    s_ "[inter]"
    s_ "[contu].. . .?"
    $ tru = (renpy.input("[contu].. . .?")).capitalize() #str
    j_ "[tru]."
    s_ "[contz].. . .?"
    $ fa = (renpy.input("[contz].. . .?")).capitalize() #str
    j_ "[fa]."
    s_ "[legal]~"

return