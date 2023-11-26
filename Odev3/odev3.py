import cv2
import numpy as np

image = cv2.imread("pirinc.jpeg")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Gauss filtresi uygula
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# Kenarları tespit et
edges = cv2.Canny(blur, 50, 150)

# Gürültüyü azalt
kernel = np.ones((5, 5), np.uint8)
dilated_edges = cv2.dilate(edges, kernel, iterations=1)

# Konturları bul
contours, _ = cv2.findContours(dilated_edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# yüklenen görüntüyü siyah arka plana yükle
result = np.zeros_like(image)

# tespit edilen pirinçleri beyaz olarak, siyah arka plana ekle
cv2.drawContours(result, contours, -1, (255, 255, 255), thickness=cv2.FILLED)

# pirinçleri hesapla
rice_count = len(contours)

print(f"Pirinç sayisi: {rice_count}")

cv2.imshow('Rice Only', result)
cv2.waitKey(0)
cv2.destroyAllWindows()