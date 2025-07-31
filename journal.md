---
title: "K75"
author: "@m0.hid"
description: "A 75% keyboard with per-key rgb lighting, a rotary encoder and usb-c!"
created_at: "2025-06-25"
---

### Making the schematic
Made the schematic, using 1x xiao rp2040, 1 rotary encoder, 2x i/o expanders (since the xiao itself doesnt have enough pins), and leds for each switch.
I tried doing something to make this process more automatic using hierarchal sheets but ended up just doing it all manually
Schematic:
<img width="1282" height="853" alt="image" src="https://github.com/user-attachments/assets/33b96beb-f2e8-4b9f-84fb-80c5cb5cf2a2" />
Time += 3 hours

### Positioning all the components
Opened up the pcb editor, and put all the footprints where they're supposed to go.
I placed the xiao rp2040 underneath one of the switches on the left so it doesnt take up any extra room on the pcb. This should make it one clean board with nothing sticking out of it!  
Also i opted to use smaller 0402 smd diodes since they're smaller, hopefully i'll be able to reflow them :sob:
Started doing some of the routing as well
<img width="1558" height="613" alt="image" src="https://github.com/user-attachments/assets/94a7cdf6-979a-4fe7-9b44-bcaaee1556bb" />
TIme += 2 hours

### Continue routing
I decided to modify the diode footprint a bit, so that it has a via underneath, which should hopefully make it a bit easier to route.
<img width="316" height="319" alt="image" src="https://github.com/user-attachments/assets/4ccf6dd8-03f6-48b1-a318-6f72d4e9669e" />
Finished up the rows as well
<img width="1546" height="594" alt="image" src="https://github.com/user-attachments/assets/f40c0edd-bc3d-437e-8e53-5de9e021596a" />
Time += 2 hours

### I/O expander
Added in one of the io expanders, underneath the enter key so it should have space to route wires to. did most of the wiring for that today.
<img width="1237" height="820" alt="image" src="https://github.com/user-attachments/assets/a7a82fb8-dc3c-4e65-9788-d0bfd5eedb2d" />
Time += 2 hours

### the other I/O expander
Today I added in the other io expander, and started finishing up the routing. I think all the routing is done now. There wasnt much space for this one but i managed to squeeze it between the 2 function keys f4 and f5 since they have a gap between them.
<img width="1539" height="587" alt="image" src="https://github.com/user-attachments/assets/3769ad56-f21b-490f-a3da-8542c636c851" />
Routing it was pretty difficult since there wasnt much space to fit vias or anything, so i tried re-assigning the labels in the schematic so they'd be physically closer to where they need to be 
<img width="1124" height="704" alt="image" src="https://github.com/user-attachments/assets/1559ca63-a48d-45fa-988d-75d23602e31a" />
Time += 4 hours

### Oled screen?
no

Sadly, i spent a bunch of time, trying different arrangements to fit one in, but it just wouldnt work without significant reworks (which i am not bothered to do :pray:). Maybe I'll design another kb in the future which has sone but until then, ill have to survive without one
<img width="1552" height="667" alt="image" src="https://github.com/user-attachments/assets/eba648a9-eca6-46cd-8cc3-d0653f502b32" />

### the 3d model!
I spent sooo long assigning the 3d models to each component, and ended up with a pretty good representation of what the kb will look like:
<img width="1038" height="410" alt="image" src="https://github.com/user-attachments/assets/4c007a95-8f63-4ca1-ae1f-99449de3853e" />
Time += 2 hours

And thats it for the pcb!! Moving on to the...

# the Case
Gonna try making something like this:
<img width="480" height="236" alt="image" src="https://github.com/user-attachments/assets/014f3400-aca6-4a06-8766-30435c7ab77f" />

I made the plate using https://www.keyboard-layout-editor.com/, and then https://kbplate.ai03.com/.
Imported that in fusion, then made it 1.5mm thick and extruded the upper lip kind of thing
<img width="1398" height="528" alt="image" src="https://github.com/user-attachments/assets/ebf507d3-2766-4a92-9c0f-d546b8d2c12e" />

