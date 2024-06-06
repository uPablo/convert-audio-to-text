# Import libraries
import os
import sys
from pydub import AudioSegment
from pydub.silence import split_on_silence
import speech_recognition as sr

r = sr.Recognizer()

source_folder = "sound-to-convert"
destination_wav_folder = "sound-wav-converted"
destination_audio_to_text_folder = "audio-to-text-converted"
destination_audio_chunks = "audio-chunks"

project_folder = "/usr/src/app"  # Atualizado para o caminho do contêiner Docker

# Function to make the conversion
def transcribe_large_audio(path, audio_name):
    """Split audio into chunks and apply speech recognition"""
    # Open audio file with pydub
    sound = AudioSegment.from_wav(path)

    # Split audio where silence is 700ms or greater and get chunks
    chunks = split_on_silence(sound, min_silence_len=700, silence_thresh=sound.dBFS-14, keep_silence=700)
    
    # Create folder to store audio chunks
    folder_name = os.path.join(destination_audio_chunks, audio_name)
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
                whole_text += text + '\n'

    # Return text for all chunks
    return whole_text

# Ensure directories exist
os.makedirs(destination_wav_folder, exist_ok=True)
os.makedirs(destination_audio_to_text_folder, exist_ok=True)
os.makedirs(destination_audio_chunks, exist_ok=True)

# Get all mp3 files
files = os.listdir(source_folder)
for name in files:
    file_path = os.path.join(source_folder, name)
    if os.path.isdir(file_path):
        continue
    # Name of the file
    wav_name = name.replace(".mp3", "")
    print(f"Converting {wav_name}.mp3 file to wav now.")
    try:
        # Convert mp3 to wav
        sound = AudioSegment.from_mp3(file_path)
        sound.export(os.path.join(destination_wav_folder, f"{wav_name}.wav"), format="wav")
    except Exception as e:
        print(f"Error converting {name}: {e}")

# Get all wav files
files_wav = os.listdir(destination_wav_folder)
for name_wav in files_wav:
    file_path_wav = os.path.join(destination_wav_folder, name_wav)
    if os.path.isdir(file_path_wav):
        continue
    # Name of the file
    wav_name = name_wav.replace(".wav", "")
    print(f"Transcripting {wav_name}.wav file in text now.")
    try:
        # Convert wav to text
        result = transcribe_large_audio(file_path_wav, wav_name)
        print(result)
        with open(os.path.join(destination_audio_to_text_folder, f"{wav_name}.txt"), 'w') as f:
            f.write(result)
    except Exception as e:
        print(f"Error transcripting {name_wav}: {e}")
