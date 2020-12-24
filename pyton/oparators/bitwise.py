# bitwise operators are used to compare binary number
# &, | , ^ ,~ , << , >>

# bitwise AND
print("\nAND")
print(10 & 4)

"""
    Returns 1 if both the bits are 1 else 0.
    a = 10 = 1010 (Binary)
    b = 4 =  0100 (Binary

    a & b = 1010
              &
            0100
            = 0000
            = 0 (Decimal)
"""

# bitwise OR
print("\nOR")
print(10 | 4)

"""
    Returns 1 if either of the bit is 1 else 0.
    a = 10 = 1010 (Binary)
    b = 4 =  0100 (Binary

    a & b = 1010
            |
            0100
          = 1110
          = 14 (Decimal)
"""

# bitwise XOR
print("\nXOR")
print(10 ^ 12)

"""
    Returns 1 if one of the bit is 1 and other is 0 else returns false.
    a = 10 = 1010 (Binary)
    b = 4 =  0100 (Binary

    a & b = 1010
            ^
            0100
          = 1110
          = 14 (Decimal)
"""

# bitwise NOT
print("\nNOT")
print(~10)
"""
    Returns one’s compliement of the number.
    a = 10 = 1010 (Binary)

    ~a = ~1010
       = -(1010 + 1)
       = -(1011)
       = -11 (Decimal)
"""

# bitwise left shift
print("\nLEFT SHIFT")
print(5 << 1)
print(5 << 2)

"""
    
        a = 5  = 0000 0101
        a << 1 = 0000 1010 = 10
        a << 2 = 0001 0100 = 20 
"""

# bitwise right shift
print("\nRIGHT SHIFT")
print(5 >> 1)
print(5 >> 2)
