def main():
    import pyautogui
    import serial
    import subprocess
    import os
    import time

    speed = 50
    # port = input("Quel port voulez-vous ? ")

    # port = "/dev/rfcomm4"
    # port = "/dev/ttyUSB0"
    ignore = ["", "4294967295", "255"]
    tour = -1
    while True:
        tour += 1
        if tour == 0:
            baseport = "/dev/ttyACM"
        elif tour == 1:
            baseport = "/dev/USB"
        elif tour == 2:
            baseport = "/dev/rfcomm"
            tour = -1
            time.sleep(1)
        for i in range(10):
            try:
                port = baseport+str(i)
                with serial.Serial(port, 9600, timeout=10, writeTimeout=10) as port_serie:
                    if port_serie.isOpen():
                        print(port)
                        while True:
                            x, y = pyautogui.position()
                            ligne = port_serie.readline()
                            ligne = str(ligne)
                            ligne = ligne.replace("b'", "", 1)
                            ligne = ligne.replace("'", "")
                            ligne = ligne.replace("\\n", "")
                            ligne = ligne.replace("\\r", "")
                            # if ligne != "":
                            if ligne in ignore:
                                pass
                            else:
                                print(ligne)
                            try:
                                if ligne == "DOWN":
                                    pyautogui.moveTo(x, y + speed)
                                if ligne == "UP":
                                    pyautogui.moveTo(x, y - speed)
                                elif ligne == "RIGHT":
                                    pyautogui.moveTo(x + speed, y)
                                elif ligne == "LEFT":
                                    pyautogui.moveTo(x - speed, y)
                                elif ligne == "CLICK":
                                    pyautogui.click()
                                elif ligne == "RIGHT_CLICK":
                                    pyautogui.click(button='right')
                                elif ligne == "SCROLL_UP":
                                    pyautogui.scroll(1)
                                elif ligne == "SCROLL_DOWN":
                                    pyautogui.scroll(-1)
                                elif ligne == "OFF":
                                    os.popen("systemctl suspend")
                            except:
                                pass
            except:
                pass
    # x, y = pyautogui.position()
    # print("X : " + str(x) + " Y : " + str(y))
    # screenWidth, screenHeight = pyautogui.size()
    # pyautogui.moveTo(screenWidth / 2, screenHeight / 2)


if __name__ == "__main__":
    main()
