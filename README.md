# Desert Media Art

## RGB Animation

### Concept
The story for my animation is pretty simple and explainable from the lights themselves. The concept is to make an accident come to life from the ligths - a person waiting for the lights to turn green and hurry back home as quickly as he can. However, as soon as he starts speeding away, he gets into an accident. Afterwards, there's an animation showing that he's in an ambulance.

### Cool Snippet
A code snippet that I am particularly proud of is below. There, I replicated the lights of an ambulance siren. The fade in-fade out transition of the red is done by making the colors go to red then to black and then back to red again and so forth. While the red to blue jump is just a general switch from a color to another.

        for x in range(3): #the initial faded blinking of the red
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

        for y in range(3): #the red-blue blink pattern
            led[0] = (0, 0, 255)
            time.sleep(0.3)
            led[0] = (255, 0, 0)
            time.sleep(0.3)


### Reflection
#### General Thoughts
I felt like getting a story out of just lights was a little too much to ask for in the beginning because there's just one light changing colors and a story or an experience encompasses a lot more elements than a fancy blinking light. However, as I started fiddling around and playing with the colors, I could see different patterns that could represent certain things - like the traffic lights and the ambulance lights. So, I just went with whatever I found was interesting and made a short story. However, the lights by themselves still felt like they couldn't convey what I was trying to so I added a few lines of text for the viewers to see on the serial monitor regarding what actually is going on. 

#### Things I could improve on
I feel like the story is still a little superficial and not very well thought out and i could flesh it out a little more. I also feel like I could've made my code a lot tidier and more concise than how it looks at the moment. Other than that, I think this is the best I could come up with and am willing to improve with time to come.



## Jyotiphul - Prototype

### Concept
'Jyotiphul' is a Nepali word that translates to 'light flower' in English. My prototype is exactly as the name suggests - it is a flower that adores light. I feel like in some way or form, such an adaptation may happen to beings in the places where the sun rarely sets as they learn to get everything  from the sunlight. 

### Interaction
The mechanism behind the interation of this being is very simple. Whenever it sees light, it gives out happy vibes with yellow colors on its crown and when it gets dark, the yellow turns to red, which suggests that it is irritated.

### Technical Implementation
![WhatsApp Image 2023-10-08 at 22 20 59](https://github.com/lm-rawr/DesertMediaArt/assets/78416925/b7f8130e-cdce-4711-83ef-ddfdeff1d29f)

https://github.com/lm-rawr/DesertMediaArt/assets/78416925/75c82494-6719-4ca1-8436-b28f31d5dde0

![WhatsApp Image 2023-10-08 at 22 20 47](https://github.com/lm-rawr/DesertMediaArt/assets/78416925/a9c4990c-7fee-498b-b3fe-fde1b45ebe41)

As seen in the images above, a single photocell is being used with an RGB led ring. The photocell detects how much light is getting to the roots of the plant and if there's enough light, the plant is happy with the yellow glow on the led ring. Whenever the light getting to the photocell is blocked ny an external force or it gets dark, the led ring glows red.

#### Schematic
![WhatsApp Image 2023-10-08 at 22 57 21](https://github.com/lm-rawr/DesertMediaArt/assets/78416925/250c8b0d-936a-4f77-aacc-e241dd050482)


#### Code
        import time
        
        import board
        import analogio
        # SPDX-FileCopyrightText: 2019 Kattni Rembor for Adafruit Industries
        #
        # SPDX-License-Identifier: MIT
        #
        # Modified by Mangtronix for Desert Media Art at NYUAD
        # https://desert.nyuadim.com
        
        """Simple rainbow example for 12-pixel NeoPixel ring"""
        
        print("Starting neoring")
        
        import digitalio
        import board
        from rainbowio import colorwheel
        import neopixel
        
        
        NUM_PIXELS = 12  # NeoPixel ring length (in pixels)
        BRIGHTNESS = 0.25 # Let's not blind everyone
        
        # The power for the NeoPixels is not enabled by default (to save battery power)
        # We need to turn on the power by setting pin D10 high
        print("Enabling NeoPixel power!")
        enable = digitalio.DigitalInOut(board.D10)
        enable.direction = digitalio.Direction.OUTPUT
        enable.value = True
        
        # Initialize analog input connected to photocell.
        photocell = analogio.AnalogIn(board.A1)
        
        # Make a function to convert from analog value to voltage.
        def analog_voltage(adc):
            return adc.value / 65535 * adc.reference_voltage
        
        strip = neopixel.NeoPixel(board.D5, NUM_PIXELS, brightness=BRIGHTNESS)
        
        while True:
             # Read the value, then the voltage.
            val = photocell.value
            volts = analog_voltage(photocell)
            # Print the values:
            print('Photocell value: {0} voltage: {1}V'.format(val, volts))
            # Delay for a second and repeat!
            time.sleep(1.0)
            if val <= 500:
                strip.fill((colorwheel(0)))
            else:
                strip.fill((colorwheel(30)))

### Self Reflection
Initially I wanted it to be an animal and not a plant, meaning I wanted it/a part of it to be movable. However, I couldn't figure out how I'd fit a servo motor in this prototype. So, I am a bit unhappy about the result at the moment because of how few the components are. Other than that, with the components I have used, I think I am pretty happy with how they are implemented. I think the wires could be organized better though.






