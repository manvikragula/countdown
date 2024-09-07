input.onPinPressed(TouchPin.P2, function () {
    for (let index = 0; index <= 4; index++) {
        basic.showNumber(5 - index)
        music.play(music.tonePlayable(262, music.beat(BeatFraction.Quarter)), music.PlaybackMode.UntilDone)
    }
    music.play(music.tonePlayable(392, music.beat(BeatFraction.Whole)), music.PlaybackMode.UntilDone)
    basic.showString("Go")
})
