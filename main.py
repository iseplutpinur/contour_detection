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

# menampilkan gambar asli
cv.imshow('Jack-Sparrow', img)

# 1. Membuat skala gambar menjadi abu abu
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# 2. Membuat Canny
canny = cv.Canny(img, 125, 175)
cv.imshow('Tepi Objek', canny)

cv.waitKey(0)