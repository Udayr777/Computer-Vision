# importing libraries
from ultralytics import YOLO
import cv2
import cvzone
import math
# importing from PokerHandFunction
import PokerHandFunction


# # initialize Webcam
cap = cv2.VideoCapture(0) # for Webcam 0 for front camera and 1 for back camera
#width
cap.set(3,1280)
#height
cap.set(4, 720)

# creating the model
model = YOLO("playingCards.pt")

classNames = ['10C', '10D', '10H', '10S',
              '2C', '2D', '2H', '2S',
              '3C', '3D', '3H', '3S',
              '4C', '4D', '4H', '4S',
              '5C', '5D', '5H', '5S',
              '6C', '6D', '6H', '6S',
              '7C', '7D', '7H', '7S',
              '8C', '8D', '8H', '8S',
              '9C', '9D', '9H', '9S',
              'AC', 'AD', 'AH', 'AS',
              'JC', 'JD', 'JH', 'JS',
              'KC', 'KD', 'KH', 'KS',
              'QC', 'QD', 'QH', 'QS']



while True:
    success, img = cap.read()
    results = model(img, stream=True)
    hand = []
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

            if conf > 0.5:
                hand.append(classNames[cls])
    print(hand)
    hand = list(set(hand))
    print(hand)
    if len(hand) == 5:
        results = PokerHandFunction.findPokerHand(hand)
        print(results)
        cvzone.putTextRect(img, f' Your Hand: {results}', (300, 75), scale=3, thickness=5)

    cv2.imshow("Image", img)
    cv2.waitKey(1)

