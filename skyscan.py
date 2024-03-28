import torch
import numpy as np
import cv2
import pandas as pd
import requests
import argparse

def process_video(video_path, output_path, model):
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        raise Exception("Could not open video file")
    
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_path, fourcc, 20.0, (width, height))

    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            results = model(frame)
        
            boxes = results.xyxy[0].numpy()
            boxes = boxes[boxes[:, -1] == 0]

            for box in boxes:
                x1, y1, x2, y2, _, _ = map(int, box)
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            
            cv2.putText(frame, f"Pedestrians: {len(boxes)}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            out.write(frame)
            cv2.imshow("Frame", frame)

            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
        else:
            break
    cap.release()
    out.release()
    cv2.destroyAllWindows()

def main():
    parser = argparse.ArgumentParser(prog="SkyScan", description="Scans the skies and outputs pedestrian count")
    parser.add_argument('inputpath', type=str, help='path to the input file')
    parser.add_argument('-o', "--outputpath", type=str, help='path to the output file')
    args = parser.parse_args()

    input_path = args.inputpath
    output_path = args.outputpath if args.outputpath else "output.avi"
    
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
    process_video(input_path, output_path, model)

if __name__ == "__main__":
    main()