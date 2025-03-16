import os
from deepface import DeepFace

def is_man(image_path):
    try:
        analysis = DeepFace.analyze(image_path, actions=["gender"], enforce_detection=False)
        return analysis[0]['dominant_gender'] == "Man"
    except Exception as e:
        print(f"Error analyzing {image_path}: {e}")
        return False
def scan_images(directory="/share/photos"):
    if not os.path.exists(directory):
        print("Directory not found.")
        return
    
    for root, _, files in os.walk(directory):
        for filename in files:
            if filename.lower().endswith((".jpg", ".png", ".jpeg")):
                image_path = os.path.join(root, filename)
                if is_man(image_path):
                    print(f"{image_path}: Man detected")
                else:
                    print(f"{image_path}: Not a man")

if __name__ == "__main__":
    scan_images()

