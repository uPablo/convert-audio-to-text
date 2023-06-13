import os

source_folder = "sound-to-convert"
destination_wav_folder = "sound-wav-converted"
destination_audio_to_text_folder = "audio-to-text-converted"
destination_audio_chunks = "audio-chunks";

#if source_folder doesn’t exist we create one
if not os.path.exists(source_folder):
    os.makedirs(source_folder)
    print("The source folder is created!")

#if destination_wav_folder doesn’t exist we create one
if not os.path.exists(destination_wav_folder):
    os.makedirs(destination_wav_folder)
    print("The destination folder is created!")

#if destination_audio_to_text_folder doesn’t exist we create one
if not os.path.exists(destination_audio_to_text_folder):
    os.makedirs(destination_audio_to_text_folder)
    print("The transcription of audio to text folder is created!")

#if destination_audio_chunks doesn’t exist we create one
if not os.path.exists(destination_audio_chunks):
    os.makedirs(destination_audio_chunks)
    print("The destination of audio chunks folder is created!")
    
#verify if has some file in this folder to don't show this message
print("Please, put your *.mp3 file in the sound to convert folder")