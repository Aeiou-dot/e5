# e5
import time

def start_focus_timer(minutes):
    seconds = minutes * 60
    while seconds > 0:
        print(f"Remaining time: {seconds // 60} minutes {seconds % 60} seconds")
        time.sleep(1)
        seconds -= 1
    print("Time's up! Stay focused!")

# 设置专注时间为25分钟
focus_minutes = 25

start_focus_timer(focus_minutes)
