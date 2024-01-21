Here are the instructions for Object Detection for Poker cards, summarized in key points without code:

Obtain Dataset:

-> Download the Poker card image dataset from RoboFlow, specifically for YOLO V8. -> Extract the downloaded ZIP file.

Configure Data:

-> Open the data.yaml file within the extracted dataset. -> Update the path within data.yaml to correctly point to your dataset's location.

Train Model:

-> Utilize Google Colab and Google Drive to facilitate model training. -> Employ the YoloV8.ipynb file for training purposes. -> Initiate training using YoloV8l.pt as the model configuration. -> Set epoch to 50 and imgsz to 640 during the training process.

Utilize Trained Model:

-> Locate the best-trained images, typically named best.pt, within the generated working folder. -> Integrate these best-trained images into a PyCharm project to execute PPE kit detection using the trained model



![poker2](https://github.com/Udayr777/Computer-Vision/assets/18031941/b4c1ee05-c0d6-4f0b-ae69-993d09456725)


