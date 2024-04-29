import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")

voice = ["yash","Arpit","krutik","shubham","Shyam","Ragho"]

for i in voice:
    speaker.Speak("shot out to a" + i)