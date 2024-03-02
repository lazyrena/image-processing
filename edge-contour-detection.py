import cv2 # library for image processing
import matplotlib.pyplot as plt 

# open image by path
img = cv2.imread('20234.png')

# Using Canny function in cv2
edges = cv2.Canny(img, 100, 200, 3, L2gradient=True)
plt.figure()
plt.title('New Year')
plt.imsave('20234.png', edges, cmap='gray', format='png')
plt.imshow(edges, cmap='gray')
plt.show()
