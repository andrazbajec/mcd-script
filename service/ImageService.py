from datetime import datetime
from os import makedirs
import pyautogui
import os

class ImageService:
    def screenshot(self):
        image = pyautogui.screenshot()
        now = datetime.now()
        folder=now.strftime('data/%Y/%m/%d')
        path = now.strftime(f'{folder}/%Y-%m-%d %H-%M.png')

        if not os.path.exists(folder):
            makedirs(folder)

        image.save(path)
        
        return path
