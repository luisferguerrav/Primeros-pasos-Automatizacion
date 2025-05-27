import pyautogui

#coordenada: 470, 363
#coordenada2: 569, 160

pyautogui.moveTo(470, 363, duration= 3)
pyautogui.click()
pyautogui.write("escribo en el block de notas", interval=0.2)

pyautogui.moveTo(569, 160, duration= 3)
pyautogui.click()
pyautogui.write("texto para este renglon", interval=0.2)
