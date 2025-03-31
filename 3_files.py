import os
import time
import pandas
#file.seek() sirve para pasar a una posicion alternativa desde donde se leera o escribira

'''
myfile = open('fruits.txt')
print(myfile.read())
myfile.close()
'''

'''
Read the bear.txt file, and print out the first 90 characters of its content.

with open('bear.txt') as myfile:
    content = myfile.read()
print(content[:90])
'''
'''
def fun(character, filepath):
    with open(filepath) as myfile:
        content = myfile.read()
        return content.count(character)
'''

'''with open('samples/fruits.txt') as myfile:
    content = myfile.read()

with open('samples/contenido.txt', 'w') as my_file:
    my_file.write('cosas\nde')

print(content)'''

'''
In this section, you learned that:

Builtin objects are all objects that are written inside the Python interpreter in C language.

Builtin modules contain builtins objects.

Some builtin objects are not immediately available in the global namespace. They are parts of a builtin module. To use those objects the module needs to be imported first. E.g.:

import time
time.sleep(5)
A list of all builtin modules can be printed out with:

import sys
sys.builtin_module_names
Standard libraries is a jargon that includes both builtin modules written in C and also modules written in Python.

Standard libraries written in Python reside in the Python installation directory as .py files. You can find their directory path with sys.prefix.

Packages are a collection of .py modules.

Third-party libraries are packages or modules written by third-party persons (not the Python core development team).

Third-party libraries can be installed from the terminal/command line:

Windows:

pip install pandas or use python -m pip install pandas if that doesn't work.

Mac and Linux:

pip3 install pandas or use python3 -m pip install pandas if that doesn't work.
'''

while True:
    if os.path.exists('samples/datos.csv'):
        myfile = pandas.read_csv('samples/datos.csv')
        print(myfile)
    else:
        print('File does not exits')
    time.sleep(10)