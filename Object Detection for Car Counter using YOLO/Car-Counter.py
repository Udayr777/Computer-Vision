# importing libraries
import numpy as np
from ultralytics import YOLO
import cv2
import cvzone
import math

from sort import *


cap = cv2.VideoCapture("../Videos/cars.mp4") # for videos



# creating the model
model = YOLO("../Yolo-Weights/yolov8l.pt")


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
mask = cv2.imread("mask.png")

# tracking using SORT algorithm
tracker = Sort(max_age=20, min_hits=3, iou_threshold=0.3)

# limits for the line tracking
limits = [400, 297, 673, 297]
totalCount = []


while True:
    success, img = cap.read()

    # Resize the mask to match the dimensions of the input image
    mask = cv2.resize(mask, (img.shape[1], img.shape[0]))

    # to take the image region
    imgRegion = cv2.bitwise_and(img, mask)

    # create the magic
    imgGraphics = cv2.imread("gp.png", cv2.IMREAD_UNCHANGED)
    img = cvzone.overlayPNG(img, imgGraphics,(0,0))

    results = model(imgRegion, stream=True)

    detections = np.empty((0, 5))


    # help to gets the id number, and remember
    dets = np.empty((0, 5))

    # bounding boxes
    for r in results:
        boxes = r.boxes
        for box in boxes:
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            # print(x1, y1, x2, y2)
            # creating bounding boxes -- img, values, color, thikness
            # cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)

            # xyxh -- xy width height
            # fancy boundry box
            w, h = x2-x1, y2-y1


            # now showing the confidence and taking up to 2 decimal points like 100 then divide by 100
            conf = (math.ceil(box.conf[0]* 100))/100
            print(conf)


            # class name
            cls = int(box.cls[0]) # str converting to integer
            currentClass = classNames[cls]

            if currentClass == "bus" or currentClass == "car" or currentClass == "motorbike" \
                    or currentClass == "truck"  and conf > 0.3:
                # display confidence and class level, by creating a rectangle on the boundry box, scale for reducing the size of the text
                # cvzone.putTextRect(img, f' {currentClass} {conf}', (max(0, x1), max(40, y1)), scale=0.6, thickness=1, offset=3)
                # cvzone.cornerRect(img, (x1, y1, w, h), l=8, rt=5)

                currentArray = np.array([x1, y1, x2, y2, conf])
                detections = np.vstack((detections, currentArray))

    resultsTracker = tracker.update((detections))

    # now mark a line to count the vehicle
    cv2.line(img, (limits[0], limits[1]),(limits[2],limits[3]), (0, 0, 255), 5)

    for result in resultsTracker:
        x1, y1, x2, y2, id = result
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
        print(result)
        w, h = x2 - x1, y2 - y1
        cvzone.cornerRect(img, (x1, y1, w, h), l=8, rt=2, colorR=(255, 0 , 255))
        # display confidence and class level, by creating a rectangle on the boundry box, scale for reducing the size of the text
        cvzone.putTextRect(img, f' {int(id)}', (max(0, x1), max(40, y1)), scale=2, thickness=3, offset=10)

        # point to the center and check the count
        cx, cy = x1+w//2, y1+h//2
        cv2.circle(img, (cx, cy), 5, (255,0,255), 5, cv2.FILLED)

        # to count the number of vehicle with respect to the points
        if limits[0] < cx < limits[2] and limits[1] - 20 < cy < limits[1] + 15:
            if totalCount.count(id) == 0:
                totalCount.append(id)
                # now mark a line to count the vehicle
                cv2.line(img, (limits[0], limits[1]), (limits[2], limits[3]), (0, 255, 0), 5)

    # cvzone.putTextRect(img, f' Count: {len(totalCount)} ', (50,50))
    cv2.putText(img, str(len(totalCount)),(255,100), cv2.FONT_HERSHEY_PLAIN, 5, (50,50,255),8)


    cv2.imshow("Image", img)
    # cv2.imshow("ImageRegion", imgRegion)
    cv2.waitKey(1)

