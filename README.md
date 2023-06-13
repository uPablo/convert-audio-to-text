### Convert audio to text
[image-with-text-in-terminal]

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
### By cloning the repository
1. Clone this repository `git clone https://github.com/uPablo/convert-audio-to-text`
2. Install all the requirements `pip install -r requirements.txt` . If you have problems with requirements, make sure to have at least Python3.6. You could also try to create a _virtualenv_ and then install all the requirements

```sh
pip install virtualenv
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
```

Run `python setup.py` to create the respective folders used in the project.

Start transcripting! `python run.py` 🥳