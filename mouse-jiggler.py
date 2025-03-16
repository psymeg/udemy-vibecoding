import pyautogui
import time
import threading
import pygame

def detect_mouse_movement():
    last_position = pyautogui.position()
    while True:
        time.sleep(2)  # Check every 2 seconds
        new_position = pyautogui.position()
        if new_position != last_position:
            print("Mouse moved by user. Stopping jiggler.")
            return True
        last_position = new_position

def play_music():
    pygame.mixer.init()
    pygame.mixer.music.load("/share/music/Infected Mushroom/Converting Vegetarians/01 - Converting Vegetarians.mp3")  # Ensure you have this file in the same directory
    pygame.mixer.music.play()

def jiggle_mouse():
    print("Mouse jiggler started. Move your mouse to stop it.")
    stop_event = threading.Event()
    detector_thread = threading.Thread(target=lambda: stop_event.set() if detect_mouse_movement() else None)
    detector_thread.start()
    
    play_music()
    
    while not stop_event.is_set():
        pyautogui.moveRel(5, 0, duration=0.2)  # Move slightly to the right
        pyautogui.moveRel(-5, 0, duration=0.2) # Move back to original position
        time.sleep(3)  # Wait before the next move
    
    pygame.mixer.music.stop()
    print("Mouse jiggler stopped.")

if __name__ == "__main__":
    jiggle_mouse()
