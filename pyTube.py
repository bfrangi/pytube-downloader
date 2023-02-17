
class YTDownload:
    
    def __init__(self, output_path=None):
        self.output_path = output_path or self.default_folder()
        
    def download(self, url, verbose=False):
        from pytube import YouTube
        yt = YouTube(url)
        if verbose: self.show_info(yt)        
        yt = yt.streams.get_highest_resolution()
        try:
            yt.download(output_path=self.output_path)
        except:
            print("An error has occurred")
        print(f"Video downloaded successfully from '{url}'. File stored at '{self.output_path}'")
    
    def default_folder(self):
        import os
        return os.path.join(os.path.expanduser('~'), "Downloads")
    
    def show_info(self, yt):
        print('Title:', yt.title)
        print('Author:', yt.author)
        print('Published date:', yt.publish_date.strftime("%Y-%m-%d"))
        print('Number of views:', yt.views)
        print('Length of video:', yt.length, 'seconds')


def parse_arguments():
    import argparse
    import sys
    
    # Default folder
    downloader = YTDownload()
    DEFAULT_FOLDER = downloader.default_folder()
    
    # Create parser
    parser = argparse.ArgumentParser()
    parser.add_argument('url', nargs='?', default=None)
    parser.add_argument('output_path', nargs='?', default=DEFAULT_FOLDER)
    parser.add_argument('-v', '--verbose', action='store_true', help="use this flag to show more information about the download")
    
    # Parse args
    args = sys.argv[1::]
    output_path = parser.parse_args(args).output_path
    url = parser.parse_args(args).url
    verbose = parser.parse_args(args).verbose
    if not url:
        parser.print_help()
        exit()
        # raise Exception("Please, specify a URL. To see usage, run with -h flag")
    return url, output_path, verbose
    

if __name__=="__main__":
    url, output_path, verbose = parse_arguments()

    downloader = YTDownload(output_path=output_path)
    downloader.download(url, verbose=verbose)
