import yt_dlp

def download_video(link, best_audio_and_video=False):
    # Options for yt-dlp
    ydl_opts = {
        'outtmpl': '%(title)s.%(ext)s',
    }
    
    if best_audio_and_video:
        ydl_opts['format'] = 'bestaudio+bestaudio/best'  # Download best available audio and video combined

    try:
        # Download the video or audio
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(link, download=True)
            print(f"Downloaded: {info_dict['title']}")
    except Exception as e:
        print("An error occurred:", e)

def main():
    print("YouTube Downloader")
    print("1. Download video")
    print("2. Download best audio and video combined")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice in ['1', '2']:
        copy_link = input("Enter the video download link: ")
        best_audio_and_video = choice == '2'
        download_video(copy_link, best_audio_and_video)
    elif choice == '3':
        print("Exiting...")
    else:
        print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
