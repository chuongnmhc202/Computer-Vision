import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('photo.png')
#img = cv2.resize(img, (300, 200))
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plt.imshow(img)
plt.show()
# height, width, channels = img.shape
#
# # In kích thước ảnh
# print(f"Chiều rộng (width): {width} pixels")
# print(f"Chiều cao (height): {height} pixels")
# print(f"Số kênh màu (channels): {channels}")
# cv2.imwrite('picture.png', img)

def conv2d(input, kernelSize):
    height, width = input.shape
    kernel = np.random.randn(kernelSize, kernelSize)
    results = np.zeros((height - kernelSize + 1, width - kernelSize + 1))
    for row in range(0, height - kernelSize + 1):
        for col in range(0, width - kernelSize + 1):
            results[row, col] = np.sum(input[row:row + kernelSize, col:col + kernelSize] * kernel)
    return results


img_gray_conv2d = conv2d(img_gray, 3)
plt.imshow(img_gray_conv2d, cmap= 'gray')
plt.show()
