## Overview

This project is a Computer Vision application that detects plastic waste objects such as bottles and cups using YOLOv8 and OpenCV. The system can perform real-time detection through a webcam or process video files for automated plastic waste identification.

## Features

* Real-time webcam detection
* Video file detection
* YOLOv8 object detection model
* Plastic object filtering (Bottle and Cup)
* Bounding box visualization with confidence scores
* Easy-to-use Python implementation

## Technologies Used

* Python
* YOLOv8 (Ultralytics)
* OpenCV
* Git & GitHub

## Project Structure

```text
plastic_project/
├── datasets/
├── runs/
├── data.yaml
├── plastic_detect.py
├── yolov8n.pt
├── README.md
└── .gitignore
```

## Installation

1. Clone the repository

```bash
git clone https://github.com/Shivapriya411/plastic-waste-detection.git
```

2. Install dependencies

```bash
pip install ultralytics opencv-python
```

3. Run the project

```bash
python plastic_detect.py
```

## Usage

When prompted:

```text
Enter 'cam' for Live Camera or 'video' for Video File:
```

* Type `cam` for webcam detection.
* Type `video` to detect plastic objects in a video file.

## Model Information

* Model: YOLOv8 Nano (`yolov8n`)
* Dataset: Custom Plastic Bottle Dataset
* Framework: Ultralytics YOLOv8

## Results

The model successfully detects plastic waste objects and displays:

* Bounding Boxes
* Object Labels
* Confidence Scores

(Add screenshots here)

## Applications

* Smart Waste Management
* Environmental Monitoring
* Recycling Automation
* Smart City Solutions

## Future Enhancements

* Detect more plastic waste categories
* Improve detection accuracy
* Deploy as a web application
* Real-time mobile integration

## Author

**Shivapriya**

Computer Science Student | AI & Machine Learning Enthusiast

GitHub: https://github.com/Shivapriya411
<img width="1246" height="1280" alt="image" src="https://github.com/user-attachments/assets/fa71de30-d4c7-40c7-aaa2-3ff7661e9a75" />
<img width="1280" height="971" alt="image" src="https://github.com/user-attachments/assets/c133f0ed-5d59-4d21-8fd1-57a3b777952a" />

