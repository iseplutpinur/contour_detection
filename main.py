"""
Tugas Akhir pengolahan citra Semester 5
Kelompok:
- Isep Lutpi Nur (2113191079) | IF A2 2019
- M. Taufiq Hidayatuloh (2113191036)  | IF A1 2019
- Adistia Ramadhani (2113191084)  | IF A2 2019
- Dara Atria Ferliandini (2113191098)  | IF A2 2019
"""

# import opencv
import cv2 as cv

# import numpy
import numpy as np

# Pertama Import Gambar menggunakan Sintaks
img = cv.imread('./Jack-Sparrow.jpg')

cv.imshow('Jack-Sparrow', img)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', canny)

ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('Thresh', thresh)

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found!')

cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow('Contours Drawn', blank)

cv.waitKey(0)