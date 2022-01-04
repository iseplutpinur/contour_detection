### Contour Detection

#### Projek Tugas Akhir Mata Kuliah Penolahan Citra

##### Kelompok:

- Isep Lutpi Nur (2113191079) | IF A2 2019
- M. Taufiq Hidayatuloh (2113191036)  | IF A1 2019
- Adistia Ramadhani (2113191084)  | IF A2 2019
- Dara Atria Ferliandini (2113191098)  | IF A2 2019



#### Projek Tugas Akhir
##### Lingkungan Pengembangan
Dalam project ini menggunakan bahasa pemrograman **Python v3.8** Dan menggunakan Tools/Library OpenCv <a href="https://opencv.org/">https://opencv.org/ </a> dan Library NumPy <a href="https://numpy.org/">https://numpy.org/ </a>



##### Pembahasan Projek Contur Detection

##### Pengertian Contur

Dalam Projek ini akan membahas contur pada OpenCV, Contour pada dasarnya adalah batas-batas object, garis atau kurva yang menghubungkan titik menerus sepanjang suatu object.

Dalam pandangan matematis contour tidak sama dengan tepi karena dalam sudut pandang matematis contour dan tepi merupakan dua hal yang berbeda. Contour Berfungsi untuk menganalisis bentuk dan mendeteksi objek.



##### Projek

**Assets:**

Kita mempunyai satu aset gambar dibawah:

![Jack-Sparrow](./Jack-Sparrow.jpg)

**Koding:**

###### 1. Skala Abu-Abu

- Pertama Kita akan mengimport OpenCv dengan cara 

```python
import cv2 as cv
```

- Kemudian kita akan menambahkan file gambar menggunakan fungsi ```cv.imread()``` yang akan ditampung kedalam variable img

```python
img = cv.imread('./Jack-Sparrow.jpg')
```

- Tampilkan terlebih dahulu gambar aslinya sebelum diubah.
```python
cv.imshow('Jack-Sparrow', img)
```

- Kali ini kita akan mencoba mengubah skala gambar menjadi abu abu dengan cara :

```python
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)
```

Sehingga Keseluruhan sintaks nya menjadi pada akhir baris ditambahkan statement untuk menahan agar windows tidak tertutup secara otomatis dengan menambahkan sintaks ```cv.waitKey(0)```:
```python
import cv2 as cv

img = cv.imread('./Jack-Sparrow.jpg')

cv.imshow('Jack-Sparrow', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

cv.waitKey(0)
```

**Hasilnya:**

<img src=".\screenshot\image-20220105043054029.png">

Dan

![image-20220105043215823](.\screenshot\image-20220105043215823.png)






###### 2. Meliha Tepi Pada Objek

Untuk bisa melihat tepi pada objek disini menggunakan fungsi ```Canny``` dengan dua argumen ambang batas yaitu 125 dan 175 dan namanya tepi objek sehingga sintaksnya seperti dibawah:
```python
import cv2 as cv

img = cv.imread('./Jack-Sparrow.jpg')

canny = cv.Canny(img, 125, 175)
cv.imshow('Tepi Objek', canny)

cv.waitKey(0)
```

**Hasilnya:**

![image-20220105044600651](.\screenshot\image-20220105044600651.png)

