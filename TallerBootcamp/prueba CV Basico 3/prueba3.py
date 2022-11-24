import cv2 
import matplotlib.pyplot as plt 
   
img_bgr = cv2.imread('hut.jpg', 1) 
   
color = ('b', 'g', 'r') 
  
for i, col in enumerate(color): 
    histr = cv2.calcHist([img_bgr], [i], None, [256], [0, 256]) 
    plt.plot(histr, color = col) 
    plt.xlim([0, 256]) 
      
plt.show()