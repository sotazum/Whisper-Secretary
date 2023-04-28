from io import BytesIO

import numpy as np
import soundfile as sf
import speech_recognition as sr
import whisper

if __name__ == "__main__":
    model = whisper.load_model("base")

    recognizer = sr.Recognizer()
    while True:
        # Get microphone input
        with sr.Microphone(sample_rate=16_000) as source:
            print("[Blank]")
            audio = recognizer.listen(source)

        print("[Processing ...]")
        wav_bytes = audio.get_wav_data()
        wav_stream = BytesIO(wav_bytes)
        audio_array, sampling_rate = sf.read(wav_stream)
        audio_fp32 = audio_array.astype(np.float32)

        result = model.transcribe(audio_fp32, fp16=False)
        print(result["text"])