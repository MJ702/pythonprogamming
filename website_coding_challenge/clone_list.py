"""
clone list
input list = [1, 2]
output list = [1, 2, [1, 2]]

"""

temp = [1, 2]
temp.append(temp[:])
print(temp)