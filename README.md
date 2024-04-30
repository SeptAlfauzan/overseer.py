# Student Classroom Behaviour with Python & YOLOv8

This program is part of my undergraduate thesis. Using data that I've been collected from Roboflow site, taking photo from classroom, and scrapping through internet. This program will be used four kind YOLOv8 model weight:

1. YOLOv8n
2. YOLOv8n _with_ Ghostnet - P5
3. YOLOv8n _with_ Ghostnet - P6
4. YOLOv8s

## How to build?

To build this python program into standalone program, please **follow these instructions**

1. install the libraries from requirements.txt

```shell
pip install -r requirements. txt
```

2. build using pyinstaller by run this command

```shell
pyinstaller --onefile --paths=venv\Lib\site-packages --hidden-import=ultralytics --add-data '.\<venv_name>\Lib\site-packages\ultralytics\cfg\default.yaml;ultralytics/cfg/' main.py
```

    in this project I use virtual environtment, please replace the **<venv_name>(()) with your virtual env directory name
