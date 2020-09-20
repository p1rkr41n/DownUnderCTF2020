# In a pickle - MISC - 200pts.

## Attachments
###### data
```
(dp0
I1
S'D'
p1
sI2
S'UCTF'
p2
sI3
S'{'
p3
sI4
I112
sI5
I49
sI6
I99
sI7
I107
sI8
I108
sI9
I51
sI10
I95
sI11
I121
sI12
I48
sI13
I117
sI14
I82
sI15
I95
sI16
I109
sI17
I51
sI18
I53
sI19
I53
sI20
I52
sI21
I103
sI22
I51
sI23
S'}'
p4
sI24
S"I know that the intelligence agency's are onto me so now i'm using ways to evade them: I am just glad that you know how to use pickle. Anyway the flag is "
p5
s.
```

## Solution
After taking a look at `data.txt` i noticed the bottom sentence `I am just glad that you know how to use pickle`.
At this point i knew that pickle was required to decode the data, so i wrote this simple script:

```python3
#!/usr/bin/python3

import pickle

flag = ""

with open('data', 'rb') as f:
    unpack = pickle.load(f)

print(unpack)

for i in range(1, len(unpack)):
    try:
        flag += chr(unpack[i])
    except:
        flag += unpack[i]

print(flag)
```

The output was: `DUCTF{p1ckl3_y0uR_m3554g3}`
