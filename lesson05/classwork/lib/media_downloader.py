from subprocess import call
import os


class Downloader:
    def menu(self):
        choice = int(
            input("1. Download video\n2. Download playlist (video)\n=> "))
        return choice

    def download_youtube_single_media(self):
        movie_url = input("Enter movie URL: ")
        movie_info = ["youtube-dl", movie_url, "-F"]

        call(movie_info)
        format_ = input("Enter format code: ")
        os.chdir("downloads")

        download_command = ["youtube-dl", "-f", format_, movie_url, "-c"]
        call(download_command)
