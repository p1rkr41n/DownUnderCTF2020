#!/usr/bin/python3

alphabet = "abcdefghijklmnopqrstuvwxyz"
encoded = "iajbo{ndldie_al_aqk_jjrnsxee}"
start = 5
flag = ""

for c in encoded:
    if c in alphabet: flag += alphabet[alphabet.find(c)-start%26]
    else: flag += c

    start += 1

print(flag)
