''' The maketrans() method returns a mapping table that can be used with the translate() method to replace specified characters. '''

# g = "Hello! bobby"                 # Hello! dobby
# v = g.maketrans('b','d')
# print(g.translate(v))

#   ''' Use a mapping table to replace many characters:  ''' 

# o = "Hello! rahul"            # Heaao! gaura 
# a = "lahru"
# b = "aaugr"                      
# x = o.maketrans(a,b)
# print(o.translate(x))

#  '''The third parameter in the mapping table describes characters that you want to remove from the string: '''

# o = "Hello! rahul"          # Ho! gaur  
# a = "lahru"
# b = "aaugr"    
# z= "lle"                  
# x = o.maketrans(a,b,z)
# print(o.translate(x))

# '''The maketrans() method itself returns a dictionary describing each replacement, in unicode: '''

# f = "Hello! sam"              # 109: 111, 115: 106, 97: 101, 72: None, 108: None, 111: None
# p = 'msa'
# q = 'oje'
# z = 'Hlo'
# print(f.maketrans(p,q,z))

# print(chr(109))        # m
# print(ord('H'))        # 72


''' The partition() method searches for a specified string, and splits the string into a tuple containing three elements. 
               The first element contains the part before the specified string.  
                                 The second element contains the specified string.
                                                   The third element contains the part after the string.'''

# k = "I want to eat panipoori today"      # "I want to eat", "panipoori", "today"
# m = k.partition("panipoori")
# print(m)

# j = "I want to eat panipoori today"            # "I want to eat panipoori today", "",""
# l = j.partition("biryani")
# print(l)


''' The replace() method replaces a specified phrase with another specified phrase.  '''

# i = "I like bananas and apples"              # I like bananas and  Biryani
# f = i.replace("apples","Biryani")
# print(f)

# c = "There was once was a table on was apple was on it"              # There once once once  a table on once apple was apple on it 
# g = c.replace("was", "once",3)
# print(g)

'''The rfind() method finds the last occurrence of the specified value. 
                    The rfind() method returns -1 if the value is not found.
                                    The rfind() method is almost the same as the rindex() method. See example below.   '''


# n = "hii sma , hello sah, hey bob"          # -1
# v = n.rfind("d")
# print(v)


# p = "hii sma , hello sah, hey bob"          # 26
# q = p.rfind("o",6,16)
# print(q)

# txt = "Hello, welcome to my world."        # diff b/t index and find methods

# w = "hii sma , hello sah, hey bob"          
# print(w.rfind("n"))                   # -1
# print(w.rindex("n"))                 # ValueError

''' The rindex() method finds the last occurrence of the specified value.  
                          The rindex() method raises an exception if the value is not found.    '''

# v = "Hello! welcome to my world"
# print(v.rindex('e'))              # 13
# print(v.index('w'))               #7        
# print(v.find('w'))                  #7
# print(v.rfind('e'))                 # 13


'''The rjust() method will right align the string, using a specified character (space is default) as the fill character.  '''

# n = "Pineapple"
# x = n.rjust(20,"5")                      # 55555555555pineapple This is my favourite fruit
# print(x + " "+"This is my favourite fruit")


''' The rpartition() method searches for the last occurrence of a specified string, and splits the string into a tuple containing three elements.'''

# b = "I could eat bananas all day, bananas are my favorite fruit"
# a = b.rpartition("bananas")              # "I could eat bananas all day,",  "bananas","are my favorite fruit"
# print(a)
# print(b.partition("bananas"))              # "I could eat" ," bananas"  ,"all day,bananas,are my favorite fruit"
# print(b.rpartition("apples"))                # '','',"I could eat bananas all day, bananas are my favorite fruit"
# print(b.partition("apples"))                 # "I could eat bananas all day, bananas are my favorite fruit",'',''


''' The rsplit() method splits a string into a list, starting from the right. '''

