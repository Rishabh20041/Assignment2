#Identity Operators:

#is

a1 = [1, 2, 3]
b1 = a1
c1 = [1, 2, 3]
print(a1 is b1)  
print(a1 is c1)  

#isNot

a1 = [1, 2, 3]
b1 = a1
c1 = [1, 2, 3]
print(a1 is not b1)  
print(a1 is not c1)  

#Membership Operators:

#in

fruits = ['apple', 'banana', 'orange']
print('banana' in fruits)    
print('grape' in fruits)     

#not in

fruit = ['apple', 'banana', 'orange']

print('banana' not in fruit) 
print('grape' not in fruit)  