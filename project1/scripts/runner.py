import subprocess


def run_script(script_name):
    """
    اجرای یک اسکریپت پایتون.
    """
    subprocess.run(["python", script_name])


if __name__ == "__main__":
    run_script("./detect_boxes.py")
    run_script("./calculate_accuracy.py")
