import json
import os


def calculate_accuracy(detected_dir, true_dir):
    """
    محاسبه دقت نتایج شناسایی جعبه‌ها.
    """
    true_positives = 0
    false_positives = 0
    true_negatives = 0
    false_negatives = 0
    perfect_pages = 0

    for filename in os.listdir(detected_dir):
        if filename.endswith(".json"):
            detected_path = os.path.join(detected_dir, filename)
            true_path = os.path.join(true_dir, filename)

            with open(detected_path, "r") as f:
                detected_data = json.load(f)
            with open(true_path, "r") as f:
                true_data = json.load(f)

            for detected_box, true_box in zip(detected_data["filled_boxes"], true_data["filled_boxes"]):
                if detected_box["is_filled"] == true_box["is_filled"]:
                    if detected_box["is_filled"]:
                        true_positives += 1
                    else:
                        true_negatives += 1
                else:
                    if detected_box["is_filled"]:
                        false_positives += 1
                    else:
                        false_negatives += 1

            if false_positives == 0 and false_negatives == 0:
                perfect_pages += 1

    total = true_positives + false_positives + true_negatives + false_negatives
    accuracy = (true_positives + true_negatives) / total * 100 if total > 0 else 0

    return {
        "true_positive": true_positives,
        "false_positive": false_positives,
        "true_negative": true_negatives,
        "false_negative": false_negatives,
        "accuracy": accuracy,
        "perfect_pages": perfect_pages
    }


if __name__ == "__main__":
    detected_dir = os.getenv("DETECTED_DIR", "results/detected")
    true_dir = os.getenv("TRUE_DIR", "data/true")
    accuracy_report = calculate_accuracy(detected_dir, true_dir)

    output_path = os.getenv("ACCURACY_OUTPUT_DIR", "results/accuracy/report.json")
    with open(output_path, "w") as f:
        json.dump(accuracy_report, f, indent=4)
