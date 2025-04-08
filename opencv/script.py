import cv2

kame_house_image = cv2.imread("kame_house.jpg", 1)
print(kame_house_image.shape)
resize_kame = cv2.resize(kame_house_image, 
    (int(kame_house_image.shape[1]/2), int(kame_house_image.shape[0]/2))) #el 0 es alto de la imagen, el 1 el ancho
print(resize_kame.shape)

#cv2.imshow("KameHouse", resize_kame)
#cv2.waitKey(0)
cv2.imwrite("kamehouse_r.jpg", resize_kame) #especificar extension
