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
        self.active_mp3  = 'D:\\HomeWork\\Python\\CAL\\tmp\\tmp.mp3'
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



percents=[0,0,0,0]
exam=[]
examN=0
mid=0
homework=[]
HwN=0
final=0
Ans=0


def getUserInput():
    ret=st.listen()
    print(ret)
    if ret=="":
        ts.speak("再說一次")
        return getUserInput()
    if ret=='一' :
        ret=1
    if ret=='三' :
        ret=3
    return int(ret)

def checkPercents():
    global percents
    tmp=0
    for x in percents:
        tmp+=x
    if tmp==100 :
        return True
    else :
        return False
    

def getExam():
    global exam
    global examN
    ts.speak("請輸入小考次數")
    examN=getUserInput()
    exam=[0]*examN
    for i in range(1,examN+1):
        s="請輸入第"+str(i)+"次小考成績"
        ts.speak(s)
        score=getUserInput()
        exam[i-1]=score
    
def getHomework():
    global homework
    global HwN
    ts.speak("請輸入作業次數")
    HwN=getUserInput()
    homework=[0]*HwN
    for i in range(1,HwN+1):
        s="請輸入第"+str(i)+"個作業成績"
        ts.speak(s)
        score=getUserInput()
        homework[i-1]=score

def calScore():
    global percents
    global exam
    global examN
    global homework
    global HwN
    global mid
    examSum=0
    global Ans
    for x in exam:
        examSum+=x
    if examN>0:
        examSum/=float(examN)
    print(examSum)
    HwSum=0
    for x in homework:
        HwSum+=x
    if HwN>0:
        HwSum/=float(HwN)
    print(HwSum)
    Ans=int((6000-(percents[0]*examSum)-(percents[1]*mid)-(percents[2]*HwSum))/float(percents[3]))
    print(Ans)

def start():
    global percents
    global mid
    ts.speak("歡迎使用成績計算機")
    ts.speak("請輸入小考占總成績百分比")
    percents[0]=getUserInput()
    ts.speak("請輸入期中考占總成績百分比")
    percents[1]=getUserInput()
    ts.speak("請輸入作業占總成績百分比")
    percents[2]=getUserInput()
    ts.speak("請輸入期末考占總成績百分比")
    percents[3]=getUserInput()
    print(percents)
    if checkPercents()==True:
        getExam()
        ts.speak("請輸入期中考成績")
        mid=getUserInput()
        getHomework()
        ts.speak("開始計算成績")
        calScore()
        
    else :
        ts.speak("輸入百分比有誤")
        ts.speak("請重新輸入")
        return True
    
    return False


def main():
    # calScore()
    # print(Ans)
    # print(str(Ans))
    # ts.speak(str(Ans))

    restart=start()
    while restart==True:
        restart=start()
    if Ans<0 :
        ts.speak("你是天才，不用考期末考了")
    elif Ans<100:
        print(Ans)
        s="期末考只需要考"+str(Ans)+"分就會過了"
        ts.speak(s)
    else:
        ts.speak("你沒救了等著重修吧")
    print(exam)
    print(homework)
    print(mid)

if __name__ == '__main__':
    main()