import time
from plyer import notification
if __name__=="__main__":
    while True:
        notification.notify(
        title = "**Please Drink Water Now!!",
        message = "Its time to Drink Water 🍹.",
        app_icon = "D:/code/Downloads/Icons.ico.ico",
        timeout=10,
    )
        time.sleep(60*60)