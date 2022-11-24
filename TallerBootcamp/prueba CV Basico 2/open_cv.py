
import cv2
import numpy as np
import argparse
print("Dame un numero.....")
dato = int(input("iNGRESE  0  PARA GIRAR 180, INGRESE 1 PARA GIRAR 90 GRADOS:  "))

image = cv2.imread("lena.jpg")
grices = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

def rotar(image,dato):
    if dato == 0:
        rotar = cv2.rotate(image, cv2.ROTATE_180)
    elif dato == 1:
        rotar = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
    return rotar

cv2.imshow('original Image', image)
cv2.imshow('Rotated Image', rotar(image,dato))
cv2.imshow('imagen en gris', grices)
cv2.waitKey(0)
cv2.destroyAllWindows()

