''' 
Name : Mohammad Shahed
Day and date : 17th June 2022 Friday
File Description : Data Types
Topic : String conversion
Notes :                   We can convert the int into str and float.
                    And we can also convert the float into str and int.
      But we cannot convert the str into int and float.

Convertng the string types into various data types
 '''

# z = 'Python programming'
# print(z,type(z))

# Converting the int into str and float
# x = 2569
# print(x,type(x))
# print(str(x))
# print(float(x))

# Converting the float into int and str

# t = 5.23

# print(int(t))     # 5
# print(str(t))     # 5.23


# Converting the str into int and float

# v = 'Operator'

# print(int(v))             # Value error
# print(int(v))             # Value error



''' But we can convert the str into int and float when the str contains number in it.'''

# c = '2659'

# print(int(c))
# print(float(c))

''' To convert the str into float we can do it but
                          when we want to convert the str into int is not possible 
                                                       then comes the varaibles into the picture '''

# d = '25.65'

# print(float(d))             # 25.65
# # print(int(d))               # ValueError

# z = float(d)
# print(int(z))                # 25


           # Concatenating  str   to str

f = 'I want to be a python '
x = 'developer 3.10.5'

print(f+x)

e = "I will be  developer in "
t = 1 
v = 'month'

print(e,t,v)
print(e+str(t)+v)


print("I will be the world's richest person soon"+"."+" "+"This is my intution")

s = 'By the end of this months I need to be placed in a multi national company'
a = 'This is '
z = 100


print(s+a+str(z)+'% sure!')
print(s,a,str(z),'% sure!')



r = '25.6'

# print(float(r))
# print(int(r))

t = float(r)
# print(t)
print(int(t))


