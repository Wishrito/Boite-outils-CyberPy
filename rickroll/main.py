import os
import random
import sys
import webbrowser
from time import sleep

from win11toast import notify, update_progress


def runVideo(video_filename: str):
    chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
    webbrowser.get(chrome_path).open(video_filename)


def fakeNotif():

    notify(progress={
        'title': 'CyberToolbox',
        'status': 'loading',
        'value': '0',
        'valueStringOverride': ''
    })
    process_statuses = [
        "Extracting files...",
        "Loading Bootstrap...",
        "Initializing user interface...",
        "Loading data...",
        "Analyzing files...",
        "Optimizing performance...",
        "Reorganizing resources...",
        "Verifying file integrity...",
        "Validating settings...",
        "Finalizing process..."
    ]

    for i in range(1, len(process_statuses) + 1):
        randInt = random.randint(1, 3)
        randStatus = random.choice(process_statuses)
        sleep(randInt)
        update_progress({'value': i/10,
                        'valueStringOverride': randStatus})
        process_statuses.remove(randStatus)

    update_progress({'status': 'Completed!', 'valueStringOverride': ""})
    runVideo(video_filename)


if __name__ == "__main__":
    video_filename = ""
    if getattr(sys, 'frozen', False):  # Si le fichier est exécuté via PyInstaller
        video_filename = os.path.join(
            f"file:///{sys._MEIPASS}", 'rickroll.mp4')
    else:  # Si le script est exécuté comme un script Python classique
        video_filename = 'rickroll.mp4'

    fakeNotif()
