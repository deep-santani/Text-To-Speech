from gtts import gTTS

# Text you want to convert to speech
text = "Hello, this is a text-to-speech example in Python."

# Create a gTTS object
tts = gTTS(text)

# Save the audio file
tts.save("output.mp3")

# You can also play the speech directly using a media player library like vlc
# from vlc import MediaPlayer
# player = MediaPlayer("output.mp3")
# player.play()
