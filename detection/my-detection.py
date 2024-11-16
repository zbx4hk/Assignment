from jetson.inference import detectNet
from jetson.utils import videoSource, videoOutput
import jetson.inference
import jetson.utils

import ctypes




camera = videoSource("/dev/video0") # '/dev/video0' for V4L2

display = videoOutput("display://0") # 'my_video.mp4' for file

while display.IsStreaming(): # main loop will go here

    display = videoOutput("display://0") # 'my_video.mp4' for file
    while display.IsStreaming(): # main loop will go here
        img = camera.Capture()
        if img is None: # capture timeout
            continue

        detections = net.Detect(img)
        
        for i,detection in enumerate(detections):
            print(f"Detection {i+1}:")
            for attr in dir(detection):
                if not attr.startswith("_"):
                    print(f" {attr}: {getattr(detection,attr)}")

        # print(detections)

        display.Render(img)
        display.SetStatus("Object Detection | Network {:.0f} FPS".format(net.GetNetworkFPS()))

