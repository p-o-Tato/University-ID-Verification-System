import cv2


class DisplayManager:
    def __init__(self):
        cv2.namedWindow("Preview")

    def show_frame(self, frame, processing_message=None, scale_factor=1):
        if processing_message:
            cv2.putText(frame, processing_message, (10, 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8 * scale_factor, (0, 0, 255), 1)
        cv2.imshow("Preview", frame)

    def cleanup(self):
        cv2.destroyAllWindows()