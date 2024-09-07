def on_pin_pressed_p2():
    for index in range(5):
        basic.show_number(5 - index)
        music.play(music.tone_playable(262, music.beat(BeatFraction.QUARTER)),
            music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(392, music.beat(BeatFraction.WHOLE)),
        music.PlaybackMode.UNTIL_DONE)
    basic.show_string("Go")
input.on_pin_pressed(TouchPin.P2, on_pin_pressed_p2)
