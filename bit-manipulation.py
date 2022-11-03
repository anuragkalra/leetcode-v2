# Generate all binary strings of length n
def generateBitStrings(n):
    result = []
    for i in range(2**n, 2**(n + 1)):
        bitmask = bin(i)[3:]
        result.append(bitmask)
    return result

n = 3
print(generateBitStrings(n))
# ['000', '001', '010', '011', '100', '101', '110', '111']

# Add two binary strings
# In-built approach: convert both a, b to int type, add them, convert to bin
def addBinary(a, b):
    c = bin(int(a, 2) + int(b, 2))
    return c[2:]

a, b = '11', '1'
print(addBinary(a, b))

