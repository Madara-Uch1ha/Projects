# # import required libraries
# # pip install scipy wavio
# import sounddevice as sd
# from scipy.io.wavfile import write
# import wavio as wv

# # Sampling frequency
# freq = 44100

# # Recording duration
# duration = 5

# # Start recorder with the given values 
# # of duration and sample frequency
# print(f"Recording for {duration} seconds...")
# recording = sd.rec(int(duration * freq), 
# 				samplerate=freq, channels=2)

# # Record audio for the given number of seconds
# sd.wait()

# # This will convert the NumPy array to an audio
# # file with the given sampling frequency
# print("Completed recording...saving recording")
# write("recording0.wav", freq, recording)

# # Convert the NumPy array to audio file
# wv.write("recording1.wav", recording, freq, sampwidth=2)
import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv
import time

# Sampling frequency
freq = 44100

# Recording duration
duration = 5

# Countdown interval in milliseconds
countdown_interval = 1000  # Adjust this value to make the countdown faster or slower

# Start recording
start_time = time.time()
print(f"Recording started at {time.strftime('%X')}")

# Display countdown


print("\nRecording...")

# Record audio for the given number of seconds
recording = sd.rec(int(duration * freq), samplerate=freq, channels=2)
for i in range(duration, 0, -1):
    print(f"{i}...", end='', flush=True)
    time.sleep(countdown_interval / 1000)  # Pause for the specified interval
sd.wait()

# Calculate and display the elapsed time
elapsed_time = time.time() - start_time
print(f"\nRecording completed at {time.strftime('%X')}. Elapsed time: {elapsed_time:.2f} seconds")

# Save the recording
print("Saving recording...")
write("recording0.wav", freq, recording)

# Convert the NumPy array to an audio file
wv.write("recording1.wav", recording, freq, sampwidth=2)

print("Recording saved successfully.")
