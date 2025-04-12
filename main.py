import pyttsx3
import speech_recognition as sr
import random
import webbrowser 
import datetime
from plyer import notification
import pyautogui
import wikipedia
import pywhatkit as pwk 
import user_config
import smtplib, ssl
import openai_request as ai
import image_generation
import mtranslate
import replicate


engine = pyttsx3.init()
voices = engine.getProperty('voices')       #getting details of current voice
for voice in voices:
    engine.setProperty('voice', voice.id)   #changing index, changes voices. 1 for female
    engine.setProperty("rate", 200)
    

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def command():
    content = ""
    while content == "":
        # obtain audio from the microphone
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)

        try:
            content = r.recognize_google(audio, language='en-in')
            print("You Said..........." + content )
        except Exception as e:
            print(" Please try again....")

    return content

def main_process():
    jarvis_chat = []
    while True:
        request = command().lower()
        if "hello" in request:
            speak("Welcome, How can i help you.")
        elif "play music" in request:
            speak("Playing music")
            song = random.randint(1,3)
            if song == 1:
                webbrowser.open("https://youtu.be/lBvbNxiVmZA?si=Hkg5sorv6KcDaDc3") 
            elif song == 2:
                webbrowser.open("https://youtu.be/AdBzzpq3xV4?si=6evxwzUIWt34rNWr") 
            elif song == 3:
                webbrowser.open("https://youtu.be/BWczaSneA0Q?si=tl0FhAz6iDucqkPN") 
        elif "say time" in request:
            now_time = datetime.datetime.now().strftime("%H:%M")
            speak("Current time is " + str(now_time))
        elif "say date" in request:
            now_time = datetime.datetime.now().strftime("%d:%m")
            speak("Current date is " + str(now_time))
        elif "new task" in request:
            task = request.replace("new task", "")
            task = task.strip()
            if task != "":
                speak("Adding task : "+ task)
                with open ("todo.txt", "a") as file:
                    file.write(task + "/n")
        elif "speak task" in request:
            with open ("todo.txt", "r") as file:
                speak("Work we have to do today is : " + file.read())
        elif "show work" in request:
            with open ("todo.txt", "r") as file:
                tasks = file.read()
            notification.notify(
                title = "Today's work",
                message = tasks
            )
        elif "open youtube" in request:
            webbrowser.open("www.youtube.com")
        elif "open" in request:
            query = request.replace("open", "")
            pyautogui.press("super")
            pyautogui.typewrite(query)
            pyautogui.sleep(2)
            pyautogui.press("enter")
        elif "wikipedia" in request:
            try:
                request = request.replace("jarvis ", "")
                request = request.replace("search wikipedia ", "")
                request = request.replace("wikipedia ", "")  # also handle this
                result = wikipedia.summary(request, sentences=2)
                speak(result)
            except wikipedia.exceptions.DisambiguationError as e:
                speak("The topic is ambiguous. Please be more specific.")
                print("Disambiguation Error:", e.options)
            except wikipedia.exceptions.PageError:
                speak("Sorry, I could not find any page related to your request.")
            except Exception as e:
                speak("Something went wrong while searching Wikipedia.")
                print("Unexpected Error:", str(e))

        elif "search google" in request:
            request = request.replace("jarvis ", "")
            request = request.replace("search google ", "")
            webbrowser.get("windows-default").open("https://www.google.com/search?q=" + request)
        elif "send whatsapp" in request:
            pwk.sendwhatmsg("+919728021923", "Hi! How are you!", 11, 27, 30)
        #elif "send email" in request:
            #pwk.send_mail("sim.goyal02@gmail.com", user_config.gmail_pass, "Hello", "How are you ?" , "simraniitbonay@gmail.com")
            #speak("Email sent")
        elif "send email" in request:
            try:
                # Email configuration
                sender_email = "sim.goyal02@gmail.com"
                receiver_email = "simraniitbonbay@gmail.com"
                password = user_config.gmail_pass
                
                # Create secure connection
                context = ssl.create_default_context()
                with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                    server.login(sender_email, password)
                    
                    # Construct proper email message with headers
                    subject = "Message from JARVIS"
                    body = """\
                        This is the message.

                        Thanks,
                        Simran
                        """
                    message = f"Subject: {subject}\n\n{body}"
                    
                    server.sendmail(sender_email, receiver_email, message)
                    speak("Email sent successfully!")
                    
            except Exception as e:
                speak(f"Sorry, I couldn't send the email. Error: {str(e)}")
                print(f"Email sending failed: {e}")
        elif "create an image of" in request:
            prompt = request.replace("create an image of", "").strip()
            image_url = image_generation.generate_image(prompt)

            if image_url:
                speak(f"Here is the image of {prompt}")
                print("Generated Image URL:", image_url)
            else:
                speak("Sorry, I couldn't generate the image.")

        elif "ask ai" in request:
            jarvis_chat = []
            request = request.replace("jarvis", "")
            request = request.replace("ask ai", "")
            jarvis_chat.append({"role": "user", "content": request})


            response = ai.send_request(jarvis_chat)
            speak(response)
        elif "clear chat" in request:
            jarvis_chat = []

            speak("Chat cleared")
        elif "ask gemini" in request:
            request = request.replace("jarvis", "")
            request = request.replace("ask gemini", "")
            response = ai.send_request_gemini(request)
            speak(response)

        else:
            request = request.replace("jarvis", "")

            jarvis_chat.append({"role": "user", "content": request})
            response = ai.send_request(jarvis_chat)
            jarvis_chat.append({"role": "assistant", "content": response})
            speak(response)

    
main_process() 






