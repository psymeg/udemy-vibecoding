#this doesnt work - youtube returns a 403 with pytube
from pytube import YouTube

def download_youtube_video(url, save_path="."):
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        print(f"Downloading: {yt.title}")
        stream.download(save_path)
        print("Download complete!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")
    download_youtube_video(video_url)

