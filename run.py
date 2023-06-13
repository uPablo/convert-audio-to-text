# Import libraries
import os
from sys import exception
from pydub import AudioSegment
from pydub.silence import split_on_silence
import speech_recognition as sr

r = sr.Recognizer()

source_folder = "sound-to-convert"
destination_wav_folder = "sound-wav-converted"
destination_audio_to_text_folder = "audio-to-text-converted"
destination_audio_chunks = "audio-chunks"

project_folder = "/Users/user/projects/python/convert-audio-to-text"

#function to make the convertion
def transcribe_large_audio(path, audio_name):
    """Split audio into chunks and apply speech recognition"""
    # Open audio file with pydub
    sound = AudioSegment.from_wav(path)

    # Split audio where silence is 700ms or greater and get chunks
    chunks = split_on_silence(sound, min_silence_len=700, silence_thresh=sound.dBFS-14, keep_silence=700)
    
    # Create folder to store audio chunks
    folder_name = destination_audio_chunks + "/" + audio_name
    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)
    
    whole_text = ""
    # Process each chunk
    for i, audio_chunk in enumerate(chunks, start=1):
        # Export chunk and save in folder
        chunk_filename = os.path.join(folder_name, f"chunk{i}.wav")
        audio_chunk.export(chunk_filename, format="wav")

        # Recognize chunk
        with sr.AudioFile(chunk_filename) as source:
            audio_listened = r.record(source)
            # Convert to text
            try:
                text = r.recognize_google(audio_listened, language='pt-BR')
            except sr.UnknownValueError as e:
                print("Error:", str(e))
            else:
                text = f"{text.capitalize()}. "
                print(chunk_filename, ":", text)
                whole_text += text+ '\n'

    # Return text for all chunks
    return whole_text

#get all mp3 files
files = os.listdir(source_folder)
for name in files:
    #name of the file                                                           
    wav_name = name.replace(".mp3", "")
    print("Converting "+wav_name+".mp3 file to wav now.")
    try:
        # convert wav to mp3 
        sound = AudioSegment.from_mp3("{}/{}".format(source_folder, name))
        sound.export("{}/{}".format(destination_wav_folder, wav_name+".wav"), format="wav")
    except exception as e:
        pass


#get all wav files
files_wav = os.listdir(destination_wav_folder)
for name_wav in files_wav:
    #name of the file                                                           
    wav_name = name_wav.replace(".wav", "")
    print("Transcripting "+wav_name+".wav file in text now.")
    try:
        # convert wav to text 
        result = transcribe_large_audio(project_folder + "/" + destination_wav_folder+"/"+wav_name+".wav",wav_name+".wav")
        print(result)
        print(result, file=open(destination_audio_to_text_folder+"/"+wav_name+'.txt', 'w'))
    except exception as e:
        pass

