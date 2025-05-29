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

#acción 2: Abrir el Bloc de Notas desde el Menú Windows
# utilizando la tecla "Win" y abriendo la lista de programas 

pyautogui.press('win')
time.sleep(2)
pyautogui.write("bloc de", interval=0.3) #escribo el nombre de programa para abrir
pyautogui.press('enter') #con enter ejecuto el programa

time.sleep(2)

#acción 3: Maximizar el Bloc de Notas
# espero medio segundo a que inicie el bloc de notas y presiono a la vez Win + Up

pyautogui.hotkey('win', 'up')

#accion 4: escribo un texto
pyautogui.write("hola este es un texto", interval=0.3)

#acción 5:
#Hago el llamado de cerrar el Block con las teclas Ctrol + F4

time.sleep(2)
pyautogui.hotkey('ctrl', 'F4')

#acción 6:
#El bloc, al reconocer la solicitud de cierre del programa, me solicita la confirmación de
# Guardar / No Guardar / Cancelar, para saber que hace con el texto
# Presiono la tecla de la flecha a la derecha para mover el cursor a la opcion "No Guardar"
# y después un enter sobre esa opción, entonces se cierra el Bloc

time.sleep(2)
pyautogui.press('right') #tecla hacia la derecha
pyautogui.press('enter') #presiono enter 

#listo de cerro el bloc de notas 
