# importing libraries
from ultralytics import YOLO
import cv2
import cvzone
import math

# # initialize Webcam
# cap = cv2.VideoCapture(0) # for Webcam
# #width
# cap.set(3,1920)
#
# #height
# cap.set(4, 1080)

cap = cv2.VideoCapture("../Videos/bikes.mp4") # for videos



# creating the model
model = YOLO("../Yolo-Weights/yolov8n.pt")


classNames = ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat",
              "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat",
              "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella",
              "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat",
              "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup",
              "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli",
              "carrot", "hot dog", "pizza", "donut", "cake", "chair", "sofa", "pottedplant", "bed",
              "diningtable", "toilet", "tvmonitor", "laptop", "mouse", "remote", "keyboard", "cell phone",
              "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors",
              "teddy bear", "hair drier", "toothbrush"
              ]

while True:
    success, img = cap.read()
    results = model(img, stream=True)
    # bounding boxes
    for r in results:
        boxes = r.boxes
        for box in boxes:
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            # print(x1, y1, x2, y2)
            # creating bounding boxes -- img, values, color, thinkness
            # cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)

            # xyxh -- xy width height
            # fancy boundry box
            w, h = x2-x1, y2-y1
            cvzone.cornerRect(img, (x1,y1,w,h))

            # now showing the confidence and taking up to 2 decimal points like 100 then divide by 100
            conf = (math.ceil(box.conf[0]* 100))/100
            print(conf)



            # class name
            cls = int(box.cls[0]) # str converting to integer
            # display confidence and class level, by creating a rectangle on the boundry box, scale for reducing the size of the text
            cvzone.putTextRect(img, f' {classNames[cls]} {conf}', (max(0, x1), max(40, y1)), scale=1, thickness=1)



    cv2.imshow("Image", img)
    cv2.waitKey(1)

