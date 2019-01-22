import sys
import cv2
import os


def read_args():
    return dict(username=sys.argv[2], filename=sys.argv[3])


args = read_args()

cap = cv2.VideoCapture(args["filename"])
length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
distance = round(length / 4)
specific_frames = [0, distance, distance * 2, distance * 3, length - 1]

count = 0
while cap.isOpened():
    while count < length:
        ret, frame = cap.read()
        if count in specific_frames:
            cv2.imwrite(os.path.join("frames", "frame%d.jpg") % count, frame)
        count += 1

    break

cap.release()
cv2.destroyAllWindows()

