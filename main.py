import speech_recognition as sr
import pyaudio
from gtts import gTTS
import pygame 
from io import BytesIO
def bot_listening():
    rg = sr.Recognizer()
    with sr.Microphone() as source: # 語音來源
        audioData = rg.listen(source)
    try:
        text = rg.recognize_google(audioData, language='zh-tw')
    except:
        text = None
    return text    
import os
import tempfile
class speech_to_text:
    def __init__(self):  
        self.rg = sr.Recognizer()
    def listen(self,lang='zh-tw'):  
        with sr.Microphone() as source:
            audioData = self.rg.listen(source)
            try:
                text = self.rg.recognize_google(audioData, language=lang)    
            except:
                text = ''
        return text

class text_to_speech:
    def __init__(self):
        self.active_mp3  = '\\tmp\\tmp.mp3'
        pygame.mixer.init()
    def __del__(self):
        try:
          os.unlink(self.active_mp3)  
        except:
          pass  
    def speak(self,text,lang='zh-tw'): 
        tts= gTTS(text, lang=lang)
        tts.save(self.active_mp3)
        pygame.mixer.music.load(self.active_mp3)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
          continue
        pygame.mixer.music.unload()
        return
  
        
st = speech_to_text()
ts = text_to_speech()
userInput=st.listen()         #監聽使用者語音輸入
print("語音輸入內容:")
print(userInput)
print("===============")
# ts.speak(userInput)

#如何切割使用者語音輸入成各個成績?
#...

testper = int(input()) #小考佔比
midexamper = int(input()) #期中考佔比
homeworkper = int(input()) #作業佔比
finalexamper = int(input()) #期末考佔比
testtime = int(input()) #小考次數
testsum = 0 #小考總成績
for i in range(0, testtime):
    testsum += int(input())
midexamscore = int(input()) #期中考成績
homeworkscore = int(input()) #作業成績

finalsum = testsum / testtime * testper / 100 + midexamscore * midexamper / 100 + homeworkscore * homeworkper / 100 #學期最後成績
finalexamscore = int((60 - finalsum) * 100 / finalexamper) #期末考成績

if finalexamscore <= 0:
    output = "期末考不須考即可通過該科目"
elif finalexamscore > 100:
    output = "期末考考多少都無法通過該科目"
else:
    output = "期末考考" + str(finalexamscore) + "分即可通過該科目"

ts.speak(output)      #回答使用者
print("語音輸出內容:")
print(output)
print("===============")
