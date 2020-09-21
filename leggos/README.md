# Leggos - WEB - 100pts.

## Description
I <3 Pasta! I won't tell you what my special secret sauce is though!

https://chal.duc.tf:30101

## Attachments
_None_

## Solution
After opening the provided link i was greeted by a nice jar of bolognese sauce.

![site](https://github.com/SamIsland/writeups/blob/master/leggos/page.PNG)

I tried to view the page source, but ctrl+U and right-click was blocked by the site.

![not_allowed](https://github.com/SamIsland/writeups/blob/master/leggos/not_allowed.PNG)

Luckly that restriction could be easily bypassed by hitting F12 and opening the source tab where 
i found a file named `disableMouseRightClick.js` containing the flag.

![flag](https://github.com/SamIsland/writeups/blob/master/leggos/flag.PNG)

`DUCTF{n0_k37chup_ju57_54uc3_r4w_54uc3_9873984579843}`
