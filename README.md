# Python YouTube Downloader

Simple CLI for downloading youtube videos from the command line.

## Setup

To set this CLI up, please follow these steps:

1. Clone the repo to your preferred location:

    ```
    git clone https://github.com/bfrangi/pytube-downloader.git
    ```
2. Navigate to your home folder:

    ```
    cd ~
    ```

3. Open up your `.bashrc` or `.zshrc` file.
4. Add the following alias:

    ```
    alias pytube="python3 /path/to/pytube-downloader/pyTube.py"
    ```
5. Restart your terminal
6. Now you can simply use the downloader as:

    ```
    pytube [url] [output_path]
    ```

## Usage

Use the `--help` flag to see usage information. 

```
>>> pytube --help
usage: pyTube.py [-h] [-v] [url] [output_path]

positional arguments:
  url
  output_path

optional arguments:
  -h, --help     show this help message and exit
  -v, --verbose  use this flag to show more information about the download
```
