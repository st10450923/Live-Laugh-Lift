default progress = 0

label start:
    
    scene background # house
    call screen play_game # 


    

    return


screen play_game:

    
    
    imagebutton:
        focus_mask True idle "item_1.png" action SetVariable("progress", 1) sensitive progress == 0
    
    imagebutton:
        focus_mask True idle "item_2.png" action SetVariable("progress", 2) sensitive progress == 1
    if progress < 1:
        add "block_out.png"
    imagebutton:
        focus_mask True idle "item_3.png" action SetVariable("progress", 3) sensitive progress == 2
    imagebutton:
        focus_mask True idle "item_4.png" action SetVariable("progress", 4) sensitive progress == 3
    
    use ui()

screen ui:


    # Textbox to get this item
    hbox:
        align(0.5,0)
        frame:
            padding (20, 15)
            text "Get item [progress]!"
            background Frame("gui/notify_black.png", gui.notify_frame_borders, tile=gui.frame_tile)


    # Please help here!
    # Vertical box with blacked out items depending on progress

    # vbox:
        # align(1,0.5) # far right on screen
        # add "item_bar.png"
    #     etc
    

    