# Skyscan

Skyscan is a demo created to demonstrate the capabilities of YOLOV5 with drone 
footage. Though only a demo, I plan to expand this project with more sample 
footage and features such as output logs and more trackable objects.

![Demo](./demo.gif)

In its current form, skyscan takes in drone footage of a group of pedestrians
and prints the current pedestrian count to the screen. The purpose of this program
is to be used for surveyers, interested determining the average foottraffic of
a given area. Future iterations will include more tools for analyzing the data
from the footage.

# Prerequisites
* python
  ```sh
  pip install -r requirements. txt
  ```

# Usage
    ```sh
    python skyscan.py input.mp4 -o output.mp4
    ```
