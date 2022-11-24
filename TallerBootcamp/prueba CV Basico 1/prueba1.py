import cv2

imagen = cv2.imread('blown_ic.png')

(alto,ancho, canales )=imagen.shape
print('Alto={} , Ancho={} , Canales={}' .format(alto, ancho, canales))

remid = cv2.resize(imagen, (200,200))

r=300/ancho
dim=(300, int(alto*r))
redimp = cv2.resize(imagen, dim)

cv2.imshow('Imagen', redimp)
cv2.waitKey(0)
cv2.imwrite('imagencopi.png',imagen)

cv2.destroyAllWindows()