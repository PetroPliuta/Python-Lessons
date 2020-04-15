from lib.media_downloader import Downloader

import subprocess
subprocess.call("ls -l",shell=True)

while True:
    media_file = Downloader()
    choice = media_file.menu()
    if choice == 1:
        media_file.download_youtube_single_media()
    elif choice == 2:
        pass
    elif choice == 0:
        exit()
