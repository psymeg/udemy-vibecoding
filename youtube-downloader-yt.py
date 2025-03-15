import yt_dlp

def download_youtube_video(url, save_path="."):
    ydl_opts = {
        "outtmpl": f"{save_path}/%(title)s.%(ext)s"
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")
    download_youtube_video(video_url)
