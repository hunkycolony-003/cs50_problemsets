from datetime import datetime

def get_time():
    time = datetime.now().hour + 5

    if 5 <= time < 12:
        return "Morning"
    elif 12 <= time < 16:
        return "Afternoon"
    elif 16 <= time < 21:
        return "Evening"
    else:
        return "Night"
