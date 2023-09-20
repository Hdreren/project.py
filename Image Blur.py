import cv2
import matplotlib.pyplot as plt
import numpy as np

import warnings
warnings.filterwarnings("ignore")

#Blurring
img = cv2.imread("new.york.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.figure(), plt.imshow(img), plt.axis("off"), plt.title("original"), plt.show()

#Average Blurring Method
dst2 = cv2.blur(img, ksize = (3,3))
plt.figure(), plt.imshow(dst2), plt.axis("off"), plt.title("average blur"), plt.show()





