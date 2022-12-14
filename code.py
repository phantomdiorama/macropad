from adafruit_macropad import MacroPad

macropad = MacroPad()

text_lines = macropad.display_text(title="")

last_position = 0
while True:
    text_lines.show()
    key_event = macropad.keys.events.get()

    if key_event:
        if key_event.pressed:
            if key_event.key_number == 0:
                macropad.keyboard.press(macropad.Keycode.F13)
                macropad.keyboard.release_all()
            if key_event.key_number == 1:
                macropad.keyboard.press(macropad.Keycode.F14)
                macropad.keyboard.release_all()
            if key_event.key_number == 2:
                macropad.keyboard.press(macropad.Keycode.F15)
                macropad.keyboard.release_all()
            if key_event.key_number == 3:
                macropad.keyboard.press(macropad.Keycode.F16)
                macropad.keyboard.release_all()
            if key_event.key_number == 4:
                macropad.keyboard.press(macropad.Keycode.F17)
                macropad.keyboard.release_all()
            if key_event.key_number == 5:
                macropad.keyboard.press(macropad.Keycode.F18)
                macropad.keyboard.release_all()
            if key_event.key_number == 6:
                macropad.keyboard.press(macropad.Keycode.F19)
                macropad.keyboard.release_all()
            if key_event.key_number == 7:
                macropad.keyboard.press(macropad.Keycode.F20)
                macropad.keyboard.release_all()
            if key_event.key_number == 8:
                macropad.keyboard.press(macropad.Keycode.F21)
                macropad.keyboard.release_all()
            if key_event.key_number == 9:
                macropad.keyboard.press(macropad.Keycode.F22)
                macropad.keyboard.release_all()
            if key_event.key_number == 10:
                macropad.keyboard.press(macropad.Keycode.F23)
                macropad.keyboard.release_all()
            if key_event.key_number == 11:
                macropad.keyboard.press(macropad.Keycode.F24)
                macropad.keyboard.release_all()

    macropad.encoder_switch_debounced.update()

    if macropad.encoder_switch_debounced.pressed:
        macropad.mouse.click(macropad.Mouse.RIGHT_BUTTON)

    current_position = macropad.encoder

    if macropad.encoder > last_position:
        macropad.keyboard.press(macropad.Keycode.PAGE_UP)
        macropad.keyboard.release_all()
        last_position = current_position

    if macropad.encoder < last_position:
        macropad.keyboard.press(macropad.Keycode.PAGE_DOWN)
        macropad.keyboard.release_all()
        last_position = current_position
