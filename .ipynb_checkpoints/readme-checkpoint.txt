0. Directory structure:
    Hen Tracking
    |_data
    |   |_frames
    |   |   |_frame_0.jpg, frame_1.jpg, ..., frame_204.jpg
    |   |_video
    |       |_video.mkv
    |
    |_train
    |   |_images
    |   |   |_ first 190 images
    |   |_labels 
    |
    |_test
    |   |_images
    |   |   |_ remaining 20 images
    |   |_labels
    |
    |_annotate.py
    |
    |_get_stuff.py
    |
    |_track.py
    |
    |_data.yaml


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

Cheers...