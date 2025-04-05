#student_grades = list(range(0,11))
#student_grades_la = [10.2, 2, 'la', []]
#__builtins__ en la terminal te devuelve todos los metodos integrados
#tuplas = (contenido) / listas = [contenido] / diccionario {'': value}
#dir(str)

'''grades_list = [10, 2, 5, 6, 9]
dict_of_grades = {'Marry': 9.1,'Jim': 8}

mysum = sum(dict_of_grades.values())
lenght = len(dict_of_grades)
notes = mysum/lenght

print(notes)
'''

'''
    list using slicing
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    print(letters[1:4])

    title: same than the others but with positive numbers.
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    print(letters[0:3])
    
    title: Print out the slice ['e', 'f', 'g'] of the letters list using slicing.
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    print(letters[-3:])

'''

'''
    Tip: Converting Between Datatypes
    Sometimes you might need to convert between different data types in Python for one reason or another. That is very easy to do:

From tuple to list:

>>> cool_tuple = (1, 2, 3)
>>> cool_list = list(cool_tuple)
>>> cool_list
[1, 2, 3]


From list to tuple:

>>> cool_list = [1, 2, 3]
>>> cool_tuple = tuple(cool_list)
>>> cool_tuple
(1, 2, 3)


From string to list:

>>> cool_string = "Hello"
>>> cool_list = list(cool_string)
>>> cool_list
['H', 'e', 'l', 'l', 'o']


From list to string:

>>> cool_list = ['H', 'e', 'l', 'l', 'o']
>>> cool_string = str.join("", cool_list)
>>> cool_string
'Hello'
As can be seen above, converting a list into a string is more complex. Here str() is not sufficient. We need str.join(). 
Try running the code above again, but this time using str.join("---", cool_list) in the second line. 
result: 'H---e---l---l---o'
You will understand how str.join() works.
'''

data = {'a': [1,2,3], 'b':[4,5,6], 'c':[7,8,9]}
print(data['b'][2])