//  Moving
input.onPinPressed(TouchPin.P0, function on_pin_pressed_p0() {
    radio.sendValue("key", cislo)
})
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    cislo = Math.constrain(cislo, 1, 75)
    cislo += 0 - 1
    basic.showString(String.fromCharCode(cislo + 64))
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    cislo = Math.constrain(cislo, 1, 5)
    cislo += 1
    basic.showString(String.fromCharCode(cislo + 64))
})
//  Start/Stop server
radio.onReceivedValue(function on_received_value(name: string, value: number) {
    
    remote_serial = radio.receivedPacket(RadioPacketProperty.SerialNumber)
    if (name == "vote") {
        start = value
        console.log(start)
    }
    
    if (start == 1 && name == "key") {
        music.playTone(262, 200)
        basic.showString(String.fromCharCode(cislo))
    }
    
})
input.onLogoEvent(TouchButtonEvent.Pressed, function on_logo_pressed() {
    
    if (start == 0) {
        start = 1
    } else {
        start = 0
    }
    
    radio.sendValue("vote", start)
})
let remote_serial = 0
let cislo = 0
let start = 0
pins.touchSetMode(TouchTarget.P0, TouchTargetMode.Capacitive)
radio.setGroup(69)
radio.setTransmitPower(7)
radio.setTransmitSerialNumber(true)
cislo = 1
let data_list = [0]
console.log(control.deviceSerialNumber())
