studentGrades = [9.1, 8.8, 7.5]

testList1 = list(range(1, 10)) #gives [1,2,3,4,5,6,7,8,9]
testList2 = list(range(1, 10, 2)) #gives [1, 3, 5, 7, 9]

#dir(____) will provide you with a list of all methods that the 
#type can use

#dir(__builtins__) gives a complete list of all built in functions
#and types

mySum = sum(studentGrades)
mean = mySum/(len(studentGrades)) #len gives you the length

print(mean)