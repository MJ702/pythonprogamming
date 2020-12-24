import re

text = " 123 This is the some dumpy text 1990, 2001"

patten = re.compile("[0-9]")

result = patten.findall(text)
print(result)
