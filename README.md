<h1 align="center"> YoutubeDownloader </h1>

<p align="center">
  <a href="#-about">About</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-features">Features</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-requirements">Requirements</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-usage">Usage</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-contributing">Contributing</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-license">License</a>
</p>
</p>

<p align="center">
  <img alt="License" src="https://img.shields.io/static/v1?label=license&message=MIT&color=49AA26&labelColor=000000">
</p>

## About

This project provides a Python script to download YouTube videos and convert them to MP3 files. It utilizes the pytube library to handle video downloads and moviepy for audio extraction.

## Features
- Downloads YouTube videos in the highest resolution available.
- Converts downloaded videos to MP3 format.
- Organizes downloaded videos and MP3 files into specified directories.

## Requirements
- Python 3.6 or higher
- pytube
- moviepy

Don't forget to install the required libraries using pip:
```bash
pip install pytube moviepy
```
## Usage

**1. Clone the repository:**
```bash
git clone https://github.com/yourusername/youtube-to-mp3-downloader.git
cd youtube-to-mp3-downloader
```

**2. Edit the script:**

Edit the script to include the YouTube URLs you wish to download and convert, you can add as many links as you like:
```python
#List of YouTube URLs to download
youtube_urls = [
    "youtube link here",
    "youtube link here",
    "youtube link here"
]
```
**3. Then run the script**

Your videos and audios will be downloaded and displayed in the directories specified in the code.

## Contributing
Feel free to fork the repository and submit pull requests. For major changes, please open an issue to discuss what you would like to change.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
