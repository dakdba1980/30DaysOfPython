print(3+4) # Addition
print(3-4) # Subtraction
print(3*4) # Multiplication
print(3/4) # Division
print(3**4) # Exponential
print(3%4) # Modulus

print('Anil Kumar Dasari') # String
print(type(True))         # Boolean
print(type(None))         # NoneType

print(type(10))          # Int
print(type(3.14))        # Float
print(type(3 + 4j))      # Complex number
print(type('Anil'))  # String
print(type([1, 2, 3]))   # List
print(type({'name':'Anil'})) # Dictionary
print(type({3.4, 6.14, 7.2}))    # Set
print(type((3.4, 6.14, 7.2)))    # Tuple
print(type(True))         # Boolean # Boolean
print(type(None))         # NoneType
print(type(b'Hello'))     # Bytes
print(type(bytearray(5))) # Bytearray
print(type(memoryview(bytes(5)))) # Memoryview
print(type(range(5)))     # Range

# Find an Euclidian distance between (2, 3) and (10, 8)
import math
point1 = (2, 3)
point2 = (10, 8)
distance = math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)
print(distance)          # Euclidean distance