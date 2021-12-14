    
label pq_(n=0):

    while _y < 10:

        $ pqz = (random.choice(_pqs) % (p, q)).capitalize() #str
        $ truf = random.choice(_trufs) #str
            
        s_ "[pqz]"

        menu:

            s_"{cps=0}[pqz]{/cps}"

            "[spq]":
                j_ "[spq]."
                call qp_(p, q, qn) #str, str, str
                    
            "[tpq]":
                j_ "[tpq]."
                call qp_(pn, qn, q) #str, str, str

            "[npq]":
                j_ "[npq]."
                if n == 0:
                    s_ "[truf].. . ."
                    $ (p, pn) = (pn, p) #str, str
                    $ (q, qn) = (qn, q) #str, str
                    $ n += 1 #int 
                    call pq_(n) #int
                elif n == 1:
                    s_ "[truf].. . ."
                    $ (p, pn) = (pn, p) #str, str
                    $ (q, qn) = (d, dn) #str, str
                    $ n += 1 #int
                    call pq_(n) #int
                elif n == 2:
                    s_ "[truf].. . ."
                    $ (p, pn) = (pn, p) #str, str
                    $ (q, qn) = (qn, q) #str, str
                    $ n += 1 #int
                    call pq_(n) #int
                else:
                    call qp_
return

label qp_(_p=0, _q=0, _qn=0): #str, str, str

    python:
            
        if _p != 0:

            pq[_p] = [_q, _qn] #str

        _y += 1 #int

        if _y < 10:

            spq = (random.choice(_tics) % ('sim')).capitalize() #str
            npq = (random.choice(_tics) % ('não')).capitalize() #str
            tpq = (random.choice(_tics) % ('talvez')).capitalize() #str

            p = corre[0][1][_y] #str
            q = corre[1][1][_y] #str
            d = corre[2][1][_y] #str

            pn = corre[0][0][_y] #str
            qn = corre[1][0][_y] #str
            dn = corre[2][0][_y] #str
                
            renpy.jump("pq_")
return