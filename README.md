# Image Enhancement Toolkit

## Overview
Image Enhancement Toolkit is a simple desktop application built with PyQt6 and OpenCV that allows users to perform basic image processing operations. The current version features Gaussian blur functionality with an interactive slider control.

## Features
- Load images in various formats (PNG, JPG, JPEG, BMP)
- Apply Gaussian blur with adjustable intensity
- Real-time preview of effects
- Save processed images

## Requirements
```
Python 3.x
PyQt6
OpenCV (cv2)
numpy
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/Image-Enhancement-Toolkit.git
cd Image-Enhancement-Toolkit
```

2. Install the required dependencies:
```bash
pip install PyQt6 opencv-python numpy
```

## Usage

1. Run the application:
```bash
python image_enhancement.py
```

2. Using the application:
   - Click "Load Image" to select an image file
   - Use the slider to adjust the blur intensity
   - Click "Save Image" to save the processed image

## Application Controls
- **Load Image Button**: Opens a file dialog to select an image
- **Blur Slider**: Adjusts the intensity of the Gaussian blur (range: 1-50)
- **Save Image Button**: Opens a file dialog to save the processed image

## Technical Details
- Built using PyQt6 for the GUI
- Uses OpenCV for image processing operations
- Supports common image formats (PNG, JPG, JPEG, BMP)
- Maintains aspect ratio when displaying images
- Automatically adjusts kernel size for Gaussian blur to ensure odd numbers

## Contributing
Feel free to fork the repository and submit pull requests for any improvements you'd like to add. Some potential areas for enhancement:
- Additional image processing filters
- Brightness/Contrast controls
- Color adjustment options
- Batch processing capabilities

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Author
[Your Name]

## Acknowledgments
- PyQt6 team for the GUI framework
- OpenCV team for the image processing capabilities

## Version
1.0.0
