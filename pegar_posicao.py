import time
import pyautogui

# Espera 5 segundos para dar tempo de posicionar o cursos do mouse no local desejado
time.sleep(5)
# Printa a posicao do cursos na tela para utilizar como argumento da funcao click
print(pyautogui.position())

pyautogui.scroll(200)