    screen adein_():

        frame:
            xsize 700 ysize 700 xalign 0.5 yalign 0.5
            at transform:
                alpha 0 
                pause 0.5 
                linear 2 alpha 1.0 
            vbox:
                xsize 565 xalign 0.5 yalign 0.5 
                text "ADEIN" xalign 0.5 size 65 text_align 0.5 kerning 50 
                text "\n\nÉ uma Novela Visual e Interativa desenvolvida com o propósito de difundir e incentivar o estudo do autoconhecimento humano através da análise de sentimentos e padrões de repetição relacionados à características que definem os principais traços de personalidade conhecidos:\n\n{s}A{/s}mabilidade, {s}D{/s}espreocupação, {s}E{/s}xtroversão, {s}I{/s}ntelectualidade e {s}N{/s}euroticismo.\n\n{s}A D E I N{/s}\n\nFoi elaborada como trabalho de conclusão do curso de Sistemas de Informação na Universidade Federal de Santa Catarina.\n\n2020.02\n\n" text_align 0.5 size 22 
                textbutton "ok" xalign 0.5:
                    action Return(True)
