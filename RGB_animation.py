# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""CircuitPython Essentials Internal RGB LED red, green, blue example"""
import time
import board

if hasattr(board, "APA102_SCK"):
    import adafruit_dotstar

    led = adafruit_dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1)
else:
    import neopixel

    led = neopixel.NeoPixel(board.NEOPIXEL, 1)

led.brightness = 0.1
a = 0
b = 255


while True:
    print('On the way to my home, I run into some traffic')
    while (a<=255) and (b>=0): #
        led[0] = (0, a, b)
        time.sleep(0.07)
        a+=1
        b-=1

    a = 0
    b = 255

    led[0] = (255, 0, 0)
    time.sleep(3)
    print('The red light is taking years to go away')
    time.sleep(1)
    print('It is still there')
    time.sleep(1)
    led[0] = (255, 120, 0)
    print()
    print()
    print('It is finally yellow')
    time.sleep(1.2)
    led[0] = (0, 255, 0)
    print('Gotta hurry, it is green')
    print('Hurrying... hurrying... --')
    time.sleep(2)

    led[0] = (0, 0, 0)
    time.sleep(4)

    print()
    print()
    print()
    print()
    print()
    print('Huh? What happened? I needed to hurry home')
    for z in range(3):
        for x in range(3):
            while a<=255:
                led[0] = (a, 0, 0)
                time.sleep(0.001)
                a+=1

            while b>=0:
                led[0] = (b, 0, 0)
                time.sleep(0.001)
                b-=1

            a=0
            b=255

        for y in range(3):
            led[0] = (0, 0, 255)
            time.sleep(0.3)
            led[0] = (255, 0, 0)
            time.sleep(0.3)

        print('I am okay...I said I am okay....--')

    print()
    print()
    print()

