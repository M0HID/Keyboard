# K75 - A lightweight, 75% mechanical keyboard

This is a 75% keyboard fully designed by me, including the PCB, case, and firmware. It is designed to use _KMK_, a circuitpython-based firmware for keyboards! I included a rotary encoder, as well as a few "action" keys on the side of the keyboard which can be reprogrammed to anything you want, such as media controls, text controls, or any kind of shortcut you can think of!
<img width="1268" height="754" alt="image" src="https://github.com/user-attachments/assets/38e0354e-5005-4768-8048-f297d6dada5c" />

### The PCB:
I wanted to create a challenge for myself, and so opted to use the simple _Xiao RP2040_ as the main MCU. This is however, quite limited in terms of I/O and so i had to make use of 2 MCP23017 io expanders! I also opted to use the QFP footprint on both of them which made things slightly easier to route, given the tight space but probably going to be really hard to solder :sob:
<img width="1546" height="591" alt="image" src="https://github.com/user-attachments/assets/6ec35b3e-9873-497e-8be6-51a103040575" />

### The BOM:
|              Item             | Part #                                                | Amount | Price [$] |
|:-----------------------------:|-------------------------------------------------------|--------|-----------|
| 0402 SMD Diodes               | C155378                                               | 82     | 2.87      |
| Akko cream yellow switches    | https://www.aliexpress.com/item/1005007665996795.html | 82     | 27.52     |
| Purple Keycap Set             | https://www.aliexpress.com/item/1005005622221680.html | 1      | 15.01     |
| Reverse Mount SK6812-Mini-E   | C5149201                                              | 86     | 5.91      |
| Xiao RP2040                   | 1597-102010428-ND                                     | 1      | 4.68      |
| MCP23017                      | C629439                                               | 2      | 3.03      |
| Mill-Max 0305 Hotswap Sockets | ED90584-ND                                            | 164    | 31.42     |
| 3D printed case shipping      |                                                       | 1      | 4.42      |
| PCB                           |                                                       |        | 26.94     |
| PCB mounted Stabilisers       | https://www.aliexpress.com/item/1005001632672798.html | 1      | 17.39     |
| Total                         |                                                       |        | 139.19    |
