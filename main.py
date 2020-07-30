degrees = 0

def on_forever():
    global degrees
    degrees = 0
    if degrees > 315 or degrees < 45:
        basic.show_string("N")
    elif degrees < 135:
        basic.show_string("E")
    elif degrees < 225:
        basic.show_string("S")
    else:
        basic.show_string("W")
basic.forever(on_forever)

