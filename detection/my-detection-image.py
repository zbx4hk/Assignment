from jetson.inference import detectNet
from jetson.utils import videoSource, videoOutput
import jetson.inference
import jetson.utils



net = detectNet("ssd-mobilenet-v2", threshold=0.5)

picture=jetson.utils.loadImage("/home/nvidia/jetson-inference/examples/source.jpg")

detections = net.Detect(picture)

for i,detection in enumerate(detections):
            print(f"Detection {i+1}:")
            for attr in dir(detection):
                if not attr.startswith("_"):
                    print(f" {attr}: {getattr(detection,attr)}")

jetson.utils.saveImageRGBA("/home/nvidia/jetson-inference/examples/result.png",picture)
