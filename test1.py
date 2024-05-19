from pydub import AudioSegment
import pygame

def play_in_ear(ear):
    # Load audio files for left and right ears
    left_audio = AudioSegment.from_wav("left_ear_digits.wav")
    right_audio = AudioSegment.from_wav("right_ear_digits.wav")

    # Select the audio based on the ear parameter
    if ear == "left":
        selected_audio = left_audio
    elif ear == "right":
        selected_audio = right_audio
    else:
        raise ValueError("Invalid ear selection. Choose 'left' or 'right'.")

    # Convert the selected audio to mono (optional, depending on your needs)
    selected_audio = selected_audio.set_channels(1)

    # Initialize pygame mixer
    pygame.mixer.init()

    # Create a temporary file to store the selected audio
    temp_file_path = "temp_audio.wav"
    selected_audio.export(temp_file_path, format="wav")

    # Play the selected audio
    pygame.mixer.music.load(temp_file_path)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    pygame.quit()

# Example usage
play_in_ear("left")  # Change to "right" to play in the right ear
