# This folder is gonna look inside the user_uploads folder and convert them into reels
# if they are not already converted

# we didn't do this in main.py as we wanted it to take care of just uploading
# and this process will take care of generating the reels

# By this we can make our project scalable as main.py focuses on uploading
# and this file work sidely and focuses on generating the reels

import os 
from text_to_audio import text_to_speech_file
import time
import subprocess


def text_to_audio(folder):
    print("TTA - ", folder)
    with open(f"user_uploads/{folder}/desc.txt") as f:
        text = f.read()
    print(text, folder)
    text_to_speech_file(text, folder)

def create_reel(folder):
    command = f'''ffmpeg -f concat -safe 0 -i user_uploads/{folder}/input.txt -i user_uploads/{folder}/audio.mp3 -vf "scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2:black" -c:v libx264 -c:a aac -shortest -r 30 -pix_fmt yuv420p static/reels/{folder}.mp4'''
    subprocess.run(command, shell=True, check=True)
    
    print("CR - ", folder)

if __name__ == "__main__":
    while True:
        print("Processing queue...")
        with open("done.txt", "r") as f: #done.txt contains the folders that are already processed means reels are made
            # so we will not process them again
            done_folders = f.readlines()

        done_folders = [f.strip() for f in done_folders]
        folders = os.listdir("user_uploads") 
        for folder in folders:
            if(folder not in done_folders): #Process only if not already processed(not came in done.txt))
                text_to_audio(folder) # Generate the audio.mp3 from desc.txt
                create_reel(folder) # Convert the images and audio.mp3 inside the folder to a reel
                with open("done.txt", "a") as f:
                    f.write(folder + "\n")
        time.sleep(4)