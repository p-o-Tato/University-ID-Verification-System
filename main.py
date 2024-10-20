import asyncio
from concurrent.futures import ThreadPoolExecutor
import time
import cv2
from image_processor import ImageProcessor
from camera_handler import CameraHandler
from display_manager import DisplayManager


async def main():
    image_processor = ImageProcessor()
    camera = CameraHandler()
    display = DisplayManager()
    executor = ThreadPoolExecutor(max_workers=1)
    scale_factor = 2 / 5
    last_process_time = 0
    processing = False

    try:
        while True:
            original_frame = await camera.get_frame()
            if original_frame is None:
                await asyncio.sleep(0.5)
                continue

            display_frame = image_processor.resize_image(original_frame, scale_factor)
            display.show_frame(display_frame, "Auto-detecting. ESC to quit", scale_factor)

            current_time = time.time()
            if not processing and current_time - last_process_time >= 0.2:
                processing = True
                last_process_time = current_time

                detected_codes = await asyncio.get_event_loop().run_in_executor(
                    executor, image_processor.process_image, original_frame)

                if detected_codes:
                    print("\nDetected Codes:")
                    for code, city, _ in detected_codes:
                        print(f"Code: {code}, City: {city}")

                    processed_display = image_processor.draw_detections(
                        display_frame.copy(), detected_codes, scale_factor)
                    display.show_frame(processed_display)
                else:
                    print("No valid codes detected.")

                processing = False

            if cv2.waitKey(1) == 27:  # ESC
                break

            await asyncio.sleep(0.01)
    finally:
        display.cleanup()
        executor.shutdown()


if __name__ == "__main__":
    asyncio.run(main())