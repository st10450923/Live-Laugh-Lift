init python:
    config.keymap['game_menu'].remove('K_ESCAPE')
    config.keymap['game_menu'].remove('mouseup_3')

default progress = 0
default item_text = ["Steak","Dumbell", "Syringe", "Big Chilli", "Forbidden Creatine", "Obsidian Kettlebell", "Growth Mindset", "Skeleton Silver Key", "Lighter", "Sigmanomicon book", "You've done it. You've summoned him."]
default choice = ""


label prologue:
    scene black 
    show text "You're enjoying a normal Saturday night braai, when all of a sudden... \n you see your beloved wife Melissa smooching some sexy bodybuilder! \n\nHow are you supposed to compete with that guy? \nHe's huge! \n\nThere's no way you could get shredded enough to win your wife back before the end of the braai!\n\n...unless...\n\n you find some way to summon the god of muscles himself to help you! \n\nThere must be something around here you can use to call the god of gains to aid you in these trying times..."
    pause
    return

label start:
    call prologue
    play music "venue_ambience.ogg" volume 2
    scene background # house
    call screen play_game # 
    pause
    return

label end:
    stop music
    stop sound
    stop audio
    scene black
    # with dissolve
    show text "YOU WON!"
    pause 5
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
        # imagebutton:
        #     focus_mask True idle "wife.png" action [SetVariable("choice", "wife"), Jump("end")]
        #     activate_sound "website_click.wav"
        imagebutton:
            focus_mask True idle "god.png" action [SetVariable("choice", "god"), Jump("end")]
            activate_sound "website_click.wav"

    use ui()

    if progress == 7:
        add "fog.png":
            alpha 0.3
    elif progress == 8:
        add "fog.png":
            matrixcolor TintMatrix("#ff9c9c")
            alpha 0.5
    elif progress == 9:
        add "fog.png":
            matrixcolor TintMatrix("#ff7171")
            alpha 1
    elif progress == 10:
        add "glow.png":
            alpha 1

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
            add "stat_9.png"

    
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
                    add "steak_icon.png" matrixcolor TintMatrix("#000000")
                else:
                    add "steak_icon.png" matrixcolor TintMatrix("#ffffff")
                if progress <2:
                    add "dumbell_icon.png" matrixcolor TintMatrix("#000000")
                else:
                    add "dumbell_icon.png" matrixcolor TintMatrix("#ffffff")
                if progress <3:
                    add "syringe_icon.png" matrixcolor TintMatrix("#000000")
                else:
                    add "syringe_icon.png" matrixcolor TintMatrix("#ffffff")
                if progress <4:
                    add "chili_icon.png" matrixcolor TintMatrix("#000000")
                else:
                    add "chili_icon.png" matrixcolor TintMatrix("#ffffff")
                if progress <5:
                    add "creatine_icon.png" matrixcolor TintMatrix("#000000")
                else:
                    add "creatine_icon.png" matrixcolor TintMatrix("#ffffff")
                if progress <6:
                    add "kettlebell_icon.png" matrixcolor TintMatrix("#000000")
                else:
                    add "kettlebell_icon.png" matrixcolor TintMatrix("#ffffff")
                if progress <7:
                    add "brain_icon.png" matrixcolor TintMatrix("#000000")
                else:
                    add "brain_icon.png" matrixcolor TintMatrix("#ffffff")
                if progress<8:
                    add "key_icon.png" matrixcolor TintMatrix("#000000")
                else:
                    add "key_icon.png" matrixcolor TintMatrix("#ffffff")
                if progress <9:
                    add "lighter_icon.png" matrixcolor TintMatrix("#000000")
                else:
                    add "lighter_icon.png" matrixcolor TintMatrix("#ffffff")
                if progress <10:
                    add "book_icon.png" matrixcolor TintMatrix("#000000")
                else:
                    add "book_icon.png" matrixcolor TintMatrix("#ffffff")
                yoffset(-835)
                xoffset(20)
                spacing (5)
            
                


            
    