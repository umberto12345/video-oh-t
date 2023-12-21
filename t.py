import youtube_dl
from moviepy.editor import AudioFileClip
import speech_recognition as sr
from gtts import gTTS
from googletrans import Translator
import os

# Funzione per scaricare il video da un link YouTube
def scarica_video(link):
    ydl_opts = {}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])

# Funzione per estrarre l'audio dal video
def estrai_audio(video_file):
    video = AudioFileClip(video_file)
    audio_file = video_file.replace(".mp4", ".mp3")
    video.audio.write_audiofile(audio_file)
    return audio_file

# Funzione per eseguire la trascrizione dell'audio
def trascrivi_audio(audio_file):
    recognizer = sr.Recognizer()
    audio = sr.AudioFile(audio_file)
    with audio as source:
        audio_data = recognizer.record(source)
    text = recognizer.recognize_google(audio_data, language='en-US')  # Imposta la lingua inglese
    return text

# Funzione per eseguire la traduzione del testo dall'inglese all'italiano
def traduci_testo(testo_inglese):
    translator = Translator()
    translation = translator.translate(testo_inglese, src='en', dest='it')  # Da inglese a italiano
    return translation.text

# Funzione per eseguire la sintesi vocale del testo trascritto e tradotto
def esegui_sintesi_vocale(testo):
    tts = gTTS(text=testo, lang='it')  # Imposta la lingua italiana
    tts.save("output.mp3")
    os.system("start output.mp3")  # Apre il file audio

# URL del video da YouTube
url_video = 'INSERISCI_QUI_IL_LINK_DEL_VIDEO'

# Scarica il video da YouTube
scarica_video(url_video)

# Nome del file video scaricato
video_file = 'NOME_DEL_TUO_FILE.mp4'  # Cambia questo con il nome del tuo file video

# Estrai l'audio dal video
audio_file = estrai_audio(video_file)

# Esegui la trascrizione dell'audio
testo_trascritto = trascrivi_audio(audio_file)
print("Testo trascritto (inglese):", testo_trascritto)

# Traduci il testo dall'inglese all'italiano
testo_tradotto = traduci_testo(testo_trascritto)
print("Testo tradotto (italiano):", testo_tradotto)

# Esegui la sintesi vocale del testo tradotto
esegui_sintesi_vocale(testo_tradotto)
