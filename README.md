# deep-learning-threat-detection
Deep learning project using YOLOv5
# Intelligent Threat Detection System using Deep Learning

## Project Overview

This project is about detecting threats in time. It uses a webcam and a deep learning model called YOLOv5 to find objects and classify them as Low, Medium or High threat.

## Features

* Detect objects in time using a webcam

* Automatically classify threats

* Show bounding boxes with threat labels

* Play an alarm sound for high-level threats

* Use GPU if available

## Technologies Used

* Python

* PyTorch

* YOLOv5 (from Ultralytics)

* OpenCV

* Winsound (for alerts)

## Threat Classification Logic

Object Found | Classified As    | Threat Level  |

| --------------- | ---------------- | ------------- |

Person          | Soldier          | Medium Threat |

| Bird            | Drone            | Low Threat    |

| Airplane        | Fighter Jet      | High Threat   |

| Car/Truck/Bus   | Military Vehicle | Medium Threat |

| Boat            | Warship          | High Threat   |

## How to Run

1. Install needed packages:

pip install torch torchvision opencv-python

2. Run the program:

python threats.py

3. Press **'q'** to exit

## Output

* The system opens the webcam and detects objects in time

* It shows bounding boxes with threat labels

* It plays an alarm sound for high-level threats

## Notes

* Make sure webcam access is allowed

* Alarm sound works on Windows

* Internet is needed to download the YOLOv5 model for the time

## Future Improvements

* Train a custom model for better accuracy

* Add more threat categories

* Connect with CCTV. Live surveillance systems

* Create a web or mobile interface, for monitoring
