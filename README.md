# Desert Media Art

## RGB Animation

The story for my animation is pretty simple and explainable from the lights themselves. The concept is to make an accident come to life from the ligths - a person waiting for the lights to turn green and hurry back home as quickly as he can. However, as soon as he starts speeding away, he gets into an accident. Afterwards, there's an animation showing that he's in an ambulance.

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
