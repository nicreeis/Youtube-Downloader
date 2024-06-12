from pytube import YouTube
import os
from moviepy.editor import VideoFileClip
import glob

def build_paths(output_path_mp4, output_path_mp3):
    try:
        if not os.path.exists(output_path_mp4):
            os.makedirs(output_path_mp4)
        if not os.path.exists(output_path_mp3):
            os.makedirs(output_path_mp3)
    except Exception as e:
        print(f"An error occurred while creating directories: {e}")
        return None

def download_video(youtube_url,output_path_mp4):

    try:
        # Create a YouTube object
        yt = YouTube(youtube_url)
        
        # Get the highest resolution stream
        video_stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        
        if video_stream is None:
            print(f"No video stream found for {youtube_url}")
            return None

        # Download the video
        output_file = video_stream.download(output_path_mp4)
        print(f"Downloaded: {output_file}")
        return output_file
    
    except Exception as e:
        print(f"An error occurred while downloading {youtube_url}: {e}")
        return None

def convert_to_mp3(video_path,output_path_mp3):
    try:
        base, ext = os.path.splitext(video_path)
        mp3_file = os.path.join(output_path_mp3, os.path.basename(base) + '.mp3')
        
        # Load the video file
        video = VideoFileClip(video_path)
        
        # Write the audio part as an mp3 file
        video.audio.write_audiofile(mp3_file)
        
        print(f"Converted to MP3: {mp3_file}")
        return mp3_file
    except Exception as e:
        print(f"An error occurred while converting {video_path} to MP3: {e}")
        return None

def download_videos_as_mp3(youtube_urls,output_path_mp4,output_path_mp3):
    
    for url in youtube_urls:
        video_path = download_video(url,output_path_mp4)
        if video_path:
            convert_to_mp3(video_path,output_path_mp3)

if __name__ == "__main__":
    
    # Create necessary directories
    output_path_mp4 = 'downloads_mp4'
    output_path_mp3 = 'downloads_mp3'

    build_paths(output_path_mp4,output_path_mp3)

    # List of YouTube URLs to download
    youtube_urls = [
        "https://www.youtube.com/watch?v=2b1IqO4o1pE&ab_channel=JoelPWest-Topic",
        "https://www.youtube.com/watch?v=_-OCLUOHfn0&ab_channel=88rising",
        "https://www.youtube.com/watch?v=qxmWmlyTmvo&ab_channel=JoelPWest-Topic",
        "https://www.youtube.com/watch?v=DOxqAHKMcRc&ab_channel=Release-Topic",
        "https://www.youtube.com/watch?v=9xkMyCQ7CqQ&ab_channel=JoelPWest-Topic",
        "https://www.youtube.com/watch?v=3pZfOHl5F-Y&ab_channel=Anderson.Paak-Topic",
        "https://www.youtube.com/watch?v=2LJjtyNnOWc&ab_channel=SwaeLee",
        "https://www.youtube.com/watch?v=bq7n7rgVyqY&ab_channel=88rising",
        "https://www.youtube.com/watch?v=9jdReDQre38&ab_channel=keshi",
        "https://www.youtube.com/watch?v=zhKJEmPo0pc&ab_channel=JoelPWest-Topic",
        "https://www.youtube.com/watch?v=OANynKu9-KI&ab_channel=JoelPWest-Topic",
        "https://www.youtube.com/watch?v=1vorbfPNW_g&ab_channel=OriginalSoundtrack",
        "https://youtu.be/Vl_yoWSXv8Y?si=yEE3g_iAUm3YEV_x",
        "https://www.youtube.com/watch?v=x-EK-5USFTo&ab_channel=OriginalSoundtrack"
    ]   
    
    # Download all videos in the list as MP3
    download_videos_as_mp3(youtube_urls,output_path_mp4,output_path_mp3)