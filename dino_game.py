import pyautogui
if __name__=="__main__":
  #color may change due to browser theme
    obstacle_color = (172,172,172)
    dino_color  = (172,172,172)
    xd,yd= 636,291
    #checks if dino game is open
    if dino_color== pyautogui.pixel(xd,yd):
        while True:
          #when it detects obstacle passing through (x,y) jump
            x, y = 729,288
            current_color= pyautogui.pixel(x,y)
            if current_color == obstacle_color:
                pyautogui.press('space')
