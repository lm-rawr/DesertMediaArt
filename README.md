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
