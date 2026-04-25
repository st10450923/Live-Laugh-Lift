default progress = 0
default item_text = ["Steak","Protein Shake", "Dumb dfoasdfohsdhfuoihsdfoiuhsdouifh Bells", "Syringe", "Big Chilli", "Skeleton Silver Key", "Obsidian Kettlebell", "Growth Mindset", "Forbidden Creatine", "Sigmanomicon book", "Now... make your choice. Who do you choose?"]
default choice = ""

label start:
    play music "venue_ambience.ogg" volume 2
    scene background # house
    call screen play_game # 
    pause
    return

label end:
    show win
    with dissolve
    if choice == "wife":
        show text "You chose your wife!"
    else:
        show text "You chose the Eldritch God!"
    pause 10
    return

screen play_game:

    
    imagebutton:
        focus_mask True idle "item_1.png" action SetVariable("progress", 1) sensitive progress == 0
        activate_sound "website_click.wav"
    imagebutton:
        focus_mask True idle "item_2.png" action SetVariable("progress", 2) sensitive progress == 1
        activate_sound "website_click.wav"
    if progress < 1:
        add "block_out.png"
    imagebutton:
        focus_mask True idle "item_3.png" action SetVariable("progress", 3) sensitive progress == 2
        activate_sound "website_click.wav"
    imagebutton:
        focus_mask True idle "item_4.png" action SetVariable("progress", 4) sensitive progress == 3
        activate_sound "website_click.wav"
    imagebutton:
        focus_mask True idle "item_5.png" action SetVariable("progress", 5) sensitive progress == 4
        activate_sound "website_click.wav"
    imagebutton:
        focus_mask True idle "item_6.png" action SetVariable("progress", 6) sensitive progress == 5
        activate_sound "website_click.wav"
    imagebutton:
        focus_mask True idle "item_7.png" action SetVariable("progress", 7) sensitive progress == 6
        activate_sound "website_click.wav"
    imagebutton:
        focus_mask True idle "item_8.png" action SetVariable("progress", 8) sensitive progress == 7
        activate_sound "website_click.wav"
    imagebutton:
        focus_mask True idle "item_9.png" action SetVariable("progress", 9) sensitive progress == 8
        activate_sound "website_click.wav"
    imagebutton:
        focus_mask True idle "item_10.png" action SetVariable("progress", 10) sensitive progress == 9
        activate_sound "website_click.wav"
    if progress == 10:
        imagebutton:
            focus_mask True idle "wife.png" action [SetVariable("choice", "wife"), Jump("end")]
            activate_sound "website_click.wav"
        imagebutton:
            focus_mask True idle "god.png" action [SetVariable("choice", "god"), Jump("end")]
            activate_sound "website_click.wav"

    use ui()

screen ui:

    # character stat screen

    hbox:
        align(0,0)
        offset(20,20)
        if progress == 0:
            add "stat_0.png"
        elif progress == 1:
            add "stat_1.png"
        elif progress == 2:
            add "stat_2.png"
        elif progress == 3:
            add "stat_3.png"
        elif progress == 4:
            add "stat_4.png"
        elif progress == 5:
            add "stat_5.png"
        elif progress == 6:
            add "stat_6.png"
        elif progress == 7:
            add "stat_7.png"
        elif progress == 8:
            add "stat_8.png"
        elif progress == 9:
            add "stat_9.png"
        elif progress == 10:
            add "stat_10.png"

    
    # Textbox to get this item
    hbox:
        align(0.5,0)
        yoffset 30
        
        frame:
            yminimum 80
            padding (100, 15)
            background Frame("text_frame.png", 290, 18)
            if progress != 10:
                text "Where is the [item_text[progress]]?":
                    color "#fff"
                    outlines [ ( 4, "#000005") ]
                    outline_scaling "linear"
            
            else:
                text "[item_text[progress]]":
                    color "#fff"
                    outlines [ ( 4, "#000005") ]
                    outline_scaling "linear"
    
    # half-implemented below:

    hbox:
        align(0.98,0.5)
        add "item_bar.png"

            # add "item_bar.png"
                # for i in range(10):
                #     vbox:
                #         add "item_circle.png"



    vbox:
        align (0.98, -0.2)  # Centers the vbox on the screen
        spacing 5        # Adds 10 pixels of vertical space between images
        frame:
            xysize (120, 850)
            padding (20, 15)    
            background Frame("images/item_bar.png", gui.notify_frame_borders, tile=gui.frame_tile)
        for i in range (10):
            vbox:
                add "item_circle.png"
                xysize(20,20)
                yoffset(-835)
                xoffset(20) 

    vbox:
        align (0.98, -0.2)  # Centers the vbox on the screen
        spacing 5        # Adds 10 pixels of vertical space between images
        frame:
            xysize (120, 850)
            padding (20, 15)    
            background None
        for i in range (1):
            vbox:
                if progress <1:
                    add "dumbell_icon.png" matrixcolor TintMatrix("#000000")
                else:
                    add "dumbell_icon.png" matrixcolor TintMatrix("#ffffff")
                if progress <2:
                    add "dumbell_icon.png" matrixcolor TintMatrix("#000000")
                else:
                    add "dumbell_icon.png" matrixcolor TintMatrix("#ffffff")
                if progress <3:
                    add "dumbell_icon.png" matrixcolor TintMatrix("#000000")
                else:
                    add "dumbell_icon.png" matrixcolor TintMatrix("#ffffff")
                if progress <4:
                    add "dumbell_icon.png" matrixcolor TintMatrix("#000000")
                else:
                    add "dumbell_icon.png" matrixcolor TintMatrix("#ffffff")
                if progress <5:
                    add "dumbell_icon.png" matrixcolor TintMatrix("#000000")
                else:
                    add "dumbell_icon.png" matrixcolor TintMatrix("#ffffff")
                if progress <6:
                    add "dumbell_icon.png" matrixcolor TintMatrix("#000000")
                else:
                    add "dumbell_icon.png" matrixcolor TintMatrix("#ffffff")
                if progress <7:
                    add "dumbell_icon.png" matrixcolor TintMatrix("#000000")
                else:
                    add "dumbell_icon.png" matrixcolor TintMatrix("#ffffff")
                if progress<8:
                    add "dumbell_icon.png" matrixcolor TintMatrix("#000000")
                else:
                    add "dumbell_icon.png" matrixcolor TintMatrix("#ffffff")
                if progress <9:
                    add "dumbell_icon.png" matrixcolor TintMatrix("#000000")
                else:
                    add "dumbell_icon.png" matrixcolor TintMatrix("#ffffff")
                if progress <10:
                    add "dumbell_icon.png" matrixcolor TintMatrix("#000000")
                else:
                    add "dumbell_icon.png" matrixcolor TintMatrix("#ffffff")
                yoffset(-835)
                xoffset(20)
                spacing (5)
            
                


            
    