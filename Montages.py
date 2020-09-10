import cv2
import numpy as np
import random
from imutils import build_montages

imagepath=["Pokedex.jpg","tetris.png","Poke.jpg","pill.png"]
random.shuffle(imagepath)
images=[]
for imagepath in imagepath:
    image=cv2.imread(imagepath)
    images.append(image)

montage=build_montages(images,(120,196),(2,3))

for i in montage:
    cv2.imshow("Montage",i)
    cv2.waitKey(0)

