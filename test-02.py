import pyautogui

#coordenada: 470, 363 obtenidas del programa coordenadas.exe
#Acción 1: Mover el puntero del mouse a la coordenada en 3 segundos


pyautogui.moveTo(470, 363, duration= 3)
#Acción 2: Hacer click sobre el block de notas
pyautogui.click()
#Acción 3: Escribir un texto con 0.2 seg de demora entre cada letra
pyautogui.write("escribo en el block de notas", interval=0.2)

#coordenada2: 569, 160 obtenidas del programa coordenadas.exe
pyautogui.moveTo(569, 160, duration= 3)

#Acción 4: Hacer click sobre el block de notas
pyautogui.click()
#Acción 5: Escribir un texto con 0.2 seg de demora entre cada letra
pyautogui.write("texto para este renglon", interval=0.2)
