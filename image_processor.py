import cv2
import numpy as np
import easyocr


class ImageProcessor:
    def __init__(self):
        self.reader = easyocr.Reader(['en'])

    def resize_image(self, image, scale_factor=1 / 2):
        width = int(image.shape[1] * scale_factor)
        height = int(image.shape[0] * scale_factor)
        return cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)

    def draw_detections(self, img, detected_codes, scale_factor=1):
        for code, city, coordinates in detected_codes:
            coordinates = np.array(coordinates).astype(int)
            if scale_factor != 1:
                coordinates = (coordinates * scale_factor).astype(int)
            cv2.polylines(img, [coordinates], True, (0, 255, 0), 3)
            cv2.putText(img, f"{code}", tuple(coordinates[0] - 1),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8 * scale_factor, (0, 255, 0), 2)
        return img

    def process_image(self, img):
        result = self.reader.readtext(img, allowlist='0123456789')
        return [(text, '', coordinates) for coordinates, text, confidence in result]