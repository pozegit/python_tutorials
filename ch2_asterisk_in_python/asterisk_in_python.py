a=2;b=3
l = ['a',2,3]
t = ('a',2,3)
str = 'abc1'
sets = {'a',2,3}
d= {'Hana':23,'Oliver':44}

#number -> multiply or exponention
print(a*b) #6
print(a**b)

#seq -> repetition the seq n times
print(l*3) #('a', 2, 3, 'a', 2, 3, 'a', 2, 3)
print(t*3) #('a', 2, 3, 'a', 2, 3, 'a', 2, 3)
print(str*3) #abc1abc1abc1
#print(sets*3) #not supported operand error
#print(d*3) #not supported operand error

#function -> in arguments passed : allows variable number of arguments
def show(name):
    return name
print(show('alex')) #alex
#print(show('alex','jane')) #TypeError: show() takes 1 positional argument but 2 were given
def show(*name):
    return name #as tuple
print(show('alex')) #('alex',) ->  tuple
print(show('alex','jane')) #('alex', 'jane') ->tuple






