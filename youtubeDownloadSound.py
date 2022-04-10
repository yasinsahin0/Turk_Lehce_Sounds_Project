import pandas as pd
import numpy as np
import os
import youtube_dl

class SoundDownload:

    def __init__(self):
        self.class_column_name = "lehce"
        self.csv_data="sound_download/youtube_sound_data.csv"
        self.sound_download_file = "sound_download"
        self.main_path = os.getcwd()

    def class_name_file_create(self):
        try:
            data = pd.read_csv(self.main_path + "/" + self.csv_data)
            class_count = len(data[self.class_column_name])
            class_name_list = []
            for cls in range(1, class_count):
                class_name = data[self.class_column_name][cls]
                class_name_list.append(class_name)
            for file_name in set(class_name_list):
                os.mkdir(self.main_path + "/" + self.sound_download_file + "/" + file_name)
            return True
        except Exception as e:
            print(e)
            return False

    def download_sound(self,download_path,video_link, sound_type="wav"):
        try:
            ydl_opts = {'format': 'bestaudio/best',
                        'outtmpl': os.path.join(download_path, '%(title)s.' + sound_type),
                        'postprocessors': [{
                            'key': 'FFmpegExtractAudio',
                            'preferredcodec': sound_type,
                            'preferredquality': '192', }], }
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                infos = ydl.extract_info(video_link, download=True)
                filename_base = ydl.prepare_filename(infos)
            return True
        except Exception as e:
            print(e)
            return False



nesne = SoundDownload()
nesne.download_sound("sound_download","https://youtu.be/XC0e6-U6yfk")
# nesne.class_name_file_create()

