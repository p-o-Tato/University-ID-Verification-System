# University ID Verification System

Real-time OCR system for detecting and validating Georgian university ID codes using IP camera feed.

## Features
- Real-time video processing from IP camera
- OCR detection of numerical codes
- Georgian university code validation
- Visual feedback with bounding boxes
- Asynchronous frame processing

## Requirements
- Python 3.8+
- EasyOCR
- OpenCV
- Requests

## Setup
1. Install dependencies: `pip install -r requirements.txt`
2. Configure camera URL in `config.py`
3. Run: `python src/main.py`

## Project Structure
```
src/
├── config.py         # Configuration and constants
├── camera_handler.py # IP camera management
├── image_processor.py # OCR and image processing
├── display_manager.py # Display interface
└── main.py          # Application entry point
```

## Credits
This project uses [EasyOCR](https://github.com/JaidedAI/EasyOCR) for text detection and recognition.

## License
This project is licensed under the Apache License 2.0 - see the LICENSE file for details.

## Note
- IP camera access requires proper network configuration
- Smartphone can be used as IP camera using apps like "IP Webcam"
- Configure camera URL in config.py before running
