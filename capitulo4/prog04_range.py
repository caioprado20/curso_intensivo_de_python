for values in range (6):
    print(values)
    
for values2 in range (1,6):
    print(values2)
    

numbers = list(range(1,6))
print(numbers)

even_numbers = list (range(2,11,2))#range(start, stop, step)
print(even_numbers)

squares =[]
for value3 in range(1,11):
    square = value3 ** 2
    squares.append(square)
print(squares)

squares2 =[]#mesma saída com menos codígo
for value4 in range (1,11):
    squares2.append(value4 ** 2)
print(squares2)    

## Usado a sitaxe list comprehension

squares3 = [values5 **2 for values5 in range (1,11)]
print(squares3)






