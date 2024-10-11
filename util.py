import  numpy as np
import  cv2

def get_limits(color):
    # Renk BGR formatında geliyor ve HSV formatına çevriliyor
    c = np.uint8([[color]])
    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)

    # HSV formatında hue değeri (0 ile 180 arasında)
    hue = int(hsvC[0][0][0])

    # Hue değeri için alt ve üst sınırları döngüsel hale getiriyoruz
    lower_hue = (hue - 15) % 180  # Alt sınırı döngüsel olarak hesapla
    upper_hue = (hue + 15) % 180  # Üst sınırı döngüsel olarak hesapla

    lowerLimit = np.array([lower_hue, 70, 70], dtype=np.uint8)  # Doygunluk ve parlaklık sabitleniyor
    upperLimit = np.array([upper_hue, 255, 255], dtype=np.uint8)

    return lowerLimit, upperLimit

def select_color_with_key(keys):
    if keys == ord('1'):  # Red
        c_color = [0, 0, 255]
        print("You selected: Red")
        return c_color, 'Red'
    elif keys == ord('2'):  # Green
        c_color = [0, 100, 0]
        print("You selected: Green")
        return c_color, 'Green'
    elif keys == ord('3'):  # Blue
        c_color = [255, 0, 0]
        print("You selected: Blue")
        return c_color, 'Blue'
    elif keys == ord('4'):  # Yellow
        c_color = [0, 255, 255]
        print("You selected: Yellow")
        return c_color, 'Yellow'
    elif keys == ord('5'):  # Cyan
        c_color = [255, 255, 0]
        print("You selected: Cyan")
        return c_color, 'Cyan'
    elif keys == ord('6'):  # Magenta
        c_color = [255, 0, 255]
        print("You selected: Magenta")
        return c_color, 'Magenta'
    elif keys == ord('7'):  # Orange
        c_color = [0, 100, 200]
        print("You selected: Orange")
        return c_color, 'Orange'
    elif keys == ord('8'):  # Purple
        c_color = [128, 0, 128]
        print("You selected: Purple")
        return c_color, 'Purple'
    else:
        return None, None