
Here are the instructions for Object Detection for PPE kit, summarized in key points without code:

1) Obtain Dataset:

    -> Download the Construction Site Safety dataset from RoboFlow, specifically for YOLO V8.
    -> Extract the downloaded ZIP file.

2) Configure Data:

    -> Open the data.yaml file within the extracted dataset.
    -> Update the path within data.yaml to correctly point to your dataset's location.

3) Train Model:

    -> Utilize Google Colab and Google Drive to facilitate model training.
    -> Employ the YoloV8.ipynb file for training purposes.
    -> Initiate training using YoloV8l.pt as the model configuration.
    -> Set epoch to 50 and imgsz to 640 during the training process.

4) Utilize Trained Model:

    -> Locate the best-trained images, typically named best.pt, within the generated working folder.
    -> Integrate these best-trained images into a PyCharm project to execute PPE kit detection using the trained model





![ses](https://github.com/Udayr777/Computer-Vision/assets/18031941/97b73653-09cd-4d51-ae4b-a0bab07cf539)
