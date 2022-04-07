import cv2
from cv2 import mean
import matplotlib.pyplot as plt
import bleedfacedetector as fd
import base64
import numpy as np


def init_emotion(model="./emotion-ferplus-8.onnx") -> None:
    # Set global variables
    global net, emotions

    # Define the emotions
    emotions = ["Neutral", "Happy", "Surprise", "Sad", "Anger"]

    # Initialize the DNN module
    net = cv2.dnn.readNetFromONNX(model)


def emotion(image) -> dict:
    # Make copy of  image
    img_copy = image.copy()

    # Detect faces in image
    faces = fd.ssd_detect(img_copy, conf=0.2)

    if len(faces) > 1 or len(faces) == 0:
        return {}

    # Define padding for face ROI
    padding = 3

    # Iterate process for all detected faces
    for x, y, w, h in faces:

        # Get the Face from image
        face = img_copy[y - padding : y + h + padding, x - padding : x + w + padding]

        # Convert the detected face from BGR to Gray scale
        gray = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

        # Resize the gray scale image into 64x64
        resized_face = cv2.resize(gray, (64, 64))

        # Reshape the final image in required format of model
        processed_face = resized_face.reshape(1, 1, 64, 64)

        # Input the processed image
        net.setInput(processed_face)

        # Forward pass
        Output = net.forward()

        # Compute softmax values for each sets of scores
        expanded = np.exp(Output - np.max(Output))
        probablities = expanded / expanded.sum()

        # Get the final probablities by getting rid of any extra dimensions
        prob = np.squeeze(probablities)

        percentage = np.multiply(prob, 100)

        return percentage


def run_model(data):
    res = {}

    for genre in data:

        res[genre] = {}

        meanProbs = {}

        lenght = 0

        for screen in data[genre]:
            screen_base64 = screen.replace("data:image/jpeg;base64,", "")
            decoded_data = base64.b64decode(screen_base64)
            np_data = np.frombuffer(decoded_data, np.uint8)
            img = cv2.imdecode(np_data, cv2.IMREAD_UNCHANGED)

            emoProbs = emotion(img)

            if not any(emoProbs):
                continue

            lenght += 1

            for emoProb, emo in zip(emoProbs, emotions):
                if emo in meanProbs:
                    meanProbs[emo] += emoProb
                else:
                    meanProbs[emo] = emoProb

        for emo in meanProbs:
            res[genre][emo] = round(meanProbs[emo] / lenght, 2)

    return res
