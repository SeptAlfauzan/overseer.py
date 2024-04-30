import argparse
import cv2

parser = argparse.ArgumentParser(
    prog="SCB Detection",
    description="This program is used to detect student behavior such as sleep, on-phone, and study",
    epilog="Thank you, made with 💓",
)

parser.add_argument(
    "-m",
    "--model_name",
    type=str,
    choices=["yolov8n", "yolov8n-ghostnet-p5", "yolov8n-ghostnet-p6"],
)  # option that takes a value
parser.add_argument("-i", "--index_camera", type=int, default=0)  # on/off flag


args = parser.parse_args()

vid = cv2.VideoCapture(args.index_camera)

while True:
    # Capture the video frame
    # by frame
    ret, frame = vid.read()
    # Display the resulting frame
    cv2.imshow("frame", frame)
    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()

print(args.model_name, args.index_camera)
