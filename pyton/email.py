import re
vowels = 'aAeEIiOoUu'
text = "India is my country. kasodiyameet000@gmail.com .some rendoom text kasodiyamit1234@gmail.com"
vowels_1 = [ x for x in text if x in vowels.lower]
print(vowels_1)

patten = re.compile("[a-zA-Z0-9\.\-\_]+@+[a-zA-Z0-9]+\.[a-zA-Z]+")

result = patten.findall(text)
print(result)


