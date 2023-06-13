[![Donate](https://img.shields.io/badge/Donate-PayPal-green.svg)](https://www.paypal.com/donate/?business=J2SPVFH7QXSRW&no_recurring=0&item_name=Help+me+keep+making+great+things+with+programmation%2C+thank+you%21&currency_code=USD)
### Convert audio to text
![convert-audio-to-text](https://raw.githubusercontent.com/uPablo/convert-audio-to-text/main/assets/convert-audio-to-text.png)

### Requirements
For MacOS using brew:
```bash
brew install ffmpeg
```

For Ubuntu / Debian Linux:
```bash
apt-get install ffmpeg
```

For Windows using Chocolatey:
```bash
choco install ffmpeg
```

---

### By cloning the repository
1. Clone this repository `git clone https://github.com/uPablo/convert-audio-to-text`
2. Install all the requirements `pip install -r requirements.txt` . If you have problems with requirements, make sure to have at least Python3.6. You could also try to create a _virtualenv_ and then install all the requirements
3. Don't forget to change the variable `project_folder` in `run.py` file with the absolute path of your cloned project

```sh
pip install virtualenv
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
```

---

### Proccess
Run `python setup.py` to create the respective folders used in the project.<br/>
![console with instructions to put mp3 in the sound-to-convert folder](https://raw.githubusercontent.com/uPablo/convert-audio-to-text/main/assets/run-python-setup.png)

Put the mp3 songs in `sound-to-convert` folder<br/>
![mp3 songs in sound-to-convert folder](https://raw.githubusercontent.com/uPablo/convert-audio-to-text/main/assets/put-mp3-files-in-sound-to-convert-folder.png)


Start transcripting! `python run.py` 🥳

First step converting all mp3 files to wav files<br/>
![script starts convert to wav and transcript the audio](https://raw.githubusercontent.com/uPablo/convert-audio-to-text/main/assets/run-python-run.png)

Second step starts chunk the wav files in small files to listening them<br/>
![chucking the wav files in small files](https://raw.githubusercontent.com/uPablo/convert-audio-to-text/main/assets/chuncked-audios.png)

Third step after finish run the script will write all the audio converted to text in `audio-to-text-converted` folder with `.txt` extension<br/>
![file txt with audio converted in text](https://raw.githubusercontent.com/uPablo/convert-audio-to-text/main/assets/folders-workflow-transcription.png)

And finally you can see the audio transcription to text<br/>
![txt file with text write inside](https://raw.githubusercontent.com/uPablo/convert-audio-to-text/main/assets/transcription-in-txt-file-finished.png)

---
#BONUS TIPS
If you was installed the ffmpeg globally in your system, you can use the follow command line to convert some extensions to `.mp3`

### MP4
```bash
ffmpeg -i name-of-video.mp4 name-of-audio.mp3
```

### OGG (WhatsApp audio)
```bash
ffmpeg -i name-of-whatsapp-audio.ogg name-of-audio.mp3
```

### All MP4 Files inside a folder
```bash
for f in *.mp4; do ffmpeg -i "$f" "$(basename $f).mp3"; done
```

### All OGG (WhatsApp audio) Files inside a folder
```bash
for f in *.ogg; do ffmpeg -i "$f" "$(basename $f).mp3"; done
```