import  time
t = time.strftime('%H:%M:,%S')
hour = int(time.strftime('%H'))
minute = int(time.strftime('%M'))
second = int(time.strftime('%S'))
print(hour,minute,second)

if(hour>=0 and hour<=12):
    print("Good morning")
elif(hour>=12 and hour<=17):
    print("Good afternoon")
elif(hour>=17 and hour<=21):
    print("Good Evening")
else:
    print("Good night")
