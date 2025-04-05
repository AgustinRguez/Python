#isistance es mas avanzado
#message = f'hello {user_input}' fstrings
#user.capitalize or user.title devuelve la primer letra en mayuscula

'''
def mean(value):
    if isinstance(value, dict):
    #if type(value) == dict:
        result = sum(value.values()) / len(value)
    else:
        result = sum(value) / len(value)
    return result

dict_of_grades = {'Marry': 9.1,'Jim': 8}
print(mean([5,6,5]))
print(mean(dict_of_grades))
'''

'''
Loop over the phone_numbers values and in each loop print out the phone number, but with '00' instead of '+'.
 In other words, your code should output:

0037682929928

00423998200919

Hint: You can access dictionary values with phone_numbers.values() and you can replace characters using str.replace() .

phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
for value in phone_numbers.values():
    print(f'{value}'.replace('+', '00'))
'''

'''
def temperature(value):
    if value > 7:
        return 'Hot'
    else:
        return 'Cold'

user_input = float(input('Ingrese una temperatura: '))
print(temperature(user_input))
'''

def text_maker(phrase):
    question_mark = ('que', 'como', 'podes', 'todo')
    capitalized = phrase.capitalize()
    if(phrase.startswith(question_mark)):
        return '{}?'.format(capitalized)
    else:
        return '{}.'.format(capitalized)

results = []
while True:
    user_input = input('Escribi algo: ')
    if user_input == 'end':
        break
    else:
        results.append(text_maker(user_input))

print(' '.join(results))