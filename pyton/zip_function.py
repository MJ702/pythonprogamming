list1 = [1, 2, 3, 4, 5, 6]
list2 = ['one' ,'two' ,'three' ,'four' ,'five']
#both list element same if first
#element have a 6 element and second element have 5 so out will be 5 element
zipped = list(zip(list1, list2))
print(zipped)

unzziped = list(zip(*zipped))
print(unzziped)

for (l1, l2) in zip(list1 , list2):
    print(l1)
    print(l2)

iteams = ['Apple', 'Banana','Orange']
counts = [5 ,7 ,4]
prices = [45, 85 , 63]

sentences = []

for (iteam, count, price) in zip(iteams, counts , prices):
    sentence = 'I bought ' + str(count) + ' ' + iteam + 's at ' + str(price) + '.'
    sentences.append(sentence)

print(sentences)