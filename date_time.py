from datetime import datetime

def Time():
    time = datetime.now().strftime("%H:%M:%S")
    print(time)
    print(type(time))

Time()    