'''
Name : Mohammad Shahed
Day & Date : 18th june 2022 Saturday
File Description : Data Types
Topic : String methods
Notes : The find() method and the index() method is almost same, 
                                 but the only diff is find() method returns -1 if the value is not found.
                                 format_map (Doubt session), isdecimal(doubt session)
'''

'''  Converting the first character to upper case  we use the key word capitalize'''

# x = 'i am a developer'    # I am a developer
# print(x.capitalize())

# y = ('i  want to develop a '); b=  ('game')     # I want to develop a game
# print((y+b).capitalize())

'''      Converting the string into lower case  use the key word casefold '''

# r = 'PYTHON PROGRAMMING'    # python programming
# print(r.casefold())

# v = 'I am Iron man'         # i am iron man
# print(v.casefold())

''' Center method gives the o/p as requeired length with character as space is default'''

# c = "Pineapple"        # 00000Pineapple000000
# print(c.center(20,'o'))


# d = 'Blogger'         # 5Blogger5
# print(d.center(9, '5'))

''' count method is used to return the number of specified characters occured in the string '''

# f = 3,5,3,5,4,8,9,5,1,2,3,6,5,4,2,3,3,3,5          # 5
# print(f.count(5))

# z = 'peusudppjsdjejdpppskdjeksppps'                # 9 
# print(z.count('p'))

''' Encoding is a method returns the encoded version of the string '''

# g = 'I am a Pytho_n developer'      # b'I am a pytho_n developer
# print(g.encode(encoding='ascii', errors= 'backslashreplace'))

# v=b'Python game'       # b'Python game' bytes
# print(v,type(v))

''' endswith method returns true if the string ends with a specified value, otherwise false'''

# m = 'Operator'        # True
# print(m.endswith('r'))

# l = "Hello!, Welcome to my coding world."     # True
# print(l.endswith('world.',8,35))

# k = 'I\'m busy!'                          # False
# print(k.endswith('.'))

'''expandtabs method is used the tabsize of  the strings '''

# h = 'He\tll\to w\tor\tld'      
# print(h.expandtabs())           # He        ll       ow        or        ld
# print(h)                        # He        ll       ow        or        ld
# print(h.expandtabs(2))          # He  ll  ow  or  ld
# print(h.expandtabs(5))          # He     ll     ow     or     ld

''' find method used to search the string and find the specified character or value and returns the position to where it is found '''

# a = 'Hello world'         # 10
# print(a.find('d'))

'''format method formats the specified values and insert them into the  string's placeholder'''
# named indexes
# i = "My name is {name}, I'm {age}".format(name = 'shahed', age= 22)   # My name is shahed, I'm 22
# print(i)
# # numbered indexes 
# i = "My name is {0}, I'm {1}".format( 'shahed', 22)                     # My name is shahed, I'm 22
# print(i)
# # empty placeholders
# i = "My name is {}, I'm {}".format( 'shahed', 22)                           # My name is shahed, I'm 22
# print(i)

'''  index method used to find the first occurence of the specified value '''

# o = "Hello world"                # ValueError
# print(o.index('p'))

# q = "Python programming"       # 9
# print(q.index('o',5,12))

''' The isalnum() method returns True if all the characters are alphanumeric, meaning alphabet letter (a-z) and numbers (0-9) 
                                  Example of characters that are not alphanumeric: (space)!#%&? etc. '''



# n = "Python company"          # False
# print(n.isalnum())

# t = "company123610"          # True
# print(t.isalnum())

# r = "Python3.10.5"            # False
# print(r.isalpha())


''' The isalpha() method returns True if all the characters are alphabet letters (a-z). '''
 
# w = "Helloworld"          # True
# print(w.isalpha())
 
# i = "Helloworld -1235"           # False
# print(i.isalnum())

# e  = "Python3.10.5"          #False
# print(e.isalpha())


''' The isascii() method returns True if all the characters are ascii characters  (a-z). '''

# u = "Company !!@#"         # True
# print(u.isascii())

# o = "Hello3.10.5"         # True
# print(o.isascii())

# y = '..'                  # True
# print(y.isascii())


''' The isdecimal() method returns True if all the characters are decimals (0-9). 
                     This method is used on unicode objects.         '''


# j = ".2.3"                  # False
# print(j.isdecimal())

# c = "1123"                  # True
# print(c.isdecimal())

# f = "Python"                  # False
# print(f.isdecimal())


