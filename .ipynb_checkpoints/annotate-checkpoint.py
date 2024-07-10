from ultralytics.data.annotator import auto_annotate

auto_annotate(data="./data/frames", det_model="yolov10x.pt", sam_model="sam_l.pt")