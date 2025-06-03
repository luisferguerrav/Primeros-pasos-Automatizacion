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

#acción 2: abrir la calculadora

pyautogui.hotkey('win', 'r')
time.sleep(2)
pyautogui.write('calc', interval=0.2)
pyautogui.press('enter')

#accion 3: hacer la multiplicacion 7*8

time.sleep(2)
pyautogui.press('7')
pyautogui.press('*')
pyautogui.press('8')
pyautogui.press('enter')

pyautogui.press('backspace')
time.sleep(2)

pyautogui.press('4')
pyautogui.press('+') #la sumatoria da error con el teclado y hace una multiplicacion
pyautogui.press('6')
pyautogui.press('enter')

#accion 4: borrar resultado anterior
borrar = pyautogui.locateOnScreen('borrar.png', confidence=0.8) #busco el simbolo del recorte 
centro1 = pyautogui.center(borrar) #encontar el centro
pyautogui.click(centro1)
pyautogui.press('enter')
time.sleep(2)

#accion 5: realizar 5 al cuadrado
pyautogui.press('5')
ubicacion = pyautogui.locateOnScreen('potencia.png', confidence=0.8) #busco el simbolo del recorte
centro = pyautogui.center(ubicacion) #encontar el centro
pyautogui.click(centro)


