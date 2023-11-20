import cv2
import numpy as np


def renk_filtresi(goruntu, alt_sinir, ust_sinir):
    # Belirtilen renk aralığındakileri  beyaz  olarak, diğerlerini siyah ayarla
    maske = cv2.inRange(goruntu, alt_sinir, ust_sinir)

    # Görüntüdeki sadece belirtilen renkteki nesneleri göster
    sonuc = cv2.bitwise_and(goruntu, goruntu, mask=maske)

    return sonuc


def main():
    # Kameraya bağlan
    cap = cv2.VideoCapture(0)

    while True:
        # Kameradan bir kare al
        ret, kare = cap.read()

        # RGB den HSV ye dönüştürme
        hsv_kare = cv2.cvtColor(kare, cv2.COLOR_BGR2HSV)

        # Kırmızı renk için filtre
        alt_kirmizi = np.array([0, 100, 100])
        ust_kirmizi = np.array([10, 255, 255])
        kirmizi_sonuc = renk_filtresi(hsv_kare, alt_kirmizi, ust_kirmizi)


        yesil_mavi_maske = np.zeros_like(kare)

        # Yeşil ve mavi nesneleri siyah yap
        yesil_mavi_maske = cv2.bitwise_or(renk_filtresi(hsv_kare, np.array([40, 40, 40]), np.array([80, 255, 255])),
                                          renk_filtresi(hsv_kare, np.array([100, 100, 100]), np.array([140, 255, 255])))

        # Siyah maskeyi orijinal görüntüden çıkararak sadece kırmızı nesneyi göster
        sonuc = cv2.subtract(kirmizi_sonuc, yesil_mavi_maske)


        cv2.imshow('Filtrelenmiş Görüntü', sonuc)

        # Çıkış için 'x' tuşuna basın
        if cv2.waitKey(1) & 0xFF == ord('x'):
            break

    # Kamerayı kapa
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
