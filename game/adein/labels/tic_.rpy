
label toc_:
    
    while _y < len(corre): #int, int

        s_ "[toc]"

        menu:

            s_ "{cps=0}[toc]{/cps=0}"

            "[sic]":
                j_ "[sic]."
                s_ "[top]."
                jump tic_

            "[nic]":
                j_ "[nic]."
                s_ "[toq]."
                jump tic_
                
            "[tic]":
                j_ "[tic]."
                s_ "[inter]"
                jump tic_
return

label tic_:

    python:
        
        _y += 1 #int

        if _y < len(corre): #int, int

            inter = random.choice(_interf) #str
            toc = (random.choice(_tocs) % (tc[_y])).capitalize() #str
            
            sic = (random.choice(_tics) % ('positivamente')).capitalize() #str
            nic = (random.choice(_tics) % ('negativamente')).capitalize() #str
            tic = (random.choice(_tics) % ('é irrelevante')).capitalize() #str

            top = (random.choice(_tops) % (_qpqs[tc[_y]][1])).capitalize() #str
            toq = (random.choice(_toqs) % (_qpqs[tc[_y]][0])).capitalize() #str 

        renpy.jump("toc_")
        
return