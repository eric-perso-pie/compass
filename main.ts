let degrees = 0
basic.forever(function () {
    degrees = 0
    if (degrees > 315 || degrees < 45) {
        basic.showString("N")
    } else if (degrees < 135) {
        basic.showString("E")
    } else if (degrees < 225) {
        basic.showString("S")
    } else {
        basic.showString("W")
    }
})
