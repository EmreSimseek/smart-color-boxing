import cv2
from util import get_limits, select_color_with_key
import  numpy as np
cap = cv2.VideoCapture(0)

# Renk seçimi bilgisi
print("Select the color you want to detect from the list (just enter the number)"
      "\n1-Red\n2-Green\n3-Blue\n4-Yellow\n5-Cyan\n6-Magenta\n7-Orange\n8-Purple\n")
print("Press '1' to '8' to select a color directly.")
print("Press 'q' to quit the program.\n")


color = None  # Başlangıçta hiçbir renk seçilmedi
color_name = ""
min_contour_area = 2000  # Minimum kontur alanı

# 3x3 bir kernel matrisi tanımlayalım
kernel = np.ones((3, 3), np.uint8)

while True:
    ret, frame = cap.read()  # Her döngüde görüntüyü al
    if not ret:
        print("Failed to capture frame.")
        break

    key = cv2.waitKey(1) & 0xFF  # Tuş kontrolü
    if ord('1') <= key <= ord('8'):
        color, color_name = select_color_with_key(key)

    if color is not None:
        hsv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # BGR'yi HSV'ye çevir

        # Renk limitlerini al
        lowerLimit, upperLimit = get_limits(color)

        # Maskeyi uygula ve görüntüyü işleme al
        mask = cv2.inRange(hsv_image, lowerLimit, upperLimit)

        # Gürültüyü azaltmak için maske üzerine ek filtreler
        mask = cv2.GaussianBlur(mask, (5, 5), 0)  # Gaussian Blur
        mask = cv2.erode(mask, kernel, iterations=7)  # Erozyon işlemi (çekirdek matrisi ile)
        mask = cv2.dilate(mask, kernel, iterations=7)  # Dilate işlemi (çekirdek matrisi ile)

        # Kontur bulma
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            area = cv2.contourArea(contour)
            if area > min_contour_area:  # Sadece büyük konturları alalım
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 5)

        cv2.putText(frame, f"Color: {color_name}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2, cv2.LINE_AA)

    # Çerçeveyi göster
    cv2.imshow("frame", frame)

    if key == ord('q'):  # Programdan çıkış
        break

cap.release()
cv2.destroyAllWindows()