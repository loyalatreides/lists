fruits = ['banana','orange','mango','lemon']
vegetables = ['Tomato','Potato','Cabbage','Onion','Carrot']
print('Fruits: ',fruits)
print('Number of Fruits: ', len(fruits))
print('Vegetables: ',vegetables)
print('Number of Vegetables: ', len(vegetables))
#first_fruit = fruits[0]
#print(first_fruit)
#second_fruit = fruits[1]
#print(second_fruit)
first_fruit, second_fruit, third_fruit, *rest = fruits
print(first_fruit)
print(second_fruit)
print(third_fruit)
print(rest)

first, second, third, *rest, tenth = [1,2,3,4,5,6,7,8,9,10]
print(first)
print(second)
print(third)
print(rest) 

fruits = ['banana','orange','mango','lemon']
fruits[0] = 'apple'
print(fruits)

#Exercises
#Level-1
#1
list = []
#2
list = ['Messi','Iniesta','Xavi', 'Pedri','Gavi']#2
print(len(list))#3
print(list[0:6:2])#4
mixed_data_types = ['Kamran',25,5.8,'Single','New Delhi'] #5
it_companies = ['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon'] #6
print(mixed_data_types) #7
print(it_companies) #7
print('Number of companies in the list: ',len(it_companies)) #8
print(it_companies[0:7:3]) #9
it_companies[0] = 'Zoho' #10
print(it_companies) 
last_index = len(it_companies) - 1 #10
print(last_index)
it_companies.append('Facebook') #11
print(it_companies)
it_companies.insert(0, 'Amazon') #12
print(it_companies)
#13 Not attended
it_companies.append('#') #14
print(it_companies) 
print(it_companies.index('Microsoft')) #15
it_companies.sort()
print(it_companies) #16
print(it_companies) #17
print(it_companies[0:3]) #18
print(it_companies[-3:]) #19
print(it_companies[3:4]) #20
it_companies.remove('Facebook') #21
print(it_companies)
it_companies.pop(0) #21
print(it_companies)
it_companies.pop(3) #22
print(it_companies)
it_companies.remove('Apple') #22
print(it_companies)
it_companies.remove('Amazon')
print(it_companies) #23
it_companies.pop(-1)
print(it_companies) #23
del it_companies[0:7] #24
it_companies.clear() #25
print(it_companies)
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
front_end.extend(back_end) #26
print(front_end)
full_stack = front_end.copy()
print(full_stack) #27
full_stack.insert(5, 'Python')
print(full_stack) #27
full_stack.insert(6, 'SQL')
print(full_stack) #27
