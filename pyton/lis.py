name = ['raj', 'krana', 'yes']

l = []
print([person for person in name])

for person in name:
    l.append(person + ' mental. ')
print(l)

print([person + ' mental.' for person in name])
l = []
movies_and_rating = {
    'Marri':9 ,
    'Marri_2': 9.1,
    'Don': 3,
    'Don_2': 6
}

for movie in movies_and_rating:
    if movies_and_rating[movie] > 6:
        l.append(movie)
print(l)

l = []

print( [ movie for movie in movies_and_rating if movies_and_rating[movie] >6])