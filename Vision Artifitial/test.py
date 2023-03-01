# import cv2
# import numpy as np
# from matplotlib import pyplot as plt

# img  = cv2.imread("Vision Artifitial/img/img1.jpg" )

# img = cv2.resize(img ,(500,500))

# print(img.shape)

# if img.shape[2] == 3:
#     img = cv2.cvtColor(img ,cv2.COLOR_RGB2GRAY)


# hist = cv2.calcHist([img], [0], None, [256], [0, 256])

# # plt.plot(hist)
# # plt.xlim([0, 256])
# # plt.show()

# # array = np.zeros([img.shape[0] ,img.shape[1]])
# # array = 255
# s = 255 - img

# hist = cv2.calcHist([s], [0], None, [256], [0, 256])
# plt.plot(hist)
# plt.xlim([0, 256])
# plt.show()

# # cv2.imshow('image', img)
# # cv2.waitKey(0)
# # cv2.destroyAllWindows()


import matplotlib.pyplot as plt
# import numpy as np
# from PIL import Image

# # Charger l'image
# img = Image.open("Vision Artifitial/img/img1.jpg")

# # Convertir l'image en tableau numpy
# img = np.array(img)

# # Inverser l'image
# img_neg = 255 - img

# # Afficher l'image originale, l'histogramme de l'image originale, l'image inversée et l'histogramme de l'image inversée
# fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(8,8))
# axes[0,0].imshow(img, cmap='gray')
# axes[0,0].set_title('Image originale')
# axes[0,1].hist(img.flatten(), bins=range(256))
# axes[0,1].set_title("Histogramme de l'image originale")
# axes[1,0].imshow(img_neg, cmap='gray')
# axes[1,0].set_title('Image inversée')
# axes[1,1].hist(img_neg.flatten(), bins=range(256))
# axes[1,1].set_title("Histogramme de l'image inversée")
# plt.show()


# import cv2
# import numpy as np

# # Load the image in grayscale
# img = cv2.imread('Vision Artifitial/img/img1.jpg', 0)

# # Calculate the mean and standard deviation
# # mean, std_dev = cv2.meanStdDev(img)

# # # Print the standard deviation
# # print("Standard deviation:", std_dev[0][0])

# img = np.array(img)


# minimal = min(min(img))
# maximum = max(max(img))

# S = 255*(img-minimal) / (maximum - minimal)

# cv2.imshow('test',S)

import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load the image in grayscale
img = cv2.imread('Vision Artifitial/img/img1.jpg', 0)

# Compute the minimum and maximum intensity values
min_val = np.min(img)
max_val = np.max(img)

# Define the output range
out_min = 0
out_max = 255

# Compute the scaling factor
scale = (out_max - out_min) / (max_val - min_val)

# Apply the scaling factor and offset to each pixel
stretched_img = (img - min_val) * scale + out_min

# Clip the pixel values to the output range
stretched_img = np.clip(stretched_img, out_min, out_max).astype(np.uint8)

# Display the original and stretched images
plt.subplot(1, 2, 1)
plt.imshow(img, cmap='gray')
plt.title('Original')
plt.axis('off')
plt.subplot(1, 2, 2)
plt.imshow(stretched_img, cmap='gray')
plt.title('Stretched')
plt.axis('off')
plt.show()



