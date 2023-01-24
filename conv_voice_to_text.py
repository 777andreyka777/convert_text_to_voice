import gtts
from playsound import playsound

user_input = input('Введите текст, который хотите воспроизвести голосом: \n')

def save_and_play_file():
    tts = gtts.gTTS(user_input,lang='ru',slow=True)
    tts.save('my_voice.mp3')
    playsound('my_voice.mp3')

save_and_play_file()