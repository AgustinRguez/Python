#dataframe utilizado para dict
#import pandas
import numpy 
import cv2

'''data = pandas.DataFrame([{'nombres':'name','apellido':'surname','edad':12 }]) 
print(data)
dataframe basicamente es el dibujo que te hace pandas con el dict que le pases'''

'''n = numpy.arange(27)
m = n.reshape(3,3,3)
print(m)'''

image_g = cv2.imread("smallgray.png",0) #con 1 te hace una matriz tridimensional donde te muestra los valores en BGR
#print(image_g)


image_create = cv2.imwrite("newimage.png", image_g)
#print(image_g)

#for i in image_g.T:
    #print(i)

lst = numpy.hstack((image_g,image_g)) #hay que pasarlo como tupla sino dara un error al concatenarlo
print(lst)
lst_split = numpy.hsplit(lst,2)
print(lst_split) #vstack hace lo mismo pero vertical


