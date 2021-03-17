def main():
    import pyautogui

    while True:
        x, y = pyautogui.position()
        print("X : " + str(x) + " Y : " + str(y))
    # screenWidth, screenHeight = pyautogui.size()
    # pyautogui.moveTo(screenWidth / 2, screenHeight / 2)


if __name__ == "__main__":
    main()
