from playsound import playsound #for playing sound
from gtts import gTTS #txt to mp3 converting
import speech_recognition as sr

import os
import time
from datetime import datetime
import random
import webbrowser
from selenium import webdriver


r = sr.Recognizer()
def record(ask = False):
    with sr.Microphone() as source:
        if ask:
            print(ask)
        audio = r.listen(source)
        voice = ""
        try:
            voice = r.recognize_google(audio,language = "tr-TR")
        except sr.UnknownValueError:
            print("Assistant: Seni duyamıyorum konuşsana")
        except sr.RequestError:
            print("Assistant: sistem çalışmıyor")
        return voice
def speak(string):
    tts = gTTS(text=string,lang="tr",slow=False)
    file = "answer.mp3"
    tts.save(file)
    playsound(file)
    os.remove(file)

def response(voice):
    if "merhaba" in voice or "selam" in voice or "ne haber" in voice:
        speak("merhaba")
    if "kimsin sen" in voice or "kendini tanıtır mısın" in voice:
        speak("ben Sümer Can ertuğral' ın sesli asistanıyım ve her hafta geliştirilmek üzerine tasarlandım")
    if "sen nasılsın" in voice or "siz nasılsınız" in voice or "nasılsın" in voice or "nasılsınız" in voice:
        speak("iyiyim teşekkür ederim sen nasılsın")
    if "iyiyim" in voice:
        speak("iyi olmana sevindim")
    if "orada mısın" in voice or "beni dinliyor musun" in voice or "beni duyuyor musun" in voice:
        speak("burdayım efendim sizi dinliyorum")
    if "iyi gidiyor" in voice:
        speak("süper")
    if "kaç yaşındasın" in voice:
        speak("tahmin bile edemezsin")
    if "nerelisin" in voice:
        speak("nereli olduğumu ben de bilmiyorum maalesef")
    if "sana soru sorabilir miyim" in voice or "sana soru sormak istiyorum" in voice:
        speak("tabi sorabilirsin seni dinliyorum")
    if "nasıl zayıflayabilirim" in voice:
        speak("uykuna dikkat etmelisin ve spor yapmalısın")
    if "hangi gündeyiz" in voice or "günlerden ne" in voice:
        today = time.strftime("%A")
        today.capitalize()
        if today == "Monday":
            today = "Pazartesi"
        elif today == "Tuesday":
            today = "Salı"
        elif today == "Wednesday":
            today = "Çarşamba"
        elif today == "Thursday":
            today = "Perşembe"
        elif today == "Friday":
            today = "Cuma"
        elif today == "Saturday":
            today = "Cumartesi"
        elif today == "Sunday":
            today = "Pazar"
        speak(today)

    if "saat" in voice:
        selection = ["Saat şuan: ", "Bakıyorum hemen: "]
        clock = datetime.now().strftime("%H:%M")
        speak("saat" + clock)

    if "internette arama yapar mısın" in voice:
        speak("anlaşıldı ne aramamı istersin")
        search = record("anlaşıldı ne aramamı istersin")
        url = "https://www.google.com/search?q=" + search
        webbrowser.get().open(url)
        print(search + "hey bunu buldum")

    if "her şey için teşekkür ederim görüşürüz" in voice or "gitmek gerekiyor görüşürüz" in voice:
        speak("bana zaman ayırdığın için teşekkür ederim tekrar görüşmek üzere kendine iyi bak")
        exit()
#def sleep_untill(voice):

    if "twitter'a giriş yapar mısın" in voice:               #you can log in twitter with your username and password
        import time as tıme #i tryed different type of time and tıme for use of twitter
        speak("twitter hesabına giriş yapıyorum")
        browser = webdriver.Chrome()
        browser.get("https://twitter.com/")
        tıme.sleep(2)
        logIn= browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a/div/span/span")

        logIn.click()
        tıme.sleep(2)
        username = browser.find_element_by_xpath("//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[5]/label/div/div[2]/div/input")
        next = browser.find_element_by_xpath("//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[6]/div")
        username.send_keys("your_username")        #you must enter your username for twitter
        next.click()
        tıme.sleep(2)
        password = browser.find_element_by_xpath("//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input")

        password.send_keys("your_password")        #you must enter your password for twitter
        tıme.sleep(2)
        LogInFinally = browser.find_element_by_xpath("//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div")
        LogInFinally.click()
        tıme.sleep(5)
        tıme.sleep(10)
        #sleep_untill(voice) I will add method or use of twitter
    """if "youtube" in voice or "video müzik açar mısın" in voice:
        speak("anlaşıldı ne açmamı istersin")
        searching = record("***")
        browser = webdriver.Chrome()
        browser.get("https://www.youtube.com/")
        time.sleep(2)
        search = browser.find_element_by_xpath("/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input")
        search.send_keys(searching)
        search.click()
        time.sleep(2)"""
while True:
    voice = record()
    if voice != "":
        voice = voice.lower()
        print(voice)
        response(voice)
