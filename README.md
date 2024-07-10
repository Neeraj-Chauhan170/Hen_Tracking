# Hen_Tracking

This project focuses on automating the tracking of hens in a video using advanced deep learning techniques. It utilizes the YOLO (You Only Look Once) model for instance segmentation and tracking. The process begins with annotating frames to detect hens, organizing these annotations for training, and subsequently training a custom YOLO model for segmentation. Once trained, the model is applied to a video feed, where it segments and tracks individual hens in real-time. The output is a video with annotated tracks, facilitating efficient monitoring and analysis of hen behavior.


1. Annotated the frames using `ultralytics auto annotator`

-> Run `python annotate.py` (See output annotate_output.txt)

This creates a folder under `data` named 'frames_auto_annotate_labels' and gives a .txt file for each frame containing the segmentations of the hens it detected.


2. Put the labels into a proper structure for training i.e. specify custom class (hen)

-> Run `python get_stuff.py`

This will put all the necesaary files under `train/labels`. Move the last 20 files to `val/labels` for validation in the next stripped


3. The model is now trained using a pretrained 'yolov8x-seg'. Ensure that the directory path is good

-> Run `yolo task=segment mode=train model=yolov8x-seg data=data.yaml epochs=20 imgsz=640` in a terminal opened in the directory
(See output train_output.txt)

This will create a `runs` folder and all the metrics and model weights will be stored there.


4. Use the best weights as input model for tracking

-> Run `python track.py` (See output output_track.py, uncomment line no. 34 if you want to visualize the output alongside running)

The final tracking video would be saved under the directory...
