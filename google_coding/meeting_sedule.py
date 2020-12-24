person_2 = [[9.00, 10.30],
            [12.00, 13.00],
            [16.00, 18.00]]
daily_bound_person1 = [9.00, 20.00]
person_1 = [[10.00, 11.30], [12.30, 14.30], [16.00, 17.00]]
daily_bound_person2 = [10.00, 18.00]


def free_time(person, dail_bound):
    temp = list()

    if person[0][0] > dail_bound[0]:
        x = list()
        x.append(dail_bound[0])
        x.append(person[0][0])

        temp.append(x)

    for i in range(len(person) - 1):
        j = 0
        x = list()
        x.append(person[i][j + 1])
        x.append(person[i + 1][j])
        if person[i][j + 1] != person[i + 1][j]:
            temp.append(x)

    if person[len(person) - 1][1] < dail_bound[1]:
        x = list()
        x.append(person[len(person) - 1][1])
        x.append(dail_bound[1])

        temp.append(x)

    return temp


def check_free_time(person1, person2):
    temp = list()
    for i in range(min(len(person_1) - 1, len(person_2) - 1)):
        if len(person1) <= len(person2):
            person = person1
        else:
            person = person2
        first_element_person1 = person[i][0]
        second_element_person1 = person[i][1]

        for j in range(max(len(person1) - 1, len(person2) - 1)):
            if len(person_1) < len(person_2):
                person = person2
            else:
                person = person1
            first_element_person2 = person[j][0]
            second_element_person2 = person[j][1]

            # minimum = min(first_element_person1, first_element_person2)
            maximum = max(first_element_person1, first_element_person2)

            minimum_1 = min(second_element_person1, second_element_person2)

            if second_element_person1 == second_element_person2:
                minimum_1 = second_element_person2
            if maximum < minimum_1:
                x = list()
                x.append(maximum)
                x.append(minimum_1)
                temp.append(x)

    print(temp)


free_time_person1 = free_time(person_1, daily_bound_person1)
free_time_person2 = free_time(person_2, daily_bound_person2)

print(free_time_person1)
print(free_time_person2)

check_free_time(free_time_person1, free_time_person2)
