## Steps
### Step 1:
`git clone https://github.com/syminical/PUK.git`

### Step 2:
`tshark -r chal.pcapng -Y "usbhid.data" -T fields -e usbhid.data | grep -E "." | grep -v '0000000000000000' > capdata.txt`

### Step 3:
`python3 PUK.py capdata.txt`
```
You successfully decodee the text!!

KKKbackspacebackspaceLlee me gibbbackspacebackspaceee you the flgg thenKEY_DOTKEY_DOTKEY_DOT UuwU

hkco2026{Tth1s_-1s_-a_-H1dden_-fl4g_-typ3d_-by_-my_-USB_-kbackspaceKk3yb0aabackspacerd}]
```

### Step 4:
Remove those "backspace":

`hkco2026{Tth1s_-1s_-a_-H1dden_-fl4g_-typ3d_-by_-my_-USB_-Kk3yb0ard}]`

### Step 5:
Next, the keyboard sends traffic whenever the input state changes (e.g., from `SHIFT + -` to `-`, or from `SHIFT + t` to `t`). If the interval between these state changes is short enough, the operating system will not register a new key press. Because of this, you may see doubled characters (like `Tth1s` or `_-`) in the captured flag.

_Example_:
|Packet #|Time|HID Data|Notes|
|---|---|---|---|
|609|46.978516|0000000000000000|Released all keys|
|611|47.690721|2000000000000000|Pressed `Shift`|
|613|47.809621|20002d0000000000|Pressed `Shift` + `-` -> `_`|
|615|47.809720|00002d0000000000|Released `Shift`, only holding `-`|
|617|47.906570|0000000000000000|Released all keys|
- In the sequence for Packets `613` -> `615` -> `617`, the duration between state changes is so short that the operating system does not register them as separate key presses. However, when parsing the raw HID data, you will see `_-` instead of just `_`.

`hkco2026{Th1s_1s_a_H1dden_fl4g_typ3d_by_my_USB_K3yb0ard}`

## Flag
```
hkco2026{Th1s_1s_a_H1dden_fl4g_typ3d_by_my_USB_K3yb0ard}
```

Reference: https://medium.com/@alyangulzar149/how-to-solve-wireshark-usb-packet-data-challenges-in-ctfs-snyk-ctf-428302d9eb4d