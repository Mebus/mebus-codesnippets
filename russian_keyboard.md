# Setting different keyboard layouts for different keyboards

Use xinput to find your keyboards:

```
$ xinput 
⎡ Virtual core pointer                    	id=2	[master pointer  (3)]
⎜   ↳ Virtual core XTEST pointer              	id=4	[slave  pointer  (2)]
⎜   ↳ SynPS/2 Synaptics TouchPad              	id=11	[slave  pointer  (2)]
⎜   ↳ TPPS/2 IBM TrackPoint                   	id=12	[slave  pointer  (2)]
⎜   ↳ Logitech Performance MX                 	id=14	[slave  pointer  (2)]
⎜   ↳ E-Signal USB Gaming Keyboard            	id=16	[slave  pointer  (2)]
⎣ Virtual core keyboard                   	id=3	[master keyboard (2)]
    ↳ Virtual core XTEST keyboard             	id=5	[slave  keyboard (3)]
    ↳ Power Button                            	id=6	[slave  keyboard (3)]
    ↳ Video Bus                               	id=7	[slave  keyboard (3)]
    ↳ Sleep Button                            	id=8	[slave  keyboard (3)]
    ↳ Integrated Camera                       	id=9	[slave  keyboard (3)]
    ↳ AT Translated Set 2 keyboard            	id=10	[slave  keyboard (3)]
    ↳ ThinkPad Extra Buttons                  	id=13	[slave  keyboard (3)]
    ↳ Sennheiser Sennheiser 3D G4ME1          	id=15	[slave  keyboard (3)]
    ↳ E-Signal USB Gaming Keyboard            	id=17	[slave  keyboard (3)]
```

The keyboards are id 10 (laptop integrated) and id 17 (external keyboard). 

Now, set the external keyboard to be русский layout:

```
$ setxkbmap -device 17 ru
```

Done!
