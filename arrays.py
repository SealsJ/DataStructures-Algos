#array memory is contiguous with no gaps
new_list = [1, 2, 3]
#since we are in python, array stores references to where the values are in memory
#different than other languages that just store the values

#seraching in an array is a constant time operation
result = new_list[0]
print(result)


#Linear search of the new_list
if 1 in new_list:
    print(True)


for n in new_list:
    if n == 1:
        print(True)

        break


#Inserting into a list / appending is also insert option that adds to end
#Appending is constant time operation but depends on language

#Creating empty list and takes up space n + 1
numbers = [] 
#we get 0 when calling length of numbers, means python doesn't use 
#memory allocation as an indicator of its size

#increases memory allocation when we keep appending to the list, growth pattern is determined by resize operation
#averaging out for resizing operation, append methods take constant time complexity

numbers.append(5)
numbers.append(500)

#inserting is more expensive because it has to shuffle everything over
numbers = []
numbers.extend([4,5,6])
print(numbers)

#Insert shifts elements to the right, delete shifts elements to the left