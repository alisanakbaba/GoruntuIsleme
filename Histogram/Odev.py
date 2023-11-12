import cv2
import matplotlib.pyplot as plt

# Resimi degiskene at
fotograf = cv2.imread("indir.jpeg",)
cv2.imshow("Manzara",fotograf)

# Görüntüyü formül ile gri tonlamaya cevir
Blue = fotograf[:,:,0]
Green = fotograf[:,:,1]
Red = fotograf[:,:,2]

gray = 0.2989 * Red + 0.5870 * Green+ 0.1140 * Blue

# Histogramı fonk kullanmadan bul
histogram = [0] * 256
for i in range(len(gray)):
    for j in range(len(gray[0])):
        pixel = int(gray[i][j])
        histogram[pixel] += 1

# Histogramı matplotlib ile çiz
plt.plot(histogram)
plt.title('Resimin Histogramı')
plt.xlabel('Piksel Değeri')
plt.ylabel('Görülme sıklığı')
plt.show()
