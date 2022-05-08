# Moving

def on_pin_pressed_p0():
    radio.send_value("key", cislo)
input.on_pin_pressed(TouchPin.P0, on_pin_pressed_p0)

def on_button_pressed_a():
    global cislo
    cislo = Math.constrain(cislo, 1, 75)
    cislo += 0 - 1
    basic.show_string(String.from_char_code(cislo + 64))
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global cislo
    cislo = Math.constrain(cislo, 1, 5)
    cislo += 1
    basic.show_string(String.from_char_code(cislo + 64))
input.on_button_pressed(Button.B, on_button_pressed_b)

# Start/Stop server

def on_received_value(name, value):
    global remote_serial, start
    remote_serial = radio.received_packet(RadioPacketProperty.SERIAL_NUMBER)
    if name == "vote":
        start = value
        print(start)
    if start == 1 and name == "key":
        music.play_tone(262, 200)
        basic.show_string(String.from_char_code(cislo))
radio.on_received_value(on_received_value)

def on_logo_pressed():
    global start
    if start == 0:
        start = 1
    else:
        start = 0
    radio.send_value("vote", start)
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

remote_serial = 0
cislo = 0
start = 0
pins.touch_set_mode(TouchTarget.P0, TouchTargetMode.CAPACITIVE)
radio.set_group(69)
radio.set_transmit_power(7)
radio.set_transmit_serial_number(True)
cislo = 1
data_list = [0]
print(control.device_serial_number())