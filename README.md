# Left Hand & Right Hand Detection Using On-Device AI Model

## Overview
This project implements a real-time left-hand and right-hand detection system using an on-device AI model. It leverages Python with OpenCV (`cv2`) for image processing and MediaPipe for hand tracking and classification.

## Features
- **Real-time Hand Detection**: Detects hands from webcam input.
- **Left/Right Hand Classification**: Differentiates between left and right hands using AI-based landmark analysis.
- **On-Device Processing**: Runs without needing an internet connection, ensuring privacy and efficiency.

## Tech Stack
- **Python**: Programming language used for implementation.
- **OpenCV (`cv2`)**: Handles video capture and image processing.
- **MediaPipe**: Provides robust hand tracking and landmark detection.
- **NumPy**: Used for numerical computations.

## Installation
### Prerequisites
Ensure you have Python (>=3.7) installed. Then, install the required dependencies:

```sh
pip install opencv-python mediapipe numpy
```

## Usage
Run the following script to start the hand detection:

```sh
python hand_detection.py
```

## Contribution
Feel free to contribute by submitting pull requests or reporting issues!


