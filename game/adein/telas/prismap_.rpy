label prismap_:
    
    if _t < 4:

        call screen prismap_ with Dissolve(5)

        screen prismap_():
            imagebutton auto "prismap/ufsc/a_%s.png" focus_mask True action Call ("locool_", "adein/ufsc/a.png", 0)
            imagebutton auto "prismap/ufsc/d_%s.png" focus_mask True action Call ("locool_", "adein/ufsc/d.png", 1)
            imagebutton auto "prismap/ufsc/e_%s.png" focus_mask True action Call ("locool_", "adein/ufsc/e.png", 2)
            imagebutton auto "prismap/ufsc/i_%s.png" focus_mask True action Call ("locool_", "adein/ufsc/i.png", 3)
            imagebutton auto "prismap/ufsc/n_%s.png" focus_mask True action Call ("locool_", "adein/ufsc/n.png", 4)
            imagebutton auto "prismap/ufsc/u_%s.png" focus_mask True action Call ("lowcool_", 0)
    
    elif _t < 6:

        call screen prismapk_ with Dissolve(5)

        screen prismapk_():
            imagebutton auto "prismap/ufsk/a_%s.png" focus_mask True action Call ("locool_", "adein/ufsk/a.png", 5)
            imagebutton auto "prismap/ufsk/d_%s.png" focus_mask True action Call ("locool_", "adein/ufsk/d.png", 6)
            imagebutton auto "prismap/ufsk/e_%s.png" focus_mask True action Call ("locool_", "adein/ufsk/e.png", 7)
            imagebutton auto "prismap/ufsk/i_%s.png" focus_mask True action Call ("locool_", "adein/ufsk/i.png", 8)
            imagebutton auto "prismap/ufsk/n_%s.png" focus_mask True action Call ("locool_", "adein/ufsk/n.png", 9)
            imagebutton auto "prismap/ufsk/u_%s.png" focus_mask True action Call ("lowcool_", 5)
   
    else:
    
        call screen prismapraya_ with Dissolve(5)

        screen prismapraya_():
            imagebutton auto "prismap/ufsq/a_%s.png" focus_mask True action Call ("locool_", "adein/ufsq/a.png", 10)
            imagebutton auto "prismap/ufsq/d_%s.png" focus_mask True action Call ("locool_", "adein/ufsq/d.png", 11)
            imagebutton auto "prismap/ufsq/e_%s.png" focus_mask True action Call ("locool_", "adein/ufsq/e.png", 12)
            imagebutton auto "prismap/ufsq/i_%s.png" focus_mask True action Call ("locool_", "adein/ufsq/i.png", 13)
            imagebutton auto "prismap/ufsq/n_%s.png" focus_mask True action Call ("locool_", "adein/ufsq/n.png", 14)
            imagebutton auto "prismap/ufsq/u_%s.png" focus_mask True action Call ("lowcool_", 10)
    
return
