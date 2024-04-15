import os
import sys

import cv2

if getattr(sys, 'frozen', False):  # Si le fichier est executé via Pyinstaller
    video_filename = os.path.join(sys._MEIPASS, 'rickroll.mp4')
else:  # Si le script est exécuté comme un script Python classique
    video_filename = 'rickroll.mp4'

cap = cv2.VideoCapture(video_filename)
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow('Video', frame)
    if cv2.waitKey(25) & 0xFF == ord('q') or cv2.getWindowProperty('Video', cv2.WND_PROP_VISIBLE) < 1:
        break
cap.release()
cv2.destroyAllWindows()
