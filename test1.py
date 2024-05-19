from transformers import WhisperProcessor, WhisperForConditionalGeneration
from datasets import load_dataset
import sounddevice as sd
import numpy as np
import os

# Function to record audio
def record_audio(duration=5, filename='recorded_audio.wav'):
    fs = 16000  # Sample rate
    seconds = duration  # Duration of recording

    print(f"Recording for {seconds} seconds...")
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
    sd.wait()  # Wait until recording is done
    print("Finished recording.")
    
    buffer = io.BytesIO()
    np.save(buffer, myrecording)
    buffer.seek(0)
    with open(filename, 'wb') as f:
        f.write(buffer.getvalue())
    print(f"Saved recording to {filename}")

# Record audio
record_audio()

# Load model and processor
processor = WhisperProcessor.from_pretrained("openai/whisper-tiny")
model = WhisperForConditionalGeneration.from_pretrained("openai/whisper-tiny")
model.config.forced_decoder_ids = None

# Read the recorded audio file
with open('recorded_audio.wav', 'rb') as f:
    audio_bytes = f.read()

# Process the audio bytes
input_features = processor(audio_bytes, sampling_rate=16000, return_tensors="pt").input_features

# Generate token IDs
predicted_ids = model.generate(input_features)

# Decode token IDs to text
transcription = processor.batch_decode(predicted_ids, skip_special_tokens=True)

print(transcription)
