class YTDownload:

    def __init__(self, output_path=None):
        self.output_path = output_path or self.default_folder()

    def get_highest_resolution_video(self, yt):
        return yt.streams.filter(progressive=False, file_extension='mp4').order_by('resolution').desc().first()

    def get_highest_resolution_audio(self, yt):
        return yt.streams.filter(only_audio=True).order_by('abr').desc().first()

    def download(self, url, verbose=False, dash=False):
        from pytubefix import YouTube
        yt = YouTube(url)
        filename = "".join(i for i in yt.title if i not in "\/:*?<>|")

        if verbose:
            self.show_info(yt)

        if dash:
            print('Downloading DASH streams...')

            video_stream = self.get_highest_resolution_video(yt)
            video_ext = video_stream.mime_type.split("/")[-1]
            filename_video = f"{filename} (Video).{video_ext}"
            self.download_stream(video_stream, filename_video)
            print(
                f"  Video downloaded successfully from '{url}'.\n  File stored at '{self.output_path}/{filename_video}'.")

            audio_stream = self.get_highest_resolution_audio(yt)
            audio_ext = audio_stream.mime_type.split("/")[-1]
            filename_audio = f"{filename} (Audio).{audio_ext}"
            self.download_stream(audio_stream, filename_audio)
            print(
                f"  Audio downloaded successfully from '{url}'.\n  File stored at '{self.output_path}/{filename_audio}'.")

            print('Muxing audio and video...', end=' ')
            self.video_audio_mux(
                f"{self.output_path}/{filename_audio}",
                f"{self.output_path}/{filename_video}",
                f"{self.output_path}/{filename}.{video_ext}")
            print('done!')
            print(
                f"Muxed file stored at '{self.output_path}/{filename}.{video_ext}'.")
            return

        stream = yt.streams.get_highest_resolution()
        ext = stream.mime_type.split("/")[-1]
        self.download_stream(stream, f"{filename}.{ext}")
        print(
            f"Video downloaded successfully from '{url}'. File stored at '{self.output_path}/{filename}.{ext}'.")

    def default_folder(self):
        import os
        return os.path.join(os.path.expanduser('~'), "Downloads")

    def show_info(self, yt):
        print('Title:', yt.title)
        print('Author:', yt.author)
        print('Published date:', yt.publish_date.strftime("%Y-%m-%d"))
        print('Number of views:', yt.views)
        print('Length of video:', yt.length, 'seconds')

    def download_stream(self, stream, filename):
        try:
            stream.download(output_path=self.output_path, filename=filename)
        except Exception as e:
            print("The following error has occurred:")
            print(e)

    def video_audio_mux(self, path_audiosource, path_imagesource, out_video_path):
        import ffmpeg
        video = ffmpeg.input(path_imagesource).video
        audio = ffmpeg.input(path_audiosource).audio
        ffmpeg.output(audio, video, out_video_path,
                      vcodec='copy', acodec='copy', loglevel='quiet').run()


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
    parser.add_argument('-v', '--verbose', action='store_true',
                        help="use this flag to show more information about the download")
    parser.add_argument('-d', '--dash', action='store_true',
                        help="use this flag to download DASH streams (higher quality but video and audio are downloaded separately and then muxed)")

    # Parse args
    args = sys.argv[1::]
    output_path = parser.parse_args(args).output_path
    url = parser.parse_args(args).url
    verbose = parser.parse_args(args).verbose
    dash = parser.parse_args(args).dash
    if not url:
        parser.print_help()
        exit()
        # raise Exception("Please, specify a URL. To see usage, run with -h flag")
    return url, output_path, verbose, dash


if __name__ == "__main__":
    url, output_path, verbose, dash = parse_arguments()

    downloader = YTDownload(output_path=output_path)
    downloader.download(url, verbose=verbose, dash=dash)
