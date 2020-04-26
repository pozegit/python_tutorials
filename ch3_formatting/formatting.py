import datetime

message = """Hello"""
name = 'Alex'
pList= ['Jen',23]
pTuple=('Livia',23)
#s={1,2,3}

tag = 'h1'
text = 'This is a headline'
person={'name':'Ann','age':22}

#the following example are working the same way with lists and tuples; we prefered a dictionary though

#first variant old way
print( 'My name is '+ person['name'] +' and i am '+str(person['age']) + ' years old.')

#with format, {} placeholder and default order
print(f'My name is {person["name"]} and i am {person["age"]} years old' )  #new
#print('My name is {} and i am {} years old'.format(person['name'],person['age']) )  #old but still okeish




#with format,{} placeholder and different order

print(  f'<{tag}>{text}</{tag}>')
#print('My name is {1} and i am {0} years old'.format(person['name'],person['age']) )  #old
#print(  '<{0}>{1}</{0}>'.format(tag,text)  )                                          #old

#with format,{} placeholder and different order -  simplified
print(f"My name is {pList[0]} and i am {pTuple[1]} years old" )
print(f"My name is {person['name']} and i am {person['age']} years old")
print('My name is {0[0]} and i am {1[1]} years old'.format(pList,pTuple))   #old
print('My name is {0[name]} and i am {0[age]} years old'.format(person))    #old

#with live keywords
print( 'My name is {name} and i am {age} years old.'.format(name = 'Oliver',age = 24) )  #old

#with tuple sufix and % placeholder
print('Ny name is %s and i am %i years old' %(person['name'],person['age']))  #sufix must be  tuple! #old

######### with dictionaries prefered way
print( f"My name is {person['name']} and i am { person['age'] } years old -"  )
#print( 'My name is {name} and i am {age} years old'.format(**person) ) # ** is unpacking a dictionary  #old


######### with Classes objects

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

person = Person('Alex',44)

print( f'my name is {person.name} and i am {person.age} years old ' )
#print( 'my name is {0.name} and i am {0.age} years old '.format(person) )  #old
#print ( ' my name is %s and i am %s years old' %(person.name,person.age) )  #old


#formatting with numbers

#default
for i in range(1,11):
    print(f'The value is {i} ')
    #print( 'The value is {} '.format(i) ) #old

#add a zero padding to the left, max 2 numbers
for i in range(1,11):
    print(f"The value is {i:02} ")
    #print( 'The value is {:02} '.format(i) )  #old

#pi decimal places
pi= 3.14159265
print( f'Pi is equal to {pi:.3f} ')
#print( 'Pi is equal to {:.3f} '.format(pi) )  #old


#comma separated high numbers
sentence = f' 1Mb is equal to {1000**2:,} bytes'
#sentence = ' 1Mb is equal to {:,} bytes'.format(1000**2) #old
print(sentence)


#datetimes

my_date = datetime.datetime(2016,9,24,12,30,45)
print(my_date)



#March 01,2016
sentence = f'{my_date:%B %d,%Y}'
#sentence = '{:%B %d,%Y}'.format(my_date) #old
print(sentence)


#March 01, 2016 fell on Tuesday and was the 061 day of the year
sentence = f'{my_date:%B %d,%Y} fell on {my_date:%A} and was the {my_date:%j} of the year '
#sentence = '{0:%B %d,%Y} fell on {0:%A} and was the {0:%j} of the year '.format(my_date)  #old
print(sentence)


#f-string functions calling
def mymax(x, y):
    return x if x > y else y
a = 3
b = 4
print(f'Max of {a} and {b} is {mymax(a, b)}')


#f-string objects class
class User:
    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation

    def __str__(self):
        return f"{self.name} is a {self.occupation} , default __str__"
    def __repr__(self):
        return f"{self.name} is a {self.occupation}"

u = User('John Doe', 'gardener')

#default __str__
print(f'{u}')
#__repr__
print(f'{u}!r')

#f-string width width -with columns
for x in range(1, 11):
    print(f'{x:02} {x*x:3} {x*x*x:4}')

#f-string notations
a = 300

# hexadecimal
print(f"{a:x}")

# octal
print(f"{a:o}")

# scientific
print(f"{a:e}")

#f-string multiline
name = 'John Doe'
age = 32
occupation = 'gardener'

msg =  f'Name: {name}\n' \
    f'Age: {age}\n'      \
    f'Occupation: {occupation}'


print(type(msg))

import timeit
timeit.timeit("""name = "Eric"
age = 74
'%s is %s.' % (name, age)""", number = 10000)

print(help(str.join))


