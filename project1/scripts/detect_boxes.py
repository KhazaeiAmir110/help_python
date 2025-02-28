import json
import os
from datetime import datetime

import cv2
from pyzbar import pyzbar


def detect_filled_boxes(image_path):
    """
    شناسایی جعبه‌های پر شده در یک تصویر.
    """
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    _, binary = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY_INV)
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    filled_boxes = []
    for i, contour in enumerate(contours):
        x, y, w, h = cv2.boundingRect(contour)
        if w > 20 and h > 20:  # فیلتر کردن جعبه‌های کوچک
            filled_boxes.append({"box_id": i, "is_filled": True})

    return filled_boxes


def process_sheets(input_dir, output_dir):
    """
    پردازش تمام تصاویر در دایرکتوری ورودی و ذخیره نتایج به‌صورت JSON.
    """
    for filename in os.listdir(input_dir):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            image_path = os.path.join(input_dir, filename)
            qr_code = pyzbar.decode(cv2.imread(image_path))
            if qr_code:
                identifier = qr_code[0].data.decode("utf-8")
                filled_boxes = detect_filled_boxes(image_path)
                result = {
                    "identifier": identifier,
                    "metadata": {
                        "page_number": 1,
                        "timestamp": datetime.now().isoformat()
                    },
                    "filled_boxes": filled_boxes
                }
                output_path = os.path.join(output_dir, f"{identifier}.json")
                with open(output_path, "w") as f:
                    json.dump(result, f, indent=4)


if __name__ == "__main__":
    input_dir = os.getenv("INPUT_DIR", "data/input")
    output_dir = os.getenv("OUTPUT_DIR", "results/detected")
    process_sheets(input_dir, output_dir)
