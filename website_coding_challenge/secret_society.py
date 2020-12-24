"""
A group of friends have decided to start a secret society. The name will be the first letter of each of their names, sorted in alphabetical order.

Create a function that takes in a list of names and returns the name of the secret society.

society_name(["Adam", "Sarah", "Malcolm"]) ➞ "AMS"

society_name(["Harry", "Newt", "Luna", "Cho"]) ➞ "CHLN"
"""

secret_name = list()


def society_name(name_society):
    return ''.join(sorted(i[0] for i in name_society))


friend = ["Adam", "Sarah", "Malcolm"]
print(society_name(friend))