# s = "apples,bananas, pineapple, orange, guava"
# x = s.rsplit(",")       # 'apples','bananas','pineapple','orange','guava'
# print(s.rsplit())         # 'apples,bananas','pineapple,','orange,','guava'    # (Doubt session)  
# print(s.rsplit(",",1))        #  applying the maxsplit to 1 will return a list with 2 elements!
# print(s.rsplit(",",4))         # ['apples','bananas','pineapple','orange','guava']
# print(x)                       

''' The rstrip() method removes any trailing characters (characters at the end a string), space is the default trailing character to remove.'''

# d = "        Mango            "
# c = d.rstrip()
# print(c+ " This is a seasonal  fruit")      #             Mango This is a seasonal fruit

# e = "Apple .....,,,,dhdif,,.///s"
# w = e.rstrip(".,hdif/s")
# print(w + "Eat an apple every day")      # Apple Eat an apple every day


''' The split() method splits a string into a list. '''

# b = "Hello! welcome to my world"
# d = b.split()
# print(d)                         # 'Hello!', 'welcome', 'to', 'my', 'world'
# s = "Hello, I am bob,  I am a engineer"
# print(s.split(","))                      # 'Hello', ' I am bob', '  I am a engineer'
# a = "Welcome!# to# my # world"
# print(a.split("#",2))               # 'Welcome!', ' to', ' my ', ' world'


''' The splitlines() method splits a string into a list. The splitting is done at line breaks.'''

# k = "Thank you for the music\nwelcome to the jungle"
# d = k.splitlines()           # 'Thank you for the music', 'Welcome to the jungle'
# print(d)
# print(k.splitlines(True))        # 'Thank you for the music', 'Welcome to the jungle'


''' The startswith() method returns True if the string starts with the specified value, otherwise False. '''

# q = "Hello! Welcome to my world"
# s = q.startswith("Hello")  
# print( q.startswith("hello"))  # False
# print(q.startswith("python"))  # false
# print(s)                         # # True
# print(q.startswith("Wel",7,25))  # True


''' The strip() method removes any leading (spaces at the beginning) and trailing (spaces at the end) characters 
                                           (space is the default leading character to remove)'''

# e = "          Dragon fruit        " 
# d = e.strip()
# print(" among all the fruits "+d+' I don\'t like it')   # among all the fruit Dragon fruit I don't like it

# f = "....,,,,,, Apple //..,,dhdjjd...,,.."
# r = f.strip(".,/dhj")
# print(r)               # Apple

''' The swapcase() method returns a string where all the upper case letters are lower case and vice versa.'''

# x = "PyThon ProGRAmmer"
# c = x.swapcase()
# print(c)      # pYthON pROgraMMER

''' The title() method returns a string where the first character in every word is upper case. Like a header, or a title.'''

# q = "Welcome! to my world"
# m = q.title()
# print(m)        # Welcome! TO My World

# e = "Python3 d89dhf9s0sjd 222"
# print(e.title())    # Python3 D89Dhf9S0Sjd 222


''' The translate() method returns a string where some specified characters are replaced 
                                           with the character described in a dictionary, or in a mapping table.
                            If you use a dictionary, you must use ascii codes instead of characters.'''

# a  = {101:  80}
# b = "Hello Sam!"
# print(b.translate(a))       # HPllo Sam!


# txt = "Good night Sam!"
# mydict = {109: 101, 83: 74, 97: 111, 111: None, 100: None, 110: None, 103: None, 104: None, 116: None}
# print(txt.translate(mydict))          # G i Joe!

# print(chr(109))

''' The upper() method returns a string where all characters are in upper case. 
                         Symbols and Numbers are ignored.'''


# l = "Hello! my friends Welcome to my prohramming world"  
# print(l.upper())            # HELLO! MY FRIENDS WELCOME TO MY PROHRAMMING WORLD


''' The zfill() method adds zeros (0) at the beginning of the string, until it reaches the specified length.
                              If the value of the len parameter is less than the length of the string, no filling is done.'''


txt = '50'
print(txt.zfill(15))             # 000000000000050


a = "hello world"                # 0000hello world
b = "welcome to the jungle"          # welcome to the jungle 
c = "10.000"                   # 000010.0000

print(a.zfill(15))
print(b.zfill(10))
print(c.zfill(10))