''' The isdigit() method returns True if all the characters are digits, otherwise False. 
              Exponents, like ², are also considered to be a digit.           '''

# g = "Programmer"      # False
# print(g.isdigit())

# b = "10235642623542"   # True
# print(b.isdigit())

# c = "45.62.2"       # False
# print(c.isdigit())

# d = "1**3"          # False
# print(d.isdigit())


''' The isidentifier() method returns True if the string is a valid identifier, otherwise False. '''

# f = "content325"     # True
# x = "Python3.10.5"    # False
# v = " program"       # False
# h = "_Ironman"        # True
# print(x.isidentifier())
# print(f.isidentifier())
# print(v.isidentifier())
# print(h.isidentifier())

''' The islower() method returns True if all the characters are in lower case, otherwise False. 
                      Numbers, symbols and spaces are not checked, only alphabet characters.        '''


# y = 'HeLLo World'         # False
# d = "python program"      # True
# v = "DevelopER3.10.5"            # False
# print(y.islower())
# print(d.islower())
# print(v.islower())

''' The isnumeric() method returns True if all the characters are numeric (0-9), otherwise False. 
                Exponents, like ² and ¾ are also considered to be numeric values.
                      "-1" and "1.5" are NOT considered numeric values, because all the characters in the string must be numeric, and the - and the . are not.
                         '''

# a = "123456"         # True
# b= "String"          # False
# c = "3.10.15.56"      # False
# d= "-125"             # False
# e = "10kms2"
# print(a.isnumeric())
# print(b.isnumeric())
# print(c.isnumeric())
# print(d.isnumeric())
# print(e.isnumeric())

''' The isprintable() method returns True if all the characters are printable, otherwise False. 
                        Example of none printable character can be carriage return and line feed.       '''


# d = "None%$%&"       # True
# f = "Hello # world?"    # True
# x = "Python3"         # True
# e =  "Hello! \n Are #1?"  # False
# print(d.isprintable())
# print(f.isprintable())
# print(x.isprintable())
# print(e.isprintable())


# r= "Hello !\n are #1?"
# print(r,type(r))


''' The isspace() method returns True if all the characters in a string are whitespaces, otherwise False.  '''

# t = "   "               # True          empty string or multiple spaces in the string will gives us True
# x  = "   ,    "         # False
# s = "   Python!    "     # False          Anything inside the string will gives us False
# z = "."                 # False

# print(t.isspace())             
# print(x.isspace())
# print(s.isspace())
# print(z.isspace())


''' The istitle() method returns True if all words in a text start with a upper case letter, 
                                               AND the rest of the word are lower case letters, otherwise False.'''


# w = "I Am A Programmaer!"         # True
# c = "22 age"                   # False
# e  = "Welcome to my world!"      # False
# q = "Hello! @3?.>"          # True
# a = "I AM A DEVELOPER !"     # False
# print(w.istitle())
# print(c.istitle())
# print(e.istitle())
# print(q.istitle())
# print(a.istitle())


''' The isupper() method returns True if all the characters are in upper case, otherwise False.
                     Numbers, symbols and spaces are not checked, only alphabet characters.        '''



# p = "Welcome!, to my world"      # False
# q = "      DANGEROUS"             # True
# s = "?PYTHON"                # True

# print(p.isupper())
# print(q.isupper())
# print(s.isupper())

''' The join() method takes all items in an iterable and joins them into one string. '''

# g = ("Hello!", "I am ", "Shahed")
# print('  '.join(g))      # Hello!  I  am  Shahed
# print(','.join(g))       # Hello!,I,am,Shahed
# print('.'.join(g))        # Hello!.I.am.Shahed


# f = {"Shahed",  "India"}
# print('I am from'.join(f))


''' The ljust() method will left align the string, using a specified character (space is default) as the fill character.'''

# r = "dragon fruit"
# print(r.ljust(20), "This is my favourite")
# print(r.ljust(20, '0'))
# print(r.ljust(20), '0')

''' The lower() method returns a string where all characters are lower case. 
                            Symbols and Numbers are ignored.       '''

# s = "I am a deVELOper"
# print(s.lower())


''' The lstrip() method removes any leading characters (space is the default leading character to remove)   '''


# d = "             Shahed.          "
# x = d.lstrip()
# print("My name is",x,"I am a programmer.")


f = "...,,,,,,---....,,,,...Banana     "
x = f.lstrip(".,-")
print(x)

































