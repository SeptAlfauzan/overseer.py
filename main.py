import os
import cv2
import socket
from datetime import datetime
from ultralytics import YOLO
import numpy as np
from ultralytics.utils.plotting import Annotator
from ultralyticsplus import render_result
from io import BytesIO
import argparse


available_models = ["yolov8n", "yolov8n-ghostnet-p5", "yolov8n-ghostnet-p6"]

parser = argparse.ArgumentParser(
    prog="Overseer.io, program to detect student behavior",
    description="This program is used to detect student behavior such as sleep, on-phone, and study",
    epilog="Thank you, made with 💓",
)

parser.add_argument(
    "-m",
    "--model_name",
    type=str,
    choices=available_models,
    default=available_models[0],
)  # option that takes a value
parser.add_argument("-c", "--camera", type=int, default=0)  # on/off flag
parser.add_argument("-i", "--image", type=str, default=None)  # on/off flag
parser.add_argument("-s", "--save", type=bool, default=False)  # on/off flag

args = parser.parse_args()
print(args.model_name, args.camera, args.save)

models_paths = [
    os.path.abspath("./student-behavior/models/batch-32/yolov8n.pt"),
    os.path.abspath("./student-behavior/models/batch-32/yolov8n-ghostnet-p5.pt"),
    os.path.abspath("./student-behavior/models/batch-32/yolov8n-ghostnet-p6.pt"),
]

cap = cv2.VideoCapture(args.camera)
HOST = "127.0.0.1"  # Server's hostname or IP address
PORT = 12345  # Server's port

model = YOLO(
    models_paths[available_models.index(args.model_name)]
)  # load a pretrained model (recommended for training)

colors = [(255, 0, 255), (0, 255, 255), (255, 255, 9)]


if args.image != None:
    file_dir = "result.png"
    results = model.predict(
        source=args.image,
        imgsz=256,
        project="result_images",
    )

    render = render_result(model=model, image=args.image, result=results[0])
    render.save(fp=file_dir)
    frame = cv2.imread(file_dir)

    cv2.imshow("Overseer.io - Camera Feed", frame)
    cv2.waitKey(0)

    if args.save == False:
        os.remove(file_dir)

else:
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        results = model.predict(source=frame, imgsz=256)
        for r in results:
            annotator = Annotator(frame)

            boxes = r.boxes
            for box in boxes:
                b = box.xyxy[
                    0
                ]  # dapatkan koordinat kotak dalam format (top, left, bottom, right)
                c = box.cls

                score = box.conf.item() * 100
                class_id = int(box.cls.item())

                label = "{}: {}".format(model.names[int(c)], format(box.conf[0], ".2f"))
                annotator.box_label(
                    b,
                    label,
                    txt_color=(0, 0, 0),
                    color=colors[int(c)],
                )

            frame = annotator.result()
        # Display the resulting frame
        cv2.imshow("Overseer.io - Camera Feed", frame)

        # Check for 'q' key to exit the loop
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break


try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        # Get the current date and time
        current_date = datetime.now()
        # send the current date to socket server in Kotlin app
        str = "Camera program closed at: {}".format(current_date.date())
        s.sendall(str.encode())
except Exception as e:
    print(e)
# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
