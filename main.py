import os
import shutil
from recorder import Recorder
import speech_recognition as sr

r = Recorder()

time_sec = int(input("Enter recording time in seconds: "))
lanInput = int(input("Select recording language: (1-English, 2-Turkish) "))
selected_language = ""

if lanInput == 1:
    selected_language = "en-EN"
elif lanInput == 2:
    selected_language = "tr-TR"
else:
    print("Invalid input, English language selected.")

print("---Recording started 🎤---")
temp_output = 'temp_out.wav'
r.record(time_sec, output='temp_out.wav')
print("---Recording ended ⏸️---")

print("Transcribing...")
transcript = sr.Recognizer()
recording = sr.AudioFile('temp_out.wav')
with recording as source:
    audio = transcript.record(source)
    script = transcript.recognize_google(audio, language=selected_language)
    print("Text: "+script)

save_choice = input("Would you like to save the audio?(y/n): ")
if save_choice.lower() == "y":
    out_name = input("Enter name of the output file: ")
    final_output = f'{out_name}.wav'
    shutil.move(temp_output, final_output)
    print(f"Audio saved as {final_output}.")
elif save_choice.lower() == "n":
    os.remove(temp_output)
    print("Audio discarded.")
else:
    os.remove(temp_output)
    print("Invalid input, audio discarded.")