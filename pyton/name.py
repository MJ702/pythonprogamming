friend=['jay','raj','sero','ram','syam']
for i in friend:
    message='Good moring '+ i
    print(message)
friend.append('xyz')
friend.insert(6,'abc')
#del friend[6]
remove_friend=friend.pop()
#print(friend)
remove_friend=friend.pop()
#print(friend)
friend.remove('jay')
print(friend)
