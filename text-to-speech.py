from gtts import gTTS
import os

def text_to_speech(input_file, output_file="output.mp3", language="en"):
    try:
        with open(input_file, "r", encoding="utf-8") as file:
            text = file.read().strip()
            
            if not text:
                print("Error: The input file is empty.")
                return
            
            tts = gTTS(text=text, lang=language, slow=False)
            tts.save(output_file)
            print(f"Audio file saved as {output_file}")
            
            # Optionally play the audio file
            os.system(f"mpg321 {output_file}" if os.name != "nt" else f"start {output_file}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    text_to_speech("speech.txt")
