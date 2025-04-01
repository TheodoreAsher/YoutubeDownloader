import yt_dlp
import os
import shutil
from time import sleep

def check_ffmpeg():
    return shutil.which("ffmpeg") is not None

def download_youtube_video(url, max_retries=3):
    try:
        if not check_ffmpeg():
            raise Exception("ffmpeg is not installed or not in PATH. Install it to merge video and audio streams.")
        
        # Define download options
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',  # Best quality video + audio
            'outtmpl': os.path.join('downloads', '%(title)s.%(ext)s'),  # Save to downloads
            'merge_output_format': 'mp4',  # Ensure MP4 output
            'quiet': False,
            'retries': max_retries,  # Retry on failure
            'retry_sleep': 5,  # Wait 5 seconds between retries
        }
        
        # Create yt-dlp object
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # Extract video info
            info = ydl.extract_info(url, download=False)
            
            # Display video details
            print(f"Title: {info['title']}")
            print(f"Author: {info.get('uploader', 'Unknown')}")
            print("\nDownload Details:")
            print(f"Format: MP4")
            print(f"Resolution: {info.get('resolution', 'Unknown') or info.get('height', 'Unknown')}p")
            print(f"File Size: {(info.get('filesize_approx', 0) / 1048576):.2f} MB (approx)")
            
            # Confirm download
            confirm = input("\nDo you want to proceed with the download? (yes/no): ").lower()
            if confirm != 'yes':
                print("Download cancelled.")
                return
            
            # Download with retry logic
            print("Starting download...")
            for attempt in range(max_retries + 1):
                try:
                    ydl.download([url])
                    break  # Exit loop if successful
                except yt_dlp.utils.DownloadError as e:
                    if attempt < max_retries:
                        print(f"Download failed: {e}. Retrying ({attempt + 1}/{max_retries})...")
                        sleep(5)  # Wait before retrying
                    else:
                        raise Exception(f"Download failed after {max_retries} attempts: {e}")
            
            download_path = os.path.join(os.getcwd(), "downloads")
            print(f"\nDownload completed! File saved in: {download_path}")
            
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        print("Troubleshooting tips:")
        print("- Check your internet connection stability")
        print("- Update yt-dlp: 'pip install -U yt-dlp'")
        print("- Try a smaller resolution: edit 'format' to 'bestvideo[height<=1080]+bestaudio/best'")
        print("- Use a VPN if the video is region-restricted")

if __name__ == "__main__":
    youtube_url = input("Please enter the YouTube URL: ")
    download_youtube_video(youtube_url)