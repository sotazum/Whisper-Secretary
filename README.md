# Whisper-Secretary
Whisper-Secretary is a tool that allows you to record video meetings as text in your terminal. With Whisper-Secretary, you can keep a record of your meetings and easily search for important information without having to sift through lengthy video recordings.

Whisper: https://github.com/openai/whisper 

## Getting Started
### System Requirements
Whisper-Secretary is designed for Apple Silicon Mac. To get started, you'll need to use Homebrew to install a few packages:

```
brew install ffmpeg
brew install blackhole-2ch
```

BlackHole: https://github.com/ExistentialAudio/BlackHole 

You'll also need to install BlackHole, which is a virtual audio device that allows you to capture the audio output from your Mac.

To set up BlackHole, follow these steps:

1. Open Audio MIDI Setup on your Mac.
2. Click the "+" button in the bottom left corner and select "Create Multi-Output Device".
3. Check the boxes for your Mac's speaker and BlackHole 2ch.
<img src="img/audio_midi.png" width="50%">
4. Open System Preferences and navigate to Sound.
5. Change the sound output to the multi-output device you created.
<img src="img/sound_set.png" width="50%">



### Python Requirements
Whisper-Secretary requires Python 3.10. To install the necessary Python packages, run the following command:

```
brew install portaudio
pip install -r requirements.txt
```

## Usage
To use Whisper-Secretary, run the following command:

```
python main.py
```

This will start recording your meeting and transcribing it to text in your terminal. To stop recording, press ```Ctrl + C```.

## Conclusion
With Whisper-Secretary, you can keep a record of your meetings and easily search for important information without having to sift through lengthy video recordings. We hope you find this tool useful! If you have any questions or feedback, please don't hesitate to reach out.