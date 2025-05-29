import pyautogui
import time

#acción 1: minimizar Visual Studio Code
# utilizando la presión de la tecla "Win" + dos veces la flecha hacia abajo
# y soltando "Win" obtengo el efecto de minimizar la aplicación actual, en este caso 
# minimizo Visual Studio Code

pyautogui.keyDown('win')
pyautogui.press('down')
pyautogui.press('down')
pyautogui.keyUp('win')

time.sleep(1)

#acción 2: Abrir chrome desde el Menú Windows
# utilizando la tecla "Win" y abriendo la lista de programas 

pyautogui.press('win')
time.sleep(2)
pyautogui.write("chrome", interval=0.2) #escribo el nombre del programa 
pyautogui.press('enter') #con enter ejecuto el programa

#coordenadas 841, 506
time.sleep(2)

#coordenada: 841, 506 obtenidas del programa coordenadas.exe
#Acción 3: Mover el puntero del mouse a la coordenada en 2 segundos
# abrir el usuario para iniciar chrome

pyautogui.moveTo(841, 506, duration=2)
time.sleep(2)
pyautogui.click()

#accion 4: escribir en la busqueda y buscar google

pyautogui.write("google", interval=0.2)
pyautogui.press('enter')

#accion 5: cerrar chrome 
time.sleep(2)
pyautogui.hotkey('ctrl', 'F4')