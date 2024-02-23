# imports https://www.youtube.com/watch?v=1O0yazhqaxs

import pytube;
import pathlib;
from pytube import YouTube;
from pytube import Channel;
from pathlib import Path;

# main code
def main():
    teste = input("Put a url: ")
    return teste


def dwn():
    ytrl = YouTube(main());
    chrl = Channel(ytrl.channel_url);

    print("Is your link correct?")
    print(f"Title: {ytrl.title} | Channel: {chrl.channel_name} ")
    choise = input("Y/N: ")

    if choise == "y" or choise == "Y":
        final_y = ytrl.streams.get_highest_resolution()
        video_path = (r"/home/user/Downloads")
        final_y.download(video_path)

        if final_y.exists_at_path(video_path) == True:
            print(f"Your download of {ytrl.title} Is complete!! You can see it in {print(final_y.get_file_path())}")
        else:
            print("senta e chora")
    elif choise == "n" or choise == "N":
        return False
    
    else:
        print("That's not a choise!!")
        return dwn()
    
    dwn()