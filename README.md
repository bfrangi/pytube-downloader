# Python YouTube Downloader

Simple CLI for downloading youtube videos from the command line.

## Setup

To set this CLI up, please follow these steps:

1. Clone the repo to your preferred location:

    ```
    git clone https://github.com/bfrangi/pytube-downloader.git
    ```
2. Install `pytube`:

    ```
    pip install pytube ffmpeg-python
    ```
3. Navigate to your home folder:

    ```
    cd ~
    ```

4. Open up your `.bashrc` or `.zshrc` file.
5. Add the following alias, replacing `/path/to/pytube-downloader` with the path to the cloned repo:

    ```
    alias pytube="python3 /path/to/pytube-downloader/pyTube.py"
    ```
6. Restart your terminal
7. Now you can simply use the downloader as:

    ```
    pytube [url] [output_path]
    ```

## Usage

Use the `--help` flag to see usage information. 

```
>>> pytube --help
usage: pyTube.py [-h] [-v] [-d] [url] [output_path]

positional arguments:
  url
  output_path

options:
  -h, --help     show this help message and exit
  -v, --verbose  use this flag to show more information about the download
  -d, --dash     use this flag to download DASH streams (higher quality but video and audio
                 are downloaded separately and then muxed)

```
