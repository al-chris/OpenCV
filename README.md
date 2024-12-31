# OpenCV object detection in kivy

This repository showcases a series of projects developed using OpenCV, focusing on image processing, real-time object detection, and deploying an Android application with Kivy for real-time object detection.
It began with experimenting with image processing techniques using OpenCV, progressed to implementing real-time object detection, and culminated in developing a single-file Kivy application for performing real-time object detection on Android devices.

## Project Overview

1. **Image Processing with OpenCV**:
   - Explored fundamental image processing techniques, including image filtering, edge detection, and color space transformations.

2. **Real-Time Object Detection**:
   - Implemented object detection algorithms capable of identifying and classifying objects in live video streams.

3. **Kivy Application for Android**:
   - Developed a single-file Kivy application to perform real-time object detection on Android devices, integrating OpenCV with Kivy for mobile deployment.

## Repository Structure

```
OpenCV/
├── assets/                 # Directory containing image and video assets
├── app.py                  # Kivy application script for Android deployment
├── main.py                 # Script for real-time object detection
├── image_processing.py     # Script demonstrating basic image processing techniques
├── requirements.txt        # List of required Python packages
└── README.md               # Project documentation
```

## Getting Started

To explore and run these projects:

1. **Clone the repository**:

   ```bash
   git clone https://github.com/al-chris/OpenCV.git
   cd OpenCV
   ```

2. **Set up a virtual environment** (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install the required packages**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the scripts**:

   - For image processing demonstrations:

     ```bash
     python image_processing.py
     ```

   - For real-time object detection:

     ```bash
     python main.py
     ```

   - To deploy the Kivy application on Android, follow the instructions provided in `app.py`.

## Prerequisites

- **Python 3.7 or higher**
- **OpenCV**: Ensure that OpenCV is installed in your environment.
- **Kivy**: Required for developing and running the Android application.

## Contributing

Contributions are welcome. Feel free to open issues or submit pull requests to enhance the functionality or add new features.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments

- [OpenCV](https://opencv.org/): Open Source Computer Vision Library
- [Kivy](https://kivy.org/): Open source Python library for rapid development of applications

For any questions or suggestions, please contact [Christopher Aliu](https://github.com/al-chris). 
