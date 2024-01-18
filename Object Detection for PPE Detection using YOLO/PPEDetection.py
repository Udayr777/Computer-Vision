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

# cap = cv2.VideoCapture("../Videos/ppe-1-1.mp4") # for videos
cap = cv2.VideoCapture("../Videos/ppe-2-1.mp4") # for videos
# cap = cv2.VideoCapture("../Videos/ppe-3-1.mp4") # for videos



# creating the model
model = YOLO("best.pt")


classNames = ['Hardhat', 'Mask', 'NO-Hardhat', 'NO-Mask', 'NO-Safety Vest', 'Person', 'Safety Cone', 'Safety Vest', 'machinery', 'vehicle']

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
            # creating bounding boxes -- img, values, color, thikness
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

