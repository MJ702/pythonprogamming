import numpy as np

a = np.arange(0, 9, 1).reshape(3, 3)
print(a)

a_ins = np.insert(a, 1, [11, 12, 13], axis=1)
print(a_ins)

a_del = np.delete(a_ins, 2, axis=0)
print(a_del)

a_row = np.append(a, [[10, 11, 12]], axis=0)
print(a_row)
