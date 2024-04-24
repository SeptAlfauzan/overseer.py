import argparse

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
parser.add_argument("-i", "--index_camera", type=int)  # on/off flag

args = parser.parse_args()
print(args.model_name, args.index_camera)
