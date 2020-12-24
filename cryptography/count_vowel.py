text = "Lorem Ipsum "
vowels = 'aAeEIiOoUu'
vowels_1 = [x for x in text if x in vowels]
constant = [x for x in text if x not in vowels]
print("vowels = " + str(vowels_1))
print("vowles = ", len(vowels_1))
print("constant = " + str(constant))
print("constant = ", len(constant))
