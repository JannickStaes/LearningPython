#! python3
# BulletPointAdder.py: Adds Wikipedia bullet points to the start
# of each line of text in the clipboard

import pyperclip

text = pyperclip.paste()

#separate lines and add stars
lines = text.split('\r\n')
for i in range(len(lines)):
    lines[i] = '* ' + lines[i]
text = '\n'.join(lines)

pyperclip.copy(text)


