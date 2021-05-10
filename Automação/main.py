import pyautogui
from pynput.mouse import Button, Controller
import time


pyautogui.alert("O código vai começar. Não use nada do seu computador enquanto o código está rodando")
pyautogui.PAUSE = 0.5
time.sleep(0.3)
# abrir o google drive no meu computador
pyautogui.hotkey('command', 'space')
pyautogui.typewrite('chrome')
pyautogui.hotkey('enter')
time.sleep(1)
pyautogui.hotkey('command', 'l')
pyautogui.typewrite("https://drive.google.com/drive/my-drive")
pyautogui.press('enter')

# # entrar na minha área de trabalho
pyautogui.hotkey('command', 'm')
# # cliquei no arquivo que eu quero fazer backup e arrastei ele
mouse = Controller()
pyautogui.moveTo(1227, 54, duration=1)
pyautogui.leftClick()
pyautogui.dragTo()
# pyautogui.dragTo()
# pyautogui.mouseDown()
pyautogui.moveTo(980, 577, duration=1)
#
# # enquanto eu to arrastando, eu vou mudar para o google drive
pyautogui.hotkey('command', 'm')
time.sleep(1)
# # larguei o arquivo no google drive
pyautogui.mouseUp()
#
# # esperar 5 segundos
time.sleep(5)
#
pyautogui.alert("O código acabou de rodar. Pode usar o seu computador de novo")