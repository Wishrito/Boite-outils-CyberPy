cd rickroll
pyinstaller --noconsole --onefile --name CyberToolbox --add-data "box.ico;." --add-data "rickPog.jpg;." --add-data "rickroll.mp4;." --icon=box.ico main.py