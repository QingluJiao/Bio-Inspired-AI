import speech_recognition as sr

# 创建 SpeechRecognition 对象
r = sr.Recognizer()
'''
# 读取音频文件
audio_file = './audio.wav'
with sr.AudioFile(audio_file) as source:
    audio = r.record(source)

'''
# 开始监听语音
with sr.Microphone() as source:
    print("请开始说话...")
    audio = r.listen(source)



# 识别音频文件
try:
    print(r.recognize_google(audio, language='zh-CN'))
except sr.UnknownValueError:
    raise 'Google Speech Recognition could not understand audio'
except sr.RequestError as e:
    raise 'Could not request results from Google Speech Recognition Service'
