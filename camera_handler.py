import requests
import numpy as np
import cv2
from config import CAMERA_URL


class CameraHandler:
    def __init__(self, url=CAMERA_URL):
        self.camera_url = url

    async def get_frame(self):
        try:
            img_resp = requests.get(self.camera_url, timeout=5)
            img_resp.raise_for_status()
            img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
            return cv2.imdecode(img_arr, -1)
        except Exception as e:
            print(f"Error fetching frame: {e}")
            return None